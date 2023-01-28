#!/usr/bin/env python
# Utwórz program (z wykorzystaniem funkcji) do obliczania pól figur płaskich, który:
# • pozwoli użytkownikowi wybrać figurę, której pole chce obliczyć,
# • pobierze z klawiatury odpowiednie dane,
# • wyświetli właściwy wynik,
# • pozwoli użytkownikowi podjąć decyzję, czy chce uruchomić program ponownie, czy nie.
# Program powinien zawierać funkcje do obliczania pól następujących figur: trójkąt, prostokąt, koło, trapez, kwadrat, trójkąt równoboczny

from math import pi, sqrt

IS_DEBUG = False

def circleArea(r:float) -> float:
    return pi * r**2

def triangleArea(a:float, h:float) -> float:
    return a * h / 2

def trapezoidArea(a:float, b:float, h:float) -> float:
    return (a + b) * h / 2

MENU_TEXT = """
       Wybierz jakej figury pole chcesz obliczyć:
       1 - Trójkąt
       2 - Trojkat równoboczny
       3 - Trapez
       4 - Prostokąt
       5 - Kwadrat
       6 - Koło

       """

def verifyAreaCalculations():
    print('Weryfikowanie poprawności obliczeń pól')
    print('Trójkąt: ', triangleArea(1, 2))
    assert triangleArea(1, 2) == 1.0, "Pole trójkąta jest liczone niepoprawnie."
    print('Trójkąt równoboczny: ', triangleArea(5, 5*sqrt(3)/2))
    assert round(triangleArea(5, 5*sqrt(3)/2)) == round((5**2 * sqrt(3)) / 4), "Pole trojkata rownobocznego jest liczone niepoprawnie."
    print('Trapez: ', trapezoidArea(5, 10, 15))
    assert trapezoidArea(5, 10, 15) == 112.5, "Pole trapezu jest liczone niepoprawnie."
    print('prostokąt', trapezoidArea(10, 10, 5))
    assert trapezoidArea(10, 10, 5) == 10 * 5, "Pole prostokąta jest liczone niepoprawnie."
    print('kwadrat', trapezoidArea(5, 5, 5))
    assert trapezoidArea(5, 5, 5) == 5 * 5, "Pole kwadratu jest liczone niepoprawnie."
    print('koło', circleArea(10))
    assert round(circleArea(10)) == round(314.1592653589793), "Pole koła jest liczone niepoprawnie."
    print('Obliczenia ukończone, nie znaleziono błędów...')

def main():
    choice = int(input(MENU_TEXT))
    try:
        match choice:
            case 1:
                a, h = map(int, input('Podaj podstawe i wysokosc swojego trojkata: ').split())
                print('Pole: ', triangleArea(a, h))
            case 2:
                a = int(input('Podaj bok trójkąta: '))
                a_h = 5 * sqrt(3)/2
                print('Pole: ', triangleArea(a, a_h))
            case 3:
                a, b, h = map(int, input('Podaj górną podstawę, dolną podstawe i wysokosc swojego trapezu: ').split())
                print('Pole: ', trapezoidArea(a, b, h))
            case 4:
                a, b = map(int, input('Podaj boki swojego prostokąta: ').split())
                print('Pole: ', trapezoidArea(a, a, b))
            case 5:
                a = int(input('Podaj bok swojego kwadratu: '))
                print('Pole: ', trapezoidArea(a, a, a))
            case 6:
                r = int(input('Podaj promień swojego swojego koła: '))
                print('Pole: ', circleArea(r))
            case _:
                return "Program nie obsługuje wskazanej figury."
    except ValueError:
        print("Invalid arguments, try again.")

if __name__ == '__main__':
    if IS_DEBUG: verifyAreaCalculations()
    main()
