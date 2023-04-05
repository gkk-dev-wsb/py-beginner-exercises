import os
import csv
from obj.KsiazkaObj import Ksiazka
from obj.CzytaczObj import Czytacz
import utils.utils as u
import utils.constants as c
import utils.db as db


class Biblioteka:
    def __init__(self) -> None:
        self.ksiazki: list[Ksiazka] = []
        self.czytacze: list[Czytacz] = []
        self.wypozyczoneKsiazki: list[Ksiazka] = []
        self.operacje: list[list] = []

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
        if os.path.join(c.DATA_DIR, f"biblioteka.csv"):
            with open(os.path.join(c.DATA_DIR, f"biblioteka.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # skip the header row
                for row in reader:
                    self.dodajKsiazke(row[1], row[2], row[3], row[4])
        if os.path.join(c.DATA_DIR, f"czytacze.csv"):
            with open(os.path.join(c.DATA_DIR, f"czytacze.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # skip the header row
                for row in reader:
                    self.dodajCzytacza(row[1], row[2])
        if os.path.join(c.DATA_DIR, f"historia.csv"):
            with open(os.path.join(c.DATA_DIR, f"historia.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # skip the header row
                for row in reader:
                    self.operacje.append(row)

    def dodajKsiazke(self, tytul=None, autor=None, rokWydania=None, status=None) -> None:
        try:
            readInput = False
            if (not tytul):
                tytul = input("Podaj tytuł: ")
                readInput = True
            if (not autor):
                autor = input("Podaj autora: ")
                readInput = True
            if (not rokWydania):
                rokWydania = u.validate_date_input(
                    input("Podaj rok wydania (w formacie YYYY): "), "%Y")
                if not rokWydania:
                    raise ValueError("Invalid date provided")
                readInput = True
            self.ksiazki.append(
                Ksiazka(tytul, autor, rokWydania, self.iloscKsiazek, status))
            if (readInput):
                status = "W bibliotece"
                db.logToFile(os.path.join(c.DATA_DIR, "biblioteka.csv"), [self.iloscKsiazek, tytul,
                                                                          autor, rokWydania, status])
        except:
            print("Nie udało się dodać książki...")

    def dodajCzytacza(self, imie=None, nazwisko=None) -> None:
        try:
            readinput = False
            if (not imie):
                imie = input("imię: ")
                readinput = True
            if (not nazwisko):
                nazwisko = input("nazwisko: ")
                readinput = True
            self.czytacze.append(Czytacz(self.iloscCzytaczy, imie, nazwisko))
            if (readinput):
                db.logToFile(os.path.join(c.DATA_DIR, "czytacze.csv"),
                             [self.iloscCzytaczy, imie, nazwisko, 0])
        except:
            print("Nie udało się dodać czytacza...")

    def wypozyczKsiazke(self):
        czyUdana = False
        op = ["", "", czyUdana, "", ""]
        try:
            ksiazka = self.znajdzPoTytuleLubIndeksie()
            ksiazka.status = "Nie w bibliotece"
            indeksCzytacza = int(input("numer czytacza: "))
            imie = input("imię: ")
            nazwisko = input("nazwisko: ")
            czytacz = self.znajdzCzytacza(indeksCzytacza)
            czytacz.wypozyczoneKsiazki.append(ksiazka)
            db.update_czytacze(
                indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
            db.update_biblioteka(ksiazka.indeksKsiazki, ksiazka.status)
            if not (czytacz.imie == imie and czytacz.nazwisko == nazwisko):
                raise ValueError("Nie znaleziono takiego czytacza.")
            dataWypozyczenia = u.validate_date_input(
                input("data wypozyczenia (w formacie yyyy-mm-dd): "))
            if not dataWypozyczenia:
                raise ValueError("Invalid date provided")
            op = [ksiazka.indeksKsiazki, indeksCzytacza,
                  czyUdana, dataWypozyczenia, 0]
            czyUdana = True
        except:
            print("Nie udało się wypożyczyć książki...")
        finally:
            self.operacje.append(op)
            db.logToFile(os.path.join(c.DATA_DIR, 'historia.csv'),
                         self.operacje[-1])

    def oddajKsiazke(self):
        czyUdana = False
        his = ["", "", czyUdana]
        try:
            ksiazka = self.znajdzPoTytuleLubIndeksie()
            his[0] = ksiazka.indeksKsiazki
            dataOddania = u.validate_date_input(
                input("Podaj datę oddania (w formacie yyyy-mm-dd): "))
            if not dataOddania:
                raise ValueError("Invalid date provided")
            his[1] = dataOddania
            indeksCzytacza = int(input("numer czytacza: "))
            for op in self.operacje:
                if (op[0] == str(ksiazka.indeksKsiazki) and op[1] == str(indeksCzytacza)):
                    if u.str_to_date(op[3]) > dataOddania:
                        raise ValueError(
                            "Nie można oddać książki przed datą wypożyczenia")
                    if (ksiazka.status[4] == "W bibliotece"):
                        raise ValueError("Książka już oddana")
                    op[4] = u.date_to_str(dataOddania)
            czytacz = self.znajdzCzytacza(indeksCzytacza)
            for k in czytacz.wypozyczoneKsiazki:
                if k.indeksKsiazki == ksiazka.indeksKsiazki:
                    czytacz.wypozyczoneKsiazki.remove(k)
            db.update_czytacze(
                indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
            db.update_biblioteka(ksiazka.indeksKsiazki, "W bibliotece")
            czyUdana = True
        except:
            print("Nie udało się oddać książki...")
        finally:
            db.update_historia(his[0], his[1], his[2])

    def podejrzyjHistorieKsiazki(self):
        try:
            ksiazka = self.znajdzPoTytuleLubIndeksie()
            print(
                f"Ksiązka: {ksiazka.tytul} {ksiazka.autor} {ksiazka.rokWydania}")
            print(f"Status: {ksiazka.status}")
            print("Historia:")
            ct = 1
            for op in self.operacje:
                if (op[0] == str(ksiazka.indeksKsiazki)):
                    ct += 1
                    print(
                        f"{ct}. Wporzyczył: {op[1]} Udanie: { 'Tak' if op[2] else 'Nie'} Wporzyczono: {op[3]} Oddano: {op[4]}")
        except:
            print("Nie udało się znaleźć książki...")

    def znajdzCzytacza(self, indeks) -> Czytacz:
        for cz in self.czytacze:
            if (cz.indeksCzytacza == (indeks-1)):
                return cz
        raise ValueError("Wybrano nie istniejącą opcję w menu")

    def znajdzPoTytuleLubIndeksie(self) -> Ksiazka:
        if (self.iloscKsiazek < 1):
            raise ValueError("Nie ma ksiazek w bibliotece")
        tytulCzyIndeks = int(input("""Chcesz znaleźć ksiązke po tytule czy indeksie?
            1) Tytuł
            2) Indeks
            """))
        if (tytulCzyIndeks == 1):
            tytul = input("Podaj tytul ksiazki: ")
            for ksiazka in self.ksiazki:
                if (ksiazka.tytul == tytul):
                    return ksiazka
        elif (tytulCzyIndeks == 2):
            indeks = int(input("Podaj indeks ksiazki: "))
            for ksiazka in self.ksiazki:
                if (ksiazka.indeksKsiazki == (indeks-1)):
                    return ksiazka
        else:
            raise ValueError("Wybrano nie istniejącą opcję w menu")
