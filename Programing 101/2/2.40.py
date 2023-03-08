#!/usr/bin/env python
# Napisz program obliczający silnię z zadanej liczby. Użytkownik podaje liczbę całkowitą. Program wykonuje obliczenia i wyświetla odpowiedź. Uwzględnij przypadek 0!=1.
num = int(input('Podaj liczbe ktorej silni szukasz: '))

assert num >= 0, "Nie istnieje silnia z liczby ujmnej."
if num == 0:
    print('Silnia wynosi 1')
else:
    fac = 1
    for i in range(1, num+1):
        fac *= i
    print(f'Silnia wynosi {fac}')
