import csv
import os
import sys
from pathlib import Path
from datetime import date, datetime


ASCII_MENU = """
    === BIBLIOTEKA ===
1) Dodaj ksiązke
2) Wypozycz ksiazke
3) Oddaj ksiazke
4) Sprawdz historie ksiazki
5) Dodaj czytelnika
6) Wyjdź
"""

FOLDER_DANYCH = os.path.join(os.curdir, 'data')

from dataclasses import dataclass


@dataclass
class Ksiazka:
    tytul: str
    autor: str
    rokWydania: int
    indeksKsiazki: int
    status: str

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


def odczytaj_dane_bez_naglowka(nazwaPliku: str) -> tuple:
    """
    Czyta podany plik CSV i zwraca krotkę zawierającą nagłówek i wiersze.
    
    Args:
    fileName: str, nazwa pliku do odczytu
    
    Returns:
    tuple, zawierająca nagłówek i wiersze
    """
    with open(os.path.join(FOLDER_DANYCH, nazwaPliku), 'r', newline='') as csvfile:
        czytacz = csv.reader(csvfile)
        naglowek = next(czytacz)
        return naglowek, list(czytacz)


def zapisz_dane_bez_naglowka(nazwaPliku: str, naglowek: list, wiersze: list[list]) -> None:
    """
    Zapisuje podane wiersze do określonego pliku CSV z podanym nagłówkiem.

    Args:
    nazwaPliku: str, nazwa pliku do zapisania
    naglowek: list, nagłówek do zapisania do pliku
    wiersze: list[list], wiersze do zapisania do pliku
    
    Returns:
    None
    """
    with open(os.path.join(FOLDER_DANYCH, nazwaPliku), 'w', newline='') as csvfile:
        pisaz = csv.writer(csvfile)
        wiersze.insert(0, naglowek)
        pisaz.writerows(wiersze)


def inicjujDane() -> None:
    """
    Inicjalizuje dane poprzez utworzenie wymaganych plików CSV z ich
    odpowiednimi nagłówkami.

    Returns:
    None
    """
    kolumnyPlikow = {
        "historia": ["ID", 'Numer czytacza',
                     "Czy udana", "Data wypozczenia", "Data oddania"],
        "biblioteka": ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        "czytacze": ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    }
    if not os.path.exists(FOLDER_DANYCH):
        os.mkdir(FOLDER_DANYCH)

    for plik, kolumny in kolumnyPlikow.items():
        sciezka = os.path.join(FOLDER_DANYCH, f"{plik}.csv")
        if not os.path.exists(sciezka):
            open(sciezka, 'w').close()
            zapiszDoPliku(sciezka, kolumny)


def zapiszDoPliku(sciezka: Path, dane: list) -> None:
    """
    Zapisuje podane dane do określonego pliku.
    
    Args:
    sciezka: str, ścieżka pliku, do którego mają zostać zapisane dane
    dane: list, dane do zapisania do pliku
    
    Returns:
    None
    """
    with open(sciezka, 'a') as f:
        pisaz = csv.writer(f)
        pisaz.writerow(dane)


def aktualizuj_czytaczy(numerCzytacza: int, iloscksiazek: int) -> None:
    """
    Aktualizuje wartość pola 'ilość książek' dla podanego 'numerCzytacza' w
    pliku CSV.
    
    Args:
    numerCzytacza: int, numer czytelnika do zaktualizowania
    iloscksiazek: int, nowa wartość pola 'ilość książek'
    
    Returns:
    None
    """
    naglowek, wiersze = odczytaj_dane_bez_naglowka('czytacze.csv')
    for wiersz in wiersze:
        if int(wiersz[0]) == numerCzytacza:
            wiersz[3] = str(iloscksiazek)
            break
    zapisz_dane_bez_naglowka('czytacze.csv', naglowek, wiersze)


def aktualizuj_historie(id_ksiazki: int, data_oddania: int, czyUdana: bool) -> None:
    """
    Aktualizuje wartość pola 'Data oddania' dla danej książki o identyfikatorze
    'id_ksiazki' w pliku CSV.
    
    Args:
    id_ksiazki: int, identyfikator książki
    data_oddania: int, nowa wartość pola 'Data oddania'
    czyUdana: bool, flaga informująca o powodzeniu operacji
    
    Returns:
    None
    """
    naglowek, wiersze = odczytaj_dane_bez_naglowka('historia.csv')
    for wiersz in wiersze:
        if wiersz[0] == str(id_ksiazki) and str(wiersz[4]) == '0':
            wiersz[4] = str(data_oddania)
            wiersz[2] = str(czyUdana)
    zapisz_dane_bez_naglowka('historia.csv', naglowek, wiersze)


def aktualizuj_biblioteke(id: int, status: str) -> None:
    """
    Aktualizuje pole 'Status' książki o podanym 'id' w pliku 'biblioteka.csv'.

    Args:
    id (int): ID książki do zaktualizowania (indeksowane od 0).
    status (str): Nowy status książki.

    Returns:
    None
    """
    naglowek, wiersze = odczytaj_dane_bez_naglowka('biblioteka.csv')
    for wiersz in wiersze:
        if int(wiersz[0]) == id+1:
            wiersz[4] = str(status)
            break
    zapisz_dane_bez_naglowka('biblioteka.csv', naglowek, wiersze)

def date_to_str(objekt_daty: date, date_format='%Y-%m-%d'):
    """
    Konwertuje obiekt datetime.date na string.
    
    Args:
    data_obj: obiekt datetime.date
    format_daty: str, format zwracanej daty
    
    Returns:
    str, data w formacie string
    """
    return datetime.strftime(objekt_daty, date_format)

def waliduj_date_z_wejscia(lancuch_daty, format_daty='%Y-%m-%d'):
    """
    Waliduje i zwraca string z datą z wejścia użytkownika, konwertując ją na
    obiekt daty.
    
    Args:
    lancuch_daty: str, string daty wprowadzony przez użytkownika
    format_daty: str, format, w jakim funkcja odczytuje datę
    
    Returns:
    obiekt datetime.date, jeśli dane wejściowe są poprawne, w przeciwnym razie None
    """
    return datetime.strptime(lancuch_daty, format_daty).date()

def czyscWejscie(wejscie:str, trybTestowania=False):
    """
    Funkcja czyszczenia łańcucha znaków przez zastępowanie polskich znaków ich
    odpowiednikami łacińskimi przy użyciu metod str.maketrans() i str.translate().

    Args:
    wejscie (str): Łańcuch znaków do wyczyszczenia.
    trybTestowania (bool, opcjonalnie): Jeśli ustawione na True, drukuje łańcuch
    wejściowy przed i po wyczyszczeniu. Domyślnie False.

    Returns:
    str: Wyczyszczony łańcuch znaków, w którym wszystkie polskie znaki zostały
    zastąpione przez ich odpowiedniki łacińskie.
"""

    polskie_na_lacinskie = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
    wyjscie = wejscie.translate(polskie_na_lacinskie)
    if trybTestowania:
        print("$: ", wejscie)
    return wyjscie


TEST_MODE = False

def sprawdzCzyTrybTestowy():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            TEST_MODE = True
            print("Uruchomiono w trybie testowym...")

import csv
import os

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
    
    def ladujBiblioteke(self) -> None:
        """
        Metoda wczytuje dane z plików CSV i dodaje je do biblioteki.
        Wczytywane pliki to biblioteka.csv, czytacze.csv i historia.csv.

        Returns:
        None
        """
        if os.path.join(FOLDER_DANYCH, f"biblioteka.csv"):
            with open(os.path.join(FOLDER_DANYCH, f"biblioteka.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.dodajKsiazke(row[1], row[2], row[3], row[4])
        if os.path.join(FOLDER_DANYCH, f"czytacze.csv"):
            with open(os.path.join(FOLDER_DANYCH, f"czytacze.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.dodajCzytacza(row[1], row[2])
        if os.path.join(FOLDER_DANYCH, f"historia.csv"):
            with open(os.path.join(FOLDER_DANYCH, f"historia.csv"), newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.operacje.append(row)

    def dodajKsiazke(self, tytul=None, autor=None, rokWydania=None, status=None) -> None:
        """
        Funkcja dodajKsiazke dodaje nową książkę do listy książek biblioteki.
        Jeśli brakuje informacji o tytule, autorze lub roku wydania, funkcja
        prosi użytkownika o wprowadzenie odpowiedniej informacji. Funkcja
        waliduje również rok wydania, sprawdzając, czy ma poprawny format.
        Po dodaniu książki do listy, funkcja również loguje informacje o dodanej
        książce do pliku biblioteki.

        Args:
        tytul: str (opcjonalny) - tytuł książki
        autor: str (opcjonalny) - autor książki
        rokWydania: str (opcjonalny) - rok wydania książki w formacie "YYYY"
        status: str (opcjonalny) - status książki
        
        Returns:
        None
        """
        try:
            readInput = False
            if (not tytul):
                tytul = czyscWejscie(input("Podaj tytuł: "),
                                     trybTestowania=self.TEST_MODE)
                readInput = True
            if (not autor):
                autor = czyscWejscie(
                    input("Podaj autora: "), trybTestowania=self.TEST_MODE)
                readInput = True
            if (not rokWydania):
                rokWydania = waliduj_date_z_wejscia(czyscWejscie(
                    input("Podaj rok wydania (w formacie YYYY): "), trybTestowania=self.TEST_MODE), "%Y")
                if not rokWydania:
                    raise ValueError("Invalid date provided")
                readInput = True
            self.ksiazki.append(
                Ksiazka(tytul, autor, rokWydania, self.iloscKsiazek, status))
            if (readInput):
                status = "W bibliotece"
                zapiszDoPliku(os.path.join(FOLDER_DANYCH, "biblioteka.csv"), [self.iloscKsiazek, tytul,
                                                                          autor, rokWydania, status])
        except:
            print("Nie udało się dodać książki...")

    def dodajCzytacza(self, imie=None, nazwisko=None) -> None:
        """
        Args:
        imie (str, optional): Imię czytacza. Jeśli nie podano, zostanie zapytane
        o nie użytkownika.
        nazwisko (str, optional): Nazwisko czytacza. Jeśli nie podano, zostanie
        zapytane o nie użytkownika.

        Returns:
        None
        """
        try:
            readinput = False
            if (not imie):
                imie = czyscWejscie(input("imię: "), trybTestowania=self.TEST_MODE)
                readinput = True
            if (not nazwisko):
                nazwisko = czyscWejscie(
                    input("nazwisko: "), trybTestowania=self.TEST_MODE)
                readinput = True
            self.czytacze.append(Czytacz(self.iloscCzytaczy, imie, nazwisko))
            if (readinput):
                zapiszDoPliku(os.path.join(FOLDER_DANYCH, "czytacze.csv"),
                             [self.iloscCzytaczy, imie, nazwisko, 0])
        except:
            print("Nie udało się dodać czytacza...")

    def wypozyczKsiazke(self) -> None:
        """
        Metoda służąca do wypożyczania książki przez czytelnika. Wypożycza
        książkę, którą znajduje po tytule lub indeksie i aktualizuje dane w
        bazie danych.

        Returns:
        None
        """
        try:
            ksiazka = self.znajdz_ksiazke_wedlug_tytulu_lub_indeksu()
            ksiazka.status = "Nie w bibliotece"
            indeksCzytacza = int(czyscWejscie(
                input("numer czytacza: "), trybTestowania=self.TEST_MODE))
            imie = czyscWejscie(input("imię: "), trybTestowania=self.TEST_MODE)
            nazwisko = czyscWejscie(
                input("nazwisko: "), trybTestowania=self.TEST_MODE)
            czytacz = self.znajdzCzytacza(indeksCzytacza)
            if not (czytacz.imie == imie and czytacz.nazwisko == nazwisko):
                raise ValueError("Nie znaleziono takiego czytacza.")
            dataWypozyczenia = waliduj_date_z_wejscia(
                czyscWejscie(input("data wypozyczenia (w formacie yyyy-mm-dd): "), trybTestowania=self.TEST_MODE))
            if not dataWypozyczenia:
                raise ValueError("Invalid date provided")
            czyUdana = True
            czytacz.wypozyczoneKsiazki.append(ksiazka)
            aktualizuj_czytaczy(
                indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
            aktualizuj_biblioteke(ksiazka.indeksKsiazki, ksiazka.status)
            op = [ksiazka.indeksKsiazki, indeksCzytacza,
                czyUdana, dataWypozyczenia, 0]
            self.operacje.append(op)
            zapiszDoPliku(os.path.join(FOLDER_DANYCH, 'historia.csv'),
                        self.operacje[-1])
        except Exception as e:
            data = [ksiazka.indeksKsiazki if 'ksiazka' in locals() else '',
                    indeksCzytacza if 'indeksCzytacza' in locals() else '',
                    False, dataWypozyczenia if 'dataWypozyczenia' in locals() else '',
                    0]
            self.operacje.append(data)
            zapiszDoPliku(os.path.join(FOLDER_DANYCH, 'historia.csv'),
                        self.operacje[-1])
            print("Nie udało się wypożyczyć książki...", e)

    def oddajKsiazke(self) -> None:
        """
        Umożliwia użytkownikowi zwrot książki do biblioteki, aktualizuje status
        książki, historię czytelnika i plik biblioteczny.

        Returns:
        None
        """
        czyUdana = False
        his = ["", "", czyUdana]
        try:
            ksiazka = self.znajdz_ksiazke_wedlug_tytulu_lub_indeksu()
            his[0] = ksiazka.indeksKsiazki
            dataOddania = waliduj_date_z_wejscia(
                czyscWejscie(input("Podaj datę oddania (w formacie yyyy-mm-dd): "), trybTestowania=self.TEST_MODE))
            if not dataOddania:
                raise ValueError("Invalid date provided")
            his[1] = dataOddania
            indeksCzytacza = int(czyscWejscie(
                input("numer czytacza: "), trybTestowania=self.TEST_MODE))
            for op in self.operacje:
                if (op[0] == str(ksiazka.indeksKsiazki) and op[1] == str(indeksCzytacza)):
                    if waliduj_date_z_wejscia(op[3]) > dataOddania:
                        raise ValueError(
                            "Nie można oddać książki przed datą wypożyczenia")
                    if (ksiazka.status[4] == "W bibliotece"):
                        raise ValueError("Książka już oddana")
                    op[4] = date_to_str(dataOddania)
            czytacz = self.znajdzCzytacza(indeksCzytacza)
            for k in czytacz.wypozyczoneKsiazki:
                if k.indeksKsiazki == ksiazka.indeksKsiazki:
                    czytacz.wypozyczoneKsiazki.remove(k)
            aktualizuj_czytaczy(
                indeksCzytacza, czytacz.iloscWypozyczonychKsiazek)
            aktualizuj_biblioteke(ksiazka.indeksKsiazki, "W bibliotece")
            czyUdana = True
            op[3] = czyUdana
        except:
            print("Nie udało się oddać książki...")
        finally:
            aktualizuj_historie(his[0], his[1], his[2])

    def podejrzyjHistorieKsiazki(self) -> None:
        """
        Wyświetla historię wypożyczeń książki.
        
        Returns:
        None
        """
        try:
            ksiazka = self.znajdz_ksiazke_wedlug_tytulu_lub_indeksu()
            print(
                f"Ksiązka: {ksiazka.tytul} {ksiazka.autor} {ksiazka.rokWydania}")
            print(f"Status: {ksiazka.status}")
            print("Historia:")
            licznik = 1
            for op in self.operacje:
                if (str(op[0]) == str(ksiazka.indeksKsiazki)):
                    licznik += 1
                    print(
                        f"{licznik}. Wyporzyczył: {op[1]} Udanie: { 'Tak' if op[2] else 'Nie'} Porzyczono: {op[3]} Oddano: {op[4]}")
        except:
            print("Nie udało się znaleźć książki...")

    def znajdzCzytacza(self, indeks) -> Czytacz:
        """
        Funkcja znajduje obiekt klasy `Czytacz` o podanym indeksie i zwraca go.
        Jeśli nie ma takiego czytacza w liście `czytacze`, funkcja rzuca błąd
        ValueError.

        Args:
        indeks (int): Indeks czytacza.

        Returns:
        Czytacz: Obiekt klasy `Czytacz` o podanym indeksie.
        """
        for cz in self.czytacze:
            if (cz.indeksCzytacza == (indeks-1)):
                return cz
        raise ValueError("Wybrano nie istniejącą opcję w menu")

    def znajdz_ksiazke_wedlug_tytulu_lub_indeksu(self) -> Ksiazka:
        """
        Funkcja zwraca obiekt klasy Ksiazka wyszukany w bibliotece na podstawie
        tytułu lub indeksu. Użytkownik wybiera sposób wyszukania, a funkcja
        zwraca obiekt klasy Ksiazka o podanym tytule lub indeksie. Może rzucać
        wyjątek ValueError w przypadku błędnych danych wejściowych.
        
        Returns:
        Obiekt klasy Ksiazka.
        """
        if self.iloscKsiazek < 1:
            raise ValueError("Nie ma książek w bibliotece")

        choice = int(czyscWejscie(input("""Chcesz znaleźć książkę po tytule czy indeksie?
            1) Tytuł
            2) Indeks
            """), trybTestowania=self.TEST_MODE))

        if choice == 1:
            title = czyscWejscie(
                input("Podaj tytuł książki: "), trybTestowania=self.TEST_MODE)
            for ksiazka in self.ksiazki:
                if ksiazka.tytul == title:
                    return ksiazka

        elif choice == 2:
            index = int(czyscWejscie(
                input("Podaj indeks książki: "), trybTestowania=self.TEST_MODE))
            if index > self.iloscKsiazek or index < 1:
                raise ValueError("Podano nieprawidłowy indeks")
            return self.ksiazki[index-1]

        else:
            raise ValueError("Wybrano nieprawidłową opcję w menu")

if __name__ == "__main__":
    sprawdzCzyTrybTestowy()
    inicjujDane()
    biblioteka = Biblioteka(TEST_MODE)
    biblioteka.ladujBiblioteke()
    while True:
        menuWybor = czyscWejscie(input(ASCII_MENU), trybTestowania=TEST_MODE)
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
            print("Wybrano nie istniejącą opcję w menu...")
    SystemExit(0)
