#!/usr/bin/env python
# Stwórz kalkulator, który będzie odporny na niewłaściwe dane wprowadzane przez użytkownika. Program powinien pobierać pierwszą liczbę, drugą liczbę, znak operacji (+ - * /), wyświetlać wynik. Jeżeli użytkownik poda niepoprawną wartość, program pyta go ponownie o wpisanie właściwej informacji.

calculated = False
while not calculated:
    try:
        a, b = map(float, input("Wpisz liczby na których chcesz wykonać działanie: ").split())
        op = str(input("Podaj jakie działanie chcesz wykonać: "))
        res = 0
        match op:
            case '+':
                print(a, op, b, '=', a + b)
                calculated = True
            case '-':
                print(a, op, b, '=', a - b)
                calculated = True
            case '*':
                print(a, op, b, '=', a * b)
                calculated = True
            case '/':
                print(a, op, b, '=', a / b)
                calculated = True
            case _ :
                print("Podana operacja nie jest obsługiwana, spróbuj ponownie.")
                calculated = False
    except:
        print("Podano niepoprawne dane, spróbuj ponownie.")