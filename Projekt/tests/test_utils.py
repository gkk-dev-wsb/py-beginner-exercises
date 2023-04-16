from datetime import date
import pytest
import sys
import os

katalog_nadrzedny = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, katalog_nadrzedny)

import utils.utils as u # pylint: disable=import-error


def test_date_to_str():
    objekt_daty = date(2023, 4, 7)
    lancuch_daty = u.date_to_str(objekt_daty)
    assert lancuch_daty == '2023-04-07'
    format_daty = '%d/%m/%Y'
    lancuch_daty = u.date_to_str(objekt_daty, format_daty)
    assert lancuch_daty == '07/04/2023'
    objekt_daty = date(2021, 1, 1)
    lancuch_daty = u.date_to_str(objekt_daty)
    assert lancuch_daty == '2021-01-01'

def test_waliduj_date_z_wejscia_valid_date():
    """
    - Test z prawidłową datą w formacie domyślnym
    - Test z prawidłową datą w niestandardowym formacie
    """
    lancuch_daty = '2022-06-01'
    rezultat = u.waliduj_date_z_wejscia(lancuch_daty)
    assert isinstance(rezultat, date)
    assert rezultat == date(2022, 6, 1)

    lancuch_daty = '01/06/2022'
    rezultat = u.waliduj_date_z_wejscia(lancuch_daty, '%d/%m/%Y')
    assert isinstance(rezultat, date)
    assert rezultat == date(2022, 6, 1)


def test_waliduj_date_z_wejscia_invalid_format():
    """Testuj z nieprawidłowym formatem"""

    lancuch_daty = '2022/06/01'
    with pytest.raises(ValueError):
        u.waliduj_date_z_wejscia(lancuch_daty)


def test_czyscWejscie_noPolishChars():
    assert u.czyscWejscie("Witaj Świecie!") == "Witaj Swiecie!"


def test_czyscWejscie_withPolishChars():
    assert u.czyscWejscie(
        "Bądź mi litościw, Boże mój") == "Badz mi litosciw, Boze moj"


def test_czyscWejscie_withTestMode():
    assert u.czyscWejscie("Dziękuję bardzo!",
                        trybTestowania=True) == "Dziekuje bardzo!"
