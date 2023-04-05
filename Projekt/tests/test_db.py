import os
import sys

katalog_nadrzedny = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, katalog_nadrzedny)


import utils.db as db # pylint: disable=import-error
import utils.constants as c # pylint: disable=import-error


def test_inicjujDane():
    if os.path.exists(c.FOLDER_DANYCH):
        for nazwa_pliku in os.listdir(c.FOLDER_DANYCH):
            os.remove(os.path.join(c.FOLDER_DANYCH, nazwa_pliku))
        os.rmdir(c.FOLDER_DANYCH)
    db.inicjujDane()
    assert os.path.exists(c.FOLDER_DANYCH)
    for nazwa_pliku in ['historia.csv', 'biblioteka.csv', 'czytacze.csv']:
        sciezka_pliku = os.path.join(c.FOLDER_DANYCH, nazwa_pliku)
        assert os.path.exists(sciezka_pliku)
    oczekiwane_naglowki = [
        ["ID", 'Numer czytacza', "Czy udana", "Data wypozczenia", "Data oddania"],
        ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    ]
    for nazwa_pliku, oczekiwany_naglowek in zip(['historia.csv', 'biblioteka.csv', 'czytacze.csv'], oczekiwane_naglowki):
        naglowek, _ = db.odczytaj_dane_bez_naglowka(nazwa_pliku)
        assert naglowek == oczekiwany_naglowek


def test_zapiszDoPliku(tmp_path):
    """
        - Przetestuj zapisanie jednego wiersza do pliku
        - Przetestuj zapisywanie wielu wierszy do pliku
        - Utwórz plik tymczasowy do testowania
    """
    
    sciezka_pliku = os.path.join(tmp_path, "test_file.csv")
    dane = ["ID", "Name", "Age"]
    db.zapiszDoPliku(sciezka_pliku, dane)
    with open(sciezka_pliku, 'r') as f:
        kontent = f.read()
    assert kontent == "ID,Name,Age\n"

    dane2 = ["1", "John", "25"]
    dane3 = ["2", "Jane", "30"]
    db.zapiszDoPliku(sciezka_pliku, dane2)
    db.zapiszDoPliku(sciezka_pliku, dane3)
    with open(sciezka_pliku, 'r') as f:
        kontent = f.readlines()
    assert kontent == ["ID,Name,Age\n", "1,John,25\n", "2,Jane,30\n"]
