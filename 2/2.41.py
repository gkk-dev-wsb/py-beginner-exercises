#!/usr/bin/env python
# Napisz program obliczający zadany wyraz ciągu Fibonacciego. Użytkownik podaje numer wyrazu, program wykonuje
# obliczenia i wyświetla wynik.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n-2)

num = int(input('Podaj numer wyrazu ciagu fibonacciego ktorego szukasz: '))
print(f'Wynosi on {fib(num)}')
