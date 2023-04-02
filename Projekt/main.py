import csv
import os
from datetime import datetime

ASCII_MENU = """
    === BIBLIOTEKA ===
1) Dodaj ksiązke
2) Wypozycz ksiazke
3) Oddaj ksiazke
4) Sprawdz historie ksiazki
5) Dodaj czytelnika
6) Wyjdź
"""
DATA_DIR = os.path.join(os.curdir, 'data')


def validate_date_input(date_string, date_format='%Y-%m-%d'):
    """
    Validates and returns converted to date object string from user input.
    :param date_string: str, user input date string
    :param date_format: str, format in which function reads date
    :return: datetime.date object if input is valid, None otherwise
    """
    try:
        date_obj = datetime.strptime(date_string, date_format).date()
        return date_obj
    except ValueError:
        return None


def inicjujDane():
    kolumnyPlikow = {
        "historia": ["ID", 'Numer czytacza',
                     "Czy udana", "Data wypozczenia", "Data oddania"],
        "biblioteka": ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        "czytacze": ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    }
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    for plik, kolumny in kolumnyPlikow.items():
        sciezka = os.path.join(DATA_DIR, f"{plik}.csv")
        if not os.path.exists(sciezka):
            open(sciezka, 'w').close()
            logToFile(sciezka, kolumny)


def logToFile(path, data):
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def update_czytacze(numerCzytacza, iloscksiazek):
    """
    Updates the value of 'ilosc ksiazek' for a given 'numerCzytacza' in a CSV file.
    :param numerCzytacza: int, the reader number to update
    :param iloscksiazek: int, the new value of 'ilosc ksiazek'
    :return: None
    """
    with open(os.path.join(DATA_DIR, 'czytacze.csv'), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)

    for row in rows:
        if int(row[0]) == numerCzytacza:
            row[3] = str(iloscksiazek)
            break

    with open(os.path.join(DATA_DIR, 'czytacze.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows.insert(0, header)
        writer.writerows(rows)


def update_biblioteka(id, status):
    with open(os.path.join(DATA_DIR, 'biblioteka.csv'), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)

    for row in rows:
        if int(row[0]) == id+1:
            row[4] = str(status)
            break

    with open(os.path.join(DATA_DIR, 'biblioteka.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows.insert(0, header)
        writer.writerows(rows)


class Ksiazka:
    def __init__(self, tytul, autor, rokWydania, indeksKsiazki, status) -> None:
        self.tytul: str = tytul
        self.autor: str = autor
        self.rokWydania: int = rokWydania
        self.indeksKsiazki: int = indeksKsiazki
        self.status: str = status

    def __str__(self):
        return (f"tytul: {self.tytul}"
                f"autor: {self.autor}"
                f"rokWydania: {self.rokWydania}"
                f"indeksKsiazki: {self.indeksKsiazki}"
                f"status: {self.status}")


class Czytacz:
    def __init__(self, indeksCzytacza: int, imie: str, nazwisko: str) -> None:
        self.indeksCzytacza: int = indeksCzytacza
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.wypozyczoneKsiazki: list[Ksiazka] = []

    @property
    def iloscWypozyczonychKsiazek(self):
        return len(self.wypozyczoneKsiazki)

    def __str__(self):
        return (f"indeksCzytacza: {self.indeksCzytacza}"
                f"imie: {self.imie}"
                f"nazwisko: {self.nazwisko}"
                f"wypozyczoneKsiazki: {self.wypozyczoneKsiazki}")


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
    def iloscOperacji(self):
        return len(self.operacje)

    @property
    def iloscKsiazek(self):
        return len(self.ksiazki)

    @property
    def iloscCzytaczy(self):
        return len(self.czytacze)

    def ladujBiblioteke(self):
        if os.path.join(DATA_DIR, f"biblioteka.csv"):
            with open(os.path.join(DATA_DIR, f"biblioteka.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # skip the header row
                for row in reader:
                    print(row)
                    self.dodajKsiazke(row[1], row[2], row[3], row[4])
        if os.path.join(DATA_DIR, f"czytacze.csv"):
            with open(os.path.join(DATA_DIR, f"czytacze.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # skip the header row
                for row in reader:
                    print(row)
                    self.dodajCzytacza(row[1], row[2])

    def dodajKsiazke(self, tytul=None, autor=None, rokWydania=None, status=None) -> None:
        readInput = False
        if (not tytul):
            tytul = input("Podaj tytuł: ")
            readInput = True
        if (not autor):
            autor = input("Podaj autora: ")
            readInput = True
        if (not rokWydania):
            rokWydania = validate_date_input(
                input("Podaj rok wydania (w formacie YYYY): "), "%Y")
            if not rokWydania:
                raise ValueError("Invalid date provided")
            readInput = True
        self.ksiazki.append(
            Ksiazka(tytul, autor, rokWydania, self.iloscKsiazek, status))
        if (readInput):
            status = "W bibliotece"
            logToFile(os.path.join(DATA_DIR, "biblioteka.csv"), [self.iloscKsiazek, tytul,
                                                                 autor, rokWydania, status])

    def dodajCzytacza(self, imie=None, nazwisko=None) -> None:
        readinput = False
        if (not imie):
            imie = input("imię: ")
            readinput = True
        if (not nazwisko):
            nazwisko = input("nazwisko: ")
            readinput = True
        self.czytacze.append(Czytacz(self.iloscCzytaczy, imie, nazwisko))
        if (readinput):
            logToFile(os.path.join(DATA_DIR, "czytacze.csv"),
                      [self.iloscCzytaczy, imie, nazwisko, 0])

    def wypozyczKsiazke(self):
        czyUdana = False
        ksiazka = self.znajdzPoTytuleLubIndeksie()
        ksiazka.status = "Nie w bibliotece"
        indeksCzytacza = int(input("numer czytacza: "))
        imie = input("imię: ")
        nazwisko = input("nazwisko: ")
        czytacz = self.znajdzCzytacza(indeksCzytacza)
        czytacz.wypozyczoneKsiazki.append(ksiazka)
        update_czytacze(indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
        update_biblioteka(ksiazka.indeksKsiazki, ksiazka.status)
        if not (czytacz.imie == imie and czytacz.nazwisko == nazwisko):
            raise ValueError("Nie znaleziono takiego czytacza.")
        dataWypozyczenia = validate_date_input(
            input("data wypozyczenia (w formacie yyyy-mm-dd): "))
        if not dataWypozyczenia:
            raise ValueError("Invalid date provided")
        self.operacje.append([ksiazka.indeksKsiazki,
                             indeksCzytacza, czyUdana, dataWypozyczenia])
        logToFile(os.path.join(DATA_DIR, 'historia.csv'), self.operacje[-1])

    def oddajKsiazke(self):
        self.znajdzPoTytuleLubIndeksie()
        dataOddania = validate_date_input(
            input("Podaj datę oddania (w formacie yyyy-mm-dd): "))
        if not dataOddania:  # or dataOddania < dataWypozyczenia
            raise ValueError("Invalid date provided")

    def podejrzyjHistorieKsiazki(self):
        self.znajdzPoTytuleLubIndeksie()

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


if __name__ == "__main__":
    inicjujDane()
    biblioteka = Biblioteka()
    biblioteka.ladujBiblioteke()
    while True:
        print(biblioteka)
        menuWybor = input(ASCII_MENU)
        if (menuWybor == '1'):
            biblioteka.dodajKsiazke()
        elif (menuWybor == '2'):
            biblioteka.wypozyczKsiazke()
        elif (menuWybor == '3'):
            biblioteka.oddajKsiazke()
        elif (menuWybor == '4'):
            biblioteka.podejrzyjHistorieKsiazki()
        elif (menuWybor == '5'):
            biblioteka.dodajCzytacza()
        elif (menuWybor == '6'):
            print(f"Zamykanie programu...")
            break
        else:
            print("Wybrano nie istniejącą opcję w menu")
    SystemExit(0)
