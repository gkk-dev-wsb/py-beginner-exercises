#!/usr/bin/env python
# Napisz program, który przyjmie od użytkownika długości trzech boków trójkąta, a następnie wyświetli komunikat, czy z
# takich boków można zbudować trójkąt prostokątny.
a, b, c = map(float, input('Podaj długość boków trójkąta: ').split())
if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
    print('Mozna zbudowac trójkąt prostokątny')
else:
    print('Nie da się zbudowac trójkąta. Podane dlugosci bokow nie spelniaja Twierdzenia Pitagorasa')
