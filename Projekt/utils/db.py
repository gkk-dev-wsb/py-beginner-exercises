import os
import csv
import utils.constants as c


def readDataSkippingHeader(fileName: str):
    with open(os.path.join(c.DATA_DIR, fileName), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        return header, list(reader)


def writeDataSkippingHeader(fileName: str, header: list, rows: list[list]):
    with open(os.path.join(c.DATA_DIR, fileName), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows.insert(0, header)
        writer.writerows(rows)


def inicjujDane():
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


def logToFile(path, data):
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def update_czytacze(numerCzytacza, iloscksiazek):
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


def update_historia(id_ksiazki, data_oddania, czyUdana):
    header, rows = readDataSkippingHeader('historia.csv')
    for row in rows:
        if row[0] == str(id_ksiazki) and str(row[4]) == '0':
            row[4] = str(data_oddania)
            row[2] = str(czyUdana)
    writeDataSkippingHeader('historia.csv', header, rows)


def update_biblioteka(id, status):
    header, rows = readDataSkippingHeader('biblioteka.csv')
    for row in rows:
        if int(row[0]) == id+1:
            row[4] = str(status)
            break
    writeDataSkippingHeader('biblioteka.csv', header, rows)
