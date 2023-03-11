#!/usr/bin/env python
# 5 Napisz program do obliczania współczynnika BMI. Użytkownik podaje swoją wagę (w kilogramach) i wzrost (w metrach). Następnie program wykonuje obliczenia współczynnika zgodnie ze wzorem: Jeżeli wynik mieści się w przedziale
# (18.5-24.9) program wyświetla komunikat ”waga jest prawidłowa”. Jeżeli wynik jest poniżej wartości 18.5 to wyświetla
# komunikat ”niedowaga”. Jeżeli z kolei wynik jest powyżej wartości 24.9 to program wyświetla komunikat ”nadwaga”.
h = int(input('Podaj wzrost w metrach: '))
m = int(input('Podaj wage w kg: '))
bmi = m / h**2
if bmi < 18.5:
    print('niedowaga')
elif bmi < 24.9:
    print('waga jest prawidłowa')
else:
    print('nadwaga')
