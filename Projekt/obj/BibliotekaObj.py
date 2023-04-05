import os
import csv
from obj.dataObjects import Ksiazka
from obj.dataObjects import Czytacz, Ksiazka
import utils.utils as u
import utils.constants as c
import utils.db as db


class Biblioteka:
    def __init__(self, TEST_MODE) -> None:
        self.ksiazki: list[Ksiazka] = []
        self.czytacze: list[Czytacz] = []
        self.wypozyczoneKsiazki: list[Ksiazka] = []
        self.operacje: list[list] = []
        self.TEST_MODE = TEST_MODE

    def __str__(self):
        return (f"ksiazki: {self.ksiazki}"
                f"czytacze: {self.czytacze}"
                f"wypozyczoneKsiazki: {self.wypozyczoneKsiazki}"
                f"operacje: {self.operacje}")

    @property
    def iloscKsiazek(self):
        return len(self.ksiazki)

    @property
    def iloscCzytaczy(self):
        return len(self.czytacze)
    
    def ladujBiblioteke(self):
        if os.path.join(c.FOLDER_DANYCH, f"biblioteka.csv"):
            with open(os.path.join(c.FOLDER_DANYCH, f"biblioteka.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.dodajKsiazke(row[1], row[2], row[3], row[4])
        if os.path.join(c.FOLDER_DANYCH, f"czytacze.csv"):
            with open(os.path.join(c.FOLDER_DANYCH, f"czytacze.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.dodajCzytacza(row[1], row[2])
        if os.path.join(c.FOLDER_DANYCH, f"historia.csv"):
            with open(os.path.join(c.FOLDER_DANYCH, f"historia.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.operacje.append(row)

    def dodajKsiazke(self, tytul=None, autor=None, rokWydania=None, status=None) -> None:
        try:
            readInput = False
            if (not tytul):
                tytul = u.czyscWejscie(input("Podaj tytuł: "),
                                     trybTestowania=self.TEST_MODE)
                readInput = True
            if (not autor):
                autor = u.czyscWejscie(
                    input("Podaj autora: "), trybTestowania=self.TEST_MODE)
                readInput = True
            if (not rokWydania):
                rokWydania = u.waliduj_date_z_wejscia(u.czyscWejscie(
                    input("Podaj rok wydania (w formacie YYYY): "), trybTestowania=self.TEST_MODE), "%Y")
                if not rokWydania:
                    raise ValueError("Invalid date provided")
                readInput = True
            self.ksiazki.append(
                Ksiazka(tytul, autor, rokWydania, self.iloscKsiazek, status))
            if (readInput):
                status = "W bibliotece"
                db.zapiszDoPliku(os.path.join(c.FOLDER_DANYCH, "biblioteka.csv"), [self.iloscKsiazek, tytul,
                                                                          autor, rokWydania, status])
        except:
            print("Nie udało się dodać książki...")

    def dodajCzytacza(self, imie=None, nazwisko=None) -> None:
        try:
            readinput = False
            if (not imie):
                imie = u.czyscWejscie(input("imię: "), trybTestowania=self.TEST_MODE)
                readinput = True
            if (not nazwisko):
                nazwisko = u.czyscWejscie(
                    input("nazwisko: "), trybTestowania=self.TEST_MODE)
                readinput = True
            self.czytacze.append(Czytacz(self.iloscCzytaczy, imie, nazwisko))
            if (readinput):
                db.zapiszDoPliku(os.path.join(c.FOLDER_DANYCH, "czytacze.csv"),
                             [self.iloscCzytaczy, imie, nazwisko, 0])
        except:
            print("Nie udało się dodać czytacza...")

    def wypozyczKsiazke(self):
        try:
            ksiazka = self.find_book_by_title_or_index()
            ksiazka.status = "Nie w bibliotece"
            indeksCzytacza = int(u.czyscWejscie(
                input("numer czytacza: "), trybTestowania=self.TEST_MODE))
            imie = u.czyscWejscie(input("imię: "), trybTestowania=self.TEST_MODE)
            nazwisko = u.czyscWejscie(
                input("nazwisko: "), trybTestowania=self.TEST_MODE)
            czytacz = self.znajdzCzytacza(indeksCzytacza)
            if not (czytacz.imie == imie and czytacz.nazwisko == nazwisko):
                raise ValueError("Nie znaleziono takiego czytacza.")
            dataWypozyczenia = u.waliduj_date_z_wejscia(
                u.czyscWejscie(input("data wypozyczenia (w formacie yyyy-mm-dd): "), trybTestowania=self.TEST_MODE))
            if not dataWypozyczenia:
                raise ValueError("Invalid date provided")
            czyUdana = True
            czytacz.wypozyczoneKsiazki.append(ksiazka)
            db.aktualizuj_czytaczy(
                indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
            db.aktualizuj_biblioteke(ksiazka.indeksKsiazki, ksiazka.status)
            op = [ksiazka.indeksKsiazki, indeksCzytacza,
                czyUdana, dataWypozyczenia, 0]
            self.operacje.append(op)
            db.zapiszDoPliku(os.path.join(c.FOLDER_DANYCH, 'historia.csv'),
                        self.operacje[-1])
        except Exception as e:
            data = [ksiazka.indeksKsiazki if 'ksiazka' in locals() else '',
                    indeksCzytacza if 'indeksCzytacza' in locals() else '',
                    False, dataWypozyczenia if 'dataWypozyczenia' in locals() else '',
                    0]
            self.operacje.append(data)
            db.zapiszDoPliku(os.path.join(c.FOLDER_DANYCH, 'historia.csv'),
                        self.operacje[-1])
            print("Nie udało się wypożyczyć książki...", e)

    def oddajKsiazke(self):
        czyUdana = False
        his = ["", "", czyUdana]
        try:
            ksiazka = self.find_book_by_title_or_index()
            his[0] = ksiazka.indeksKsiazki
            dataOddania = u.waliduj_date_z_wejscia(
                u.czyscWejscie(input("Podaj datę oddania (w formacie yyyy-mm-dd): "), trybTestowania=self.TEST_MODE))
            if not dataOddania:
                raise ValueError("Invalid date provided")
            his[1] = dataOddania
            indeksCzytacza = int(u.czyscWejscie(
                input("numer czytacza: "), trybTestowania=self.TEST_MODE))
            for op in self.operacje:
                if (op[0] == str(ksiazka.indeksKsiazki) and op[1] == str(indeksCzytacza)):
                    if u.waliduj_date_z_wejscia(op[3]) > dataOddania:
                        raise ValueError(
                            "Nie można oddać książki przed datą wypożyczenia")
                    if (ksiazka.status[4] == "W bibliotece"):
                        raise ValueError("Książka już oddana")
                    op[4] = u.date_to_str(dataOddania)
            czytacz = self.znajdzCzytacza(indeksCzytacza)
            for k in czytacz.wypozyczoneKsiazki:
                if k.indeksKsiazki == ksiazka.indeksKsiazki:
                    czytacz.wypozyczoneKsiazki.remove(k)
            db.aktualizuj_czytaczy(
                indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
            db.aktualizuj_biblioteke(ksiazka.indeksKsiazki, "W bibliotece")
            czyUdana = True
            op[3] = czyUdana
        except:
            print("Nie udało się oddać książki...")
        finally:
            db.aktualizuj_historie(his[0], his[1], his[2])

    def podejrzyjHistorieKsiazki(self):
        try:
            ksiazka = self.find_book_by_title_or_index()
            print(
                f"Ksiązka: {ksiazka.tytul} {ksiazka.autor} {ksiazka.rokWydania}")
            print(f"Status: {ksiazka.status}")
            print("Historia:")
            ct = 1
            for op in self.operacje:
                if (str(op[0]) == str(ksiazka.indeksKsiazki)):
                    ct += 1
                    print(
                        f"{ct}. Wyporzyczył: {op[1]} Udanie: { 'Tak' if op[2] else 'Nie'} Porzyczono: {op[3]} Oddano: {op[4]}")
        except:
            print("Nie udało się znaleźć książki...")

    def znajdzCzytacza(self, indeks) -> Czytacz:
        for cz in self.czytacze:
            if (cz.indeksCzytacza == (indeks-1)):
                return cz
        raise ValueError("Wybrano nie istniejącą opcję w menu")

    def find_book_by_title_or_index(self) -> Ksiazka:
        if self.iloscKsiazek < 1:
            raise ValueError("Nie ma książek w bibliotece")

        choice = int(u.czyscWejscie(input("""Chcesz znaleźć książkę po tytule czy indeksie?
            1) Tytuł
            2) Indeks
            """), trybTestowania=self.TEST_MODE))

        if choice == 1:
            title = u.czyscWejscie(
                input("Podaj tytuł książki: "), trybTestowania=self.TEST_MODE)
            for ksiazka in self.ksiazki:
                if ksiazka.tytul == title:
                    return ksiazka

        elif choice == 2:
            index = int(u.czyscWejscie(
                input("Podaj indeks książki: "), trybTestowania=self.TEST_MODE))
            if index > self.iloscKsiazek or index < 1:
                raise ValueError("Podano nieprawidłowy indeks")
            return self.ksiazki[index-1]

        else:
            raise ValueError("Wybrano nieprawidłową opcję w menu")
