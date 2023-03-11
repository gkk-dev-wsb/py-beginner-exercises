#!/usr/bin/env python3
# Zadanie 4.4
# Napisz program, który tworzy plik i wpisuje liczby od 0-10, każdą w następnej linii, następnie zamyka i otwiera ponownie plik i dopisuje litery alfabetu, każdą następną w nowej linii.

import os
import string

ALPHABET = list(string.ascii_lowercase)

f = open(os.path.join(os.getcwd(), '4', 'data', 'numbers.4.4.txt'), 'w')
for i in range(0, 11):
    f.write(str(i)+'\n')
f.close()
f = open(os.path.join(os.getcwd(), '4', 'data', 'numbers.4.4.txt'), 'a')
for i in range(0, len(ALPHABET)):
    f.write(ALPHABET[i]+'\n')
f.close()
