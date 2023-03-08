#!/usr/bin/env python
# Napisz program, który przyjmie od użytkownika długości trzech boków trójkąta, a następnie sprawdzi czy z podanych
# boków możliwe jest utworzenie jakiegokolwiek trójkąta. Wyświetl stosowny komunikat.
a, b, c = map(float, input('Podaj długość boków trójkąta: ').split())
if a + b > c and b + c > a and a + c > b:
    print('Mozna zbudowac trójkąt')
else:
    print('Nie da się zbudowac trójkąta, suma 2 bokow nie zawsze jest wieksza od pozostalego boku.')
