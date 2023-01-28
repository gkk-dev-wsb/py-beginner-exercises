#!/usr/bin/env python
# Trójmian kwadratowy wyraża się wzorem: . Napisz program, w którym użytkownik wprowadza współczynniki trójmianu
# kwadratowego (a, b, c), a następnie sprawdza, czy trójmian o podanych współczynnikach ma 2, 1 czy 0 rozwiązań w
# zbiorze liczb rzeczywistych.
# Uzupełnienie matematyczne: Należy sprawdzić znak delty: . Jeżeli:
# • trójmian ma 2 pierwiastki,
# • trójmian ma 1 pierwiastek,
# • trójmian nie ma pierwiastków rzeczywistych.
from math import sqrt

a = float(input('Dla reprezentacji trójmianu kwadratowego ax^2+bx+c, podaj współczynniki\na: '))
b = float(input('b: '))
c = float(input('c: '))

delta = b**2 - 4*a*c
if delta > 0:
    x1 =  -b + sqrt(delta) / 2*a
    x2 =  -b - sqrt(delta) / 2*a
    print('Rozwiązanie:', 'x1:', x1, 'x2:', x2)
elif delta == 0:
    x1 =  -b / 2*a
    print('Rozwiązanie:', 'x1:', x1)
else:
    print('Brak rozwiązań w dziedzinie rzeczywistej')
