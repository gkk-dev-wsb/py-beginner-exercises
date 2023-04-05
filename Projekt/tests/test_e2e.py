import subprocess
import shutil
import os


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
