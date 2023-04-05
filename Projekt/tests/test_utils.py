from datetime import date
import pytest
import sys
import os

# Add the parent directory to the sys.path list
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

import utils.utils as u # pylint: disable=import-error


def test_date_to_str():
    date_obj = date(2023, 4, 7)
    date_str = u.date_to_str(date_obj)
    assert date_str == '2023-04-07'
    date_format = '%d/%m/%Y'
    date_str = u.date_to_str(date_obj, date_format)
    assert date_str == '07/04/2023'
    date_obj = date(2021, 1, 1)
    date_str = u.date_to_str(date_obj)
    assert date_str == '2021-01-01'

def test_waliduj_date_z_wejscia_valid_date():
    # Test with valid date in default format
    date_str = '2022-06-01'
    result = u.waliduj_date_z_wejscia(date_str)
    assert isinstance(result, date)
    assert result == date(2022, 6, 1)

    # Test with valid date in custom format
    date_str = '01/06/2022'
    result = u.waliduj_date_z_wejscia(date_str, '%d/%m/%Y')
    assert isinstance(result, date)
    assert result == date(2022, 6, 1)


def test_waliduj_date_z_wejscia_invalid_format():
    # Test with invalid format
    date_str = '2022/06/01'
    with pytest.raises(ValueError):
        u.waliduj_date_z_wejscia(date_str)


def test_czyscWejscie_noPolishChars():
    assert u.czyscWejscie("Witaj Świecie!") == "Witaj Swiecie!"


def test_czyscWejscie_withPolishChars():
    assert u.czyscWejscie(
        "Bądź mi litościw, Boże mój") == "Badz mi litosciw, Boze moj"


def test_czyscWejscie_withTestMode():
    assert u.czyscWejscie("Dziękuję bardzo!",
                        trybTestowania=True) == "Dziekuje bardzo!"
