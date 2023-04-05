import pytest
from datetime import date
import utils.utils as u


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


def test_str_to_date_valid_date():
    date_str = '2022-06-30'
    expected_date = date(2022, 6, 30)
    actual_date = u.str_to_date(date_str)
    assert actual_date == expected_date


def test_str_to_date_custom_format():
    date_str = '30-06-2022'
    expected_date = date(2022, 6, 30)
    actual_date = u.str_to_date(date_str, '%d-%m-%Y')
    assert actual_date == expected_date


def test_validate_date_input_valid_date():
    # Test with valid date in default format
    date_str = '2022-06-01'
    result = u.validate_date_input(date_str)
    assert isinstance(result, date)
    assert result == date(2022, 6, 1)

    # Test with valid date in custom format
    date_str = '01/06/2022'
    result = u.validate_date_input(date_str, '%d/%m/%Y')
    assert isinstance(result, date)
    assert result == date(2022, 6, 1)


def test_validate_date_input_invalid_format():
    # Test with invalid format
    date_str = '2022/06/01'
    with pytest.raises(ValueError):
        u.validate_date_input(date_str)


def test_cleanInput_noPolishChars():
    assert u.cleanInput("Hello world") == "Hello world"


def test_cleanInput_withPolishChars():
    assert u.cleanInput(
        "Bądź mi litościw, Boże mój") == "Badz mi litosciw, Boze moj"


def test_cleanInput_withTestMode():
    assert u.cleanInput("Dziękuję bardzo!",
                        testMode=True) == "Dziekuje bardzo!"
