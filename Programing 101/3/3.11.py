#!/usr/bin/env python
from statistics import mean


def Pearson(lista_x, lista_y):
    """
    funkcja, dla dwóch list liczb rzeczywistych, oblicza
    odpowiadający im współczynnikkorelacji Pearsona
    - lista_x, lista_y - listy liczb rzeczywistych
    """
    sr_x = mean(lista_x)
    sr_y = mean(lista_y)

    # Licznik
    suma_L = 0
    for i in range(len(lista_x)):
        suma_L = suma_L + (lista_x[i]-sr_x)*(lista_y[i]-sr_y)

    # Mianownik
    suma_M = 0
    suma_M_L = 0
    suma_M_P = 0

    for x in lista_x:
        suma_M_L = suma_M_L + (x-sr_x)**2
        suma_M_L = suma_M_L**(1/2)
    for y in lista_y:
        suma_M_P = suma_M_P + (y-sr_y)**2
        suma_M_P = suma_M_P**(1/2)

    suma_M = suma_M_L * suma_M_P
    return suma_L / suma_M


# Wywołanie funkcji
print(Pearson([1, 2, 3, 4], [1, 2, 3, 4]))
