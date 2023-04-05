import os
import sys

# Add the parent directory to the sys.path list
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)


import utils.db as db # pylint: disable=import-error
import utils.constants as c # pylint: disable=import-error


def test_inicjujDane():
    if os.path.exists(c.FOLDER_DANYCH):
        for file_name in os.listdir(c.FOLDER_DANYCH):
            os.remove(os.path.join(c.FOLDER_DANYCH, file_name))
        os.rmdir(c.FOLDER_DANYCH)
    db.inicjujDane()
    assert os.path.exists(c.FOLDER_DANYCH)
    for file_name in ['historia.csv', 'biblioteka.csv', 'czytacze.csv']:
        file_path = os.path.join(c.FOLDER_DANYCH, file_name)
        assert os.path.exists(file_path)
    expected_headers = [
        ["ID", 'Numer czytacza', "Czy udana", "Data wypozczenia", "Data oddania"],
        ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    ]
    for file_name, expected_header in zip(['historia.csv', 'biblioteka.csv', 'czytacze.csv'], expected_headers):
        header, _ = db.odczytaj_dane_bez_naglowka(file_name)
        assert header == expected_header


def test_zapiszDoPliku(tmp_path):
    # Create a temporary file for testing
    file_path = os.path.join(tmp_path, "test_file.csv")

    # Test writing one row to the file
    data = ["ID", "Name", "Age"]
    db.zapiszDoPliku(file_path, data)
    with open(file_path, 'r') as f:
        contents = f.read()
    assert contents == "ID,Name,Age\n"

    # Test writing multiple rows to the file
    data2 = ["1", "John", "25"]
    data3 = ["2", "Jane", "30"]
    db.zapiszDoPliku(file_path, data2)
    db.zapiszDoPliku(file_path, data3)
    with open(file_path, 'r') as f:
        contents = f.readlines()
    assert contents == ["ID,Name,Age\n", "1,John,25\n", "2,Jane,30\n"]
