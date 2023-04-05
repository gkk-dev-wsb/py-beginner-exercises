import os
import csv
import utils.constants as c
from pathlib import Path


def readDataSkippingHeader(fileName: str) -> tuple:
    """
    Reads the given CSV file and returns a tuple containing the header and rows.
    :param fileName: str, the name of the file to read
    :return: tuple, containing header and rows
    """
    with open(os.path.join(c.DATA_DIR, fileName), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        return header, list(reader)


def writeDataSkippingHeader(fileName: str, header: list, rows: list[list]) -> None:
    """
    Writes the given rows to the specified CSV file with the specified header.
    :param fileName: str, the name of the file to write
    :param header: list, the header to write to the file
    :param rows: list[list], the rows to write to the file
    :return: None
    """
    with open(os.path.join(c.DATA_DIR, fileName), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows.insert(0, header)
        writer.writerows(rows)


def inicjujDane() -> None:
    """
    Initializes data by creating required CSV files with their respective headers.
    :return: None
    """
    kolumnyPlikow = {
        "historia": ["ID", 'Numer czytacza',
                     "Czy udana", "Data wypozczenia", "Data oddania"],
        "biblioteka": ["ID", "Tytul", "Autor", "Rok wydania", "Status"],
        "czytacze": ["Numer czytacza", "Imie", "Nazwisko", "llosc ksiazek"]
    }
    if not os.path.exists(c.DATA_DIR):
        os.mkdir(c.DATA_DIR)

    for plik, kolumny in kolumnyPlikow.items():
        sciezka = os.path.join(c.DATA_DIR, f"{plik}.csv")
        if not os.path.exists(sciezka):
            open(sciezka, 'w').close()
            logToFile(sciezka, kolumny)


def logToFile(path: Path, data: list) -> None:
    """
    Logs the given data to the specified file.
    :param path: str, the path of the file to log data to
    :param data: list, the data to log to the file
    :return: None
    """
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def update_czytacze(numerCzytacza: int, iloscksiazek: int) -> None:
    """
    Updates the value of 'ilosc ksiazek' for a given 'numerCzytacza' in a CSV file.
    :param numerCzytacza: int, the reader number to update
    :param iloscksiazek: int, the new value of 'ilosc ksiazek'
    :return: None
    """
    header, rows = readDataSkippingHeader('czytacze.csv')
    for row in rows:
        if int(row[0]) == numerCzytacza:
            row[3] = str(iloscksiazek)
            break
    writeDataSkippingHeader('czytacze.csv', header, rows)


def update_historia(id_ksiazki: int, data_oddania: int, czyUdana: bool) -> None:
    """
    Updates the value of 'Data oddania' for a given 'id_ksiazki' in a CSV file.
    :param id_ksiazki: int, target book ID
    :param data_oddania: int, the new value of 'Data oddania'
    :param czyUdana: bool, flag if operation was successful
    :return: None
    """
    header, rows = readDataSkippingHeader('historia.csv')
    for row in rows:
        if row[0] == str(id_ksiazki) and str(row[4]) == '0':
            row[4] = str(data_oddania)
            row[2] = str(czyUdana)
    writeDataSkippingHeader('historia.csv', header, rows)


def update_biblioteka(id: int, status: str) -> None:
    """
    Update the 'Status' field for a book in the 'biblioteka.csv' file with the given 'id'.

    Parameters:
    id (int): The ID of the book to update (indexed from 0).
    status (str): The new status to set for the book.

    Returns:
    None
    """
    header, rows = readDataSkippingHeader('biblioteka.csv')
    for row in rows:
        if int(row[0]) == id+1:
            row[4] = str(status)
            break
    writeDataSkippingHeader('biblioteka.csv', header, rows)
