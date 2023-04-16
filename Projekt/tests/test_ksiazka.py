import sys
import os

katalog_nadrzedny = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, katalog_nadrzedny)

from obj.objektyDanych import Ksiazka # pylint: disable=import-error


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