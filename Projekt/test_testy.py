import os
import sys
from datetime import date
import pytest
import shutil
import subprocess

katalog_nadrzedny = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, katalog_nadrzedny)

from main import *  # pylint: disable=import-error


def _usun_katalogi_pycache(directory):
    for korzen, katalogi, pliki in os.walk(directory):
        for katalog in katalogi:
            if katalog == '__pycache__':
                sciezka_katalogu = os.path.join(korzen, katalog)
                print(f'Removing directory {sciezka_katalogu}')
                try:
                    shutil.rmtree(sciezka_katalogu)
                except OSError as e:
                    print(f'Error deleting {sciezka_katalogu}: {e}')

def teardown():
    _usun_katalogi_pycache('.')
    shutil.rmtree("data")

def test_main():

    # Skonfiguruj dane testowe
    LANCUCH_TESTOWYCH_DANYCH_WEJSCIOWYCH = b'\n'

    # Dodaj książkę 1
    for i in [b'1\n', b'451 Stopni Fahrenheita\n', b'Ray Bradbury\n', b'1953\n']:
        LANCUCH_TESTOWYCH_DANYCH_WEJSCIOWYCH += i

    # Dodaj książkę 2
    for i in [b'1\n', b'Zmierzch\n', b'Stephenie Meyer\n', b'2005\n']:
        LANCUCH_TESTOWYCH_DANYCH_WEJSCIOWYCH += i

    # Dodaj czytaczy
    for cz in [[b'Janusz\n', b'Kowalski\n'], [b'Michal\n', b'Staszewski\n'],
               [b'Jadwiga\n', b'Mroczek\n'], [b'Paulina\n', b'Borsuk\n']]:
        for i in [b'5\n', cz[0], cz[1]]:
            LANCUCH_TESTOWYCH_DANYCH_WEJSCIOWYCH += i

    # Wypozycz ksiazke
    for i in [b'2\n', b'2\n', b'1\n', b'1\n', b'Janusz\n', b'Kowalski\n', b'2002-02-21\n',
              b'3\n', b'2\n', b'1\n', b'2002-02-22\n', b'1\n',
              b'2\n', b'1\n', b'451 Stopni Fahrenheita\n', b'2\n', b'Michal\n', b'Staszewski\n', b'2002-02-23\n',
              b'3\n', b'1\n', b'451 Stopni Fahrenheita\n', b'2005-02-23\n', b'2\n',
              b'2\n', b'2\n', b'1\n', b'3\n', b'\n', b'\n',  # Przypadek testowy, w którym dane czytacza (Imie, Nazwisko) są niepoprawne
              b'2\n', b'2\n', b'1\n', b'4\n', b'Paulina\n', b'Borsuk\n', b'2010-04-01\n']:
        LANCUCH_TESTOWYCH_DANYCH_WEJSCIOWYCH += i
    process = subprocess.Popen(['python3', 'main.py', 'test'],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        wyjscie, blad = process.communicate(
            input=LANCUCH_TESTOWYCH_DANYCH_WEJSCIOWYCH)
        print(wyjscie.decode('utf-8'))
    except Exception as e:
        print(f'Błąd: {e}')

def test_data_folder():
    katalog_danych = "data"
    pliki = ["biblioteka.csv", "czytacze.csv", "historia.csv"]

    for plik in pliki:
        assert os.path.isfile(os.path.join(katalog_danych, plik))

def test_biblioteka_csv():
    with open('data/biblioteka.csv', 'r') as f:
        kontent = f.read().strip()
    oczekiwany_kontent = """ID,Tytul,Autor,Rok wydania,Status
1,451 Stopni Fahrenheita,Ray Bradbury,1953-01-01,Nie w bibliotece
2,Zmierzch,Stephenie Meyer,2005-01-01,W bibliotece"""
    assert kontent == oczekiwany_kontent, f"Expected '{oczekiwany_kontent}', but got '{kontent}'"

def test_historia_csv():
    with open('data/historia.csv', 'r') as f:
        kontent = f.read().strip()
    oczekiwany_kontent = """ID,Numer czytacza,Czy udana,Data wypozczenia,Data oddania
0,1,False,2002-02-21,2002-02-22
0,2,False,2002-02-23,2005-02-23
0,3,False,,0
0,4,True,2010-04-01,0"""
    assert kontent == oczekiwany_kontent, f"Expected '{oczekiwany_kontent}', but got '{kontent}'"

def test_czytacze_csv():
    with open('data/czytacze.csv', 'r') as f:
        kontent = f.read().strip()
    oczekiwany_kontent = """Numer czytacza,Imie,Nazwisko,llosc ksiazek
1,Janusz,Kowalski,0
2,Michal,Staszewski,0
3,Jadwiga,Mroczek,0
4,Paulina,Borsuk,1"""
    assert kontent == oczekiwany_kontent, f"Expected '{oczekiwany_kontent}', but got '{kontent}'"

def test_Ksiazka_str():
    ksiazka = Ksiazka("Testowa Ksiazka", "Testowy Autor", 2022, 1, "Dostepna")
    result = str(ksiazka)
    assert result == "tytul: Testowa Ksiazkaautor: Testowy AutorrokWydania: 2022indeksKsiazki: 1status: Dostepna"

def test_Ksiazka_eq():
    ksiazka1 = Ksiazka("Testowa Ksiazka", "Testowy Autor", 2022, 1, "Dostepna")
    ksiazka2 = Ksiazka("Testowa Ksiazka", "Testowy Autor", 2022, 1, "Dostepna")
    ksiazka3 = Ksiazka("Inna Ksiazka", "Inny Autor", 2021, 2, "Wypozyczona")
    assert ksiazka1 == ksiazka2
    assert ksiazka1 != ksiazka3

def test_inicjujDane():
    if os.path.exists(FOLDER_DANYCH):
        for nazwa_pliku in os.listdir(FOLDER_DANYCH):
            os.remove(os.path.join(FOLDER_DANYCH, nazwa_pliku))
        os.rmdir(FOLDER_DANYCH)
    inicjujDane()
    assert os.path.exists(FOLDER_DANYCH)
    for nazwa_pliku in ['historia.csv', 'biblioteka.csv', 'czytacze.csv']:
        sciezka_pliku = os.path.join(FOLDER_DANYCH, nazwa_pliku)
        assert os.path.exists(sciezka_pliku)
    oczekiwane_naglowki = [
        ["ID", 'Numer czytacza', "Czy udana", "Data wypozczenia", "Data oddania"],
        ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    ]
    for nazwa_pliku, oczekiwany_naglowek in zip(['historia.csv', 'biblioteka.csv', 'czytacze.csv'], oczekiwane_naglowki):
        naglowek, _ = odczytaj_dane_bez_naglowka(nazwa_pliku)
        assert naglowek == oczekiwany_naglowek

def test_zapiszDoPliku(tmp_path):
    """
        - Przetestuj zapisanie jednego wiersza do pliku
        - Przetestuj zapisywanie wielu wierszy do pliku
        - Utwórz plik tymczasowy do testowania
    """
    
    sciezka_pliku = os.path.join(tmp_path, "test_file.csv")
    dane = ["ID", "Name", "Age"]
    zapiszDoPliku(sciezka_pliku, dane)
    with open(sciezka_pliku, 'r') as f:
        kontent = f.read()
    assert kontent == "ID,Name,Age\n"

    dane2 = ["1", "John", "25"]
    dane3 = ["2", "Jane", "30"]
    zapiszDoPliku(sciezka_pliku, dane2)
    zapiszDoPliku(sciezka_pliku, dane3)
    with open(sciezka_pliku, 'r') as f:
        kontent = f.readlines()
    assert kontent == ["ID,Name,Age\n", "1,John,25\n", "2,Jane,30\n"]

def test_date_to_str():
    objekt_daty = date(2023, 4, 7)
    lancuch_daty = date_to_str(objekt_daty)
    assert lancuch_daty == '2023-04-07'
    format_daty = '%d/%m/%Y'
    lancuch_daty = date_to_str(objekt_daty, format_daty)
    assert lancuch_daty == '07/04/2023'
    objekt_daty = date(2021, 1, 1)
    lancuch_daty = date_to_str(objekt_daty)
    assert lancuch_daty == '2021-01-01'

def test_waliduj_date_z_wejscia_valid_date():
    """
    - Test z prawidłową datą w formacie domyślnym
    - Test z prawidłową datą w niestandardowym formacie
    """
    lancuch_daty = '2022-06-01'
    rezultat = waliduj_date_z_wejscia(lancuch_daty)
    assert isinstance(rezultat, date)
    assert rezultat == date(2022, 6, 1)

    lancuch_daty = '01/06/2022'
    rezultat = waliduj_date_z_wejscia(lancuch_daty, '%d/%m/%Y')
    assert isinstance(rezultat, date)
    assert rezultat == date(2022, 6, 1)

def test_waliduj_date_z_wejscia_invalid_format():
    """Testuj z nieprawidłowym formatem"""

    lancuch_daty = '2022/06/01'
    with pytest.raises(ValueError):
        waliduj_date_z_wejscia(lancuch_daty)

def test_czyscWejscie_noPolishChars():
    assert czyscWejscie("Witaj Świecie!") == "Witaj Swiecie!"

def test_czyscWejscie_withPolishChars():
    assert czyscWejscie(
        "Bądź mi litościw, Boże mój") == "Badz mi litosciw, Boze moj"

def test_czyscWejscie_withTestMode():
    assert czyscWejscie("Dziękuję bardzo!",
                        trybTestowania=True) == "Dziekuje bardzo!"
