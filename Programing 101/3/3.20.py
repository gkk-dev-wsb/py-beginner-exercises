#!/usr/bin/env python
# Utwórz wyrażenie lambda przyjmujące dwa argumenty (liczby rzeczywiste) i wykonujące na nich kwadrat różnicy.
foo = lambda a, b: (float(a)-float(b))**2
print(foo(1, 2))
print(foo(12, 2))
print(foo(10, 24))
print(foo(11, 2))
