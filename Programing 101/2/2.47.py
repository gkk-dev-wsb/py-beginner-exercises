#!/usr/bin/env python
# Sito Erastotenesa: Utwórz program, który przyjmie liczbę naturalną i sprawdzi czy jest pierwsza czy nie.

num = int(input('Podaj liczbę o którym chcesz się dowiedzieć czy jest liczbą parzystą: '))

isPrime = True

if num in [0, 1]:
    isPrime = False
else:
    for i in range(2,num):
        if i == num:
            continue
        if num % i == 0:
            isPrime = False
            break

print(f"Liczba {'nie ' if not isPrime else ''}jest pierwszą.")
