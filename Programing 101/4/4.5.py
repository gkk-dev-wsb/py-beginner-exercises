#!/usr/bin/env python3
# Zadanie 4.5
# Napisz program, który umożliwia zapisywanie do pliku .txt danych takich jak: imię, nazwisko, stanowisko i wynagrodzenie. Użytkownik ma mieć możliwość dodawania, usuwania i wypisywania listy osób. Usuwanie pozycji powinno działać po podaniu samego nazwiska osoby. Program powinien posiadać interaktywne menu: D-dodaj, U-usuń, W-wypisz i Q-wyjście. Podpowiedź: Utwórz funkcje: dodaj, usuń, pokaż zawartość pliku

import os
import sys
from os.path import exists

MENU = """
D - dodaj
U - usuń
W - wypisz
Q - wyjście
"""


def removeSpecificLine(file, line_to_remove):
    with open(file, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            if number not in [line_to_remove]:
                fp.write(line)


class Person():
    def __init__(self):
        self.name = input("Podaj imie: ")
        self.lastname = input("Podaj nazwisko: ")
        self.position = input("Podaj stanowisko: ")
        self.compensation = input("Podaj wynagrodzenie: ")


if __name__ == "__main__":
    PERSON_DB = os.path.join(os.getcwd(), '4', 'data', 'personDB.4.5.txt')

    print(MENU)
    opt = (input("Wybierze opcje: ")).upper()
    match opt:
        case 'D':
            if (exists(PERSON_DB)):
                f = open(PERSON_DB, 'a')
            else:
                f = open(PERSON_DB, 'w')
            p = Person()
            f.write(p.name+' ')
            f.write(p.lastname+' ')
            f.write(p.position+' ')
            f.write(p.compensation+'\n')
        case 'U':
            if (exists(PERSON_DB)):
                idx = int(input("Who to remove (provide index): "))
                removeSpecificLine(PERSON_DB, idx)
            else:
                print("Currently there is no person database...")
                sys.exit(3)
        case 'W':
            f = open(PERSON_DB, 'r')
            print(f.read())
        case 'Q':
            print("Exiting...")
            sys.exit(1)
        case _:
            print("Option doesn't exist. Try again.")
            sys.exit(2)
