#!/usr/bin/env python3
# Zadanie 4.11
# Maksymalne tętno człowieka można oszacować korzystając z przybliżonego wyrażenia: HRmax=208−(0.7⋅A) gdzie:
# HRmax - maksymalne tętno w uderzeniach na minutę
# A - wiek w latach
# (na podstawie: http://www.shapesense.com/fitness-exercise/calculators/heart-rate-based-calorie-burn-calculator.shtml)
# Na podstawie powyższego równania wygeneruj dane wartości maksymalnego tętna w zależności od wieku. Pojedyńczy rekord powinien zawierać:
# - numer porządkowy
# - wiek
# - tętno maksymalne
# Dane zapisz do pliku z rozszerzeniem csv.

import csv
import os

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            columns = [row[0], row[1], row[2]]
            data.append(columns)
        return data

MAX_HR_DB = os.path.join(os.getcwd(), '4', 'data', 'maxHRDB.4.11.csv')

age = float(input("Podaj swój wiek: "))
HRmax = 208 - (0.7 * age)

data = import_csv(MAX_HR_DB)
last_row = data[-1][0]
idx = int(data[-1][0]) + 1
data.append([idx, age, HRmax])

with open(MAX_HR_DB, 'w') as f:
    writer = csv.writer(f, delimiter=';')
    for row in data:
        writer.writerow(row)