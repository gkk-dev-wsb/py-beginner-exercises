# Zadanie 4.3
# Stwórz plik tekstowy z kilkoma wierszami danych, a następnie napisz program, który wypisze zawartość utworzonego pliku do konsoli.

import os

f = open(os.path.join(os.getcwd(), '4', 'data', 'file4.3.txt'))
print(f.read())
