import os
import csv
import utils.constants as c
from pathlib import Path


def odczytaj_dane_bez_naglowka(nazwaPliku: str) -> tuple:
    """
    Czyta podany plik CSV i zwraca krotkę zawierającą nagłówek i wiersze.
    
    :param fileName: str, nazwa pliku do odczytu
    
    :return: tuple, zawierająca nagłówek i wiersze
    """
    with open(os.path.join(c.FOLDER_DANYCH, nazwaPliku), 'r', newline='') as csvfile:
        czytacz = csv.reader(csvfile)
        naglowek = next(czytacz)
        return naglowek, list(czytacz)


def zapisz_dane_bez_naglowka(nazwaPliku: str, naglowek: list, wiersze: list[list]) -> None:
    """
    Zapisuje podane wiersze do określonego pliku CSV z podanym nagłówkiem.

    :param nazwaPliku: str, nazwa pliku do zapisania
    :param naglowek: list, nagłówek do zapisania do pliku
    :param wiersze: list[list], wiersze do zapisania do pliku
    
    :return: None
    """
    with open(os.path.join(c.FOLDER_DANYCH, nazwaPliku), 'w', newline='') as csvfile:
        pisaz = csv.writer(csvfile)
        wiersze.insert(0, naglowek)
        pisaz.writerows(wiersze)


def inicjujDane() -> None:
    """
    Inicjalizuje dane poprzez utworzenie wymaganych plików CSV z ich odpowiednimi nagłówkami.

    :return: None
    """
    kolumnyPlikow = {
        "historia": ["ID", 'Numer czytacza',
                     "Czy udana", "Data wypozczenia", "Data oddania"],
        "biblioteka": ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        "czytacze": ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    }
    if not os.path.exists(c.FOLDER_DANYCH):
        os.mkdir(c.FOLDER_DANYCH)

    for plik, kolumny in kolumnyPlikow.items():
        sciezka = os.path.join(c.FOLDER_DANYCH, f"{plik}.csv")
        if not os.path.exists(sciezka):
            open(sciezka, 'w').close()
            zapiszDoPliku(sciezka, kolumny)


def zapiszDoPliku(sciezka: Path, dane: list) -> None:
    """
    Zapisuje podane dane do określonego pliku.
    :param sciezka: str, ścieżka pliku, do którego mają zostać zapisane dane
    :param dane: list, dane do zapisania do pliku
    :return: None
    """
    with open(sciezka, 'a') as f:
        pisaz = csv.writer(f)
        pisaz.writerow(dane)


def aktualizuj_czytaczy(numerCzytacza: int, iloscksiazek: int) -> None:
    """
    Aktualizuje wartość pola 'ilość książek' dla podanego 'numerCzytacza' w
    pliku CSV.
    
    :param numerCzytacza: int, numer czytelnika do zaktualizowania
    :param iloscksiazek: int, nowa wartość pola 'ilość książek'
    
    :return: None
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
    
    :param id_ksiazki: int, identyfikator książki
    :param data_oddania: int, nowa wartość pola 'Data oddania'
    :param czyUdana: bool, flaga informująca o powodzeniu operacji
    
    :return: None
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

    Parameters:
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
