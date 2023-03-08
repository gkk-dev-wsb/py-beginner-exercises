#!/usr/bin/env python3
# Zadanie 4.7
# Korzystając ze znanych Ci zagadnień (struktury danych, listy, łańcuchy znaków, konkatenacja łańcuchów znaków, f-stringi, pętle, funkcje, klasy, generatory liczb losowych, wczytywanie plików z danymi) zaproponuj program do generowania danych kadrowych przedsiębiorstwa. Pojedyńcza encja danych powinna zawierać następujące dane:
# - numer porządkowy
# - nazwisko
# - imię
# - płeć
# - stanowisko
# - data zatrudnienia
# - wynagrodzenie
# - niewykorzystane dni urlopu
# - Aby maksymalnie zbliżyć dane do rzeczywistości, skorzystaj z bazy danych dotyczących nazwisk i imion wystepujących w Polsce. Znajdziesz je na stronach:
# baza imion: https://dane.gov.pl/pl/dataset/1501,lista-imion-wystepujacych-w-rejestrze-pesel
# baza nazwisk: https://dane.gov.pl/pl/dataset/568,nazwiska-wystepujace-w-rejestrze-pesel
# Program powinien wczytać dane dot. imion i nazwisk i na tej podstawie generować dane osobowe. Wygenerowane dane zapisz do pliku w postaci wyrażeń rozdzielonych średnikami i nazwij go dane_kadrowe.csv. Plik powinien zawierać min. 1000 rekordów.

import csv
import os
import pandas as pd

DATA_DIR = os.path.join(os.getcwd(), '4', 'data')
HR_DATA_FILE = os.path.join(DATA_DIR, 'dane_kadrowe.csv')

df = pd.read_csv(os.path.join(DATA_DIR, 'IMIONA.csv'))
df2 = pd.read_csv(os.path.join(DATA_DIR, 'NAZWISKA.csv'))

print(df['IMIE'])
print(df2['Nazwisko'])

def writeHrData(filePath, data):
    with open(filePath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)

if __name__ == '__main__':
    writeHrData(HR_DATA_FILE, [])