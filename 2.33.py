#!/usr/bin/env python
# Napisz program do wystawiania ocen. Uczniowie pisali sprawdzian, na którym maksylanie można było zdobyć 50 pkt.
# Użytkownik wprowadza uzyskaną liczbę punktów, a program zwraca ocenę jaką pownien uzyskać. Progi ocen są następujące: 0-39% - ndst, 40-49% - dop, 50-69% -dst, 70-84% - db, 85-99% bdb, 100% - cel.
max_points = 50
points = int(input("Podaj ilosc punktow uzyskana na tescie: "))
assert points >= 0, "Nie mozna uzyskac punktow ujemnych"
percent = points / max_points * 100
print('Uzyskano ocene:')
if percent <= 39:
    print('ndst')
elif percent <= 49:
    print('dop')
elif percent <= 69:
    print('dst')
elif percent <= 84:
    print('db')
elif percent <= 99:
    print('bdb')
else:
    print('cel')
