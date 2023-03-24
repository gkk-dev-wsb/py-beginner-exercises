import math


class Funkcja:
    def Rozwiaz(self) -> int | tuple[int]:
        raise NotImplementedError(
            "Nie istnieje uniwersalny sposób na rozwiązanie kazdej funkcji")

    # Uniwersalna funkcja przeniesiona z FunkcjaKwadratowa, gdyz kazda funkcja
    # moze nie miec w pewnych warunkach rozwiazan.
    def __noRealSolution(self) -> None:
        e = f"Podana funkcja: {self.pretty} nie"\
            f"ma rozwiązań w dziedzienie rzeczywistej"
        raise ValueError(e)


class FunkcjaLiniowa(Funkcja):
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    @property
    def pretty(self) -> str:
        return f"({self.a})x+({self.b})"

    def Rozwiaz(self) -> int:
        if self.a == 0:
            self.__noRealSolution()
        else:
            return -self.b / self.a


class FunkcjaKwadratowa(Funkcja):
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def pretty(self) -> str:
        return f"({self.a})x^2+({self.b})x+({self.c})"

    def Rozwiaz(self) -> int | tuple[int]:
        if self.a != 0:
            delta = self.b**2 - 4*self.a*self.c
            if delta > 0:
                return (-math.sqrt(delta) + self.b / 2*self.a,
                        -math.sqrt(delta) - self.b / 2*self.a)
            elif delta < 0:
                self.__noRealSolution()
            else:
                return (-self.b/2*self.a, -self.b/2*self.a)
        else:
            if self.b == 0:
                if self.c == 0:
                    return math.inf
                else:
                    self.__noRealSolution()
            else:
                return -self.c/self.b


class Liczba:
    def dodaj(self):
        raise NotImplementedError(
            "Nie istnieje uniwersalny sposób na sumowanie liczb")

    def mnoz(self):
        raise NotImplementedError(
            "Nie istnieje uniwersalny sposób na mnozenie liczb")


class Rzeczywista(Liczba):
    def __init__(self, re: int) -> None:
        self.re = re

    def odejmij(self, r):
        return Rzeczywista(self.re - r.re)

    def dziel(self, r):
        return Rzeczywista(self.re / r.re)

    def dodaj(self, r):
        return Rzeczywista(self.re + r.re)

    def mnoz(self, r):
        return Rzeczywista(self.re * r.re)

    def __str__(self) -> str:
        return str(self.re)


class Zespolona(Liczba):
    def __init__(self, re: int, im: int) -> None:
        self.re = re
        self.im = im

    @ property
    def pretty(self) -> str:
        return f"({self.re})+({self.im})i"

    @ property
    def modul(self):
        return math.sqrt(self.re**2+self.im**2)

    def dodaj(self, z):
        return Zespolona(self.re + z.re, self.im + z.im)

    def mnoz(self, z):
        return Zespolona((self.re*z.re - self.im*z.im), (self.re*z.im+self.im*z.re))


class Ulamek:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        if b == 0:
            raise ValueError("Mianownik nie moze byc równy 0")
        else:
            self.b = b

    def dodaj(self, uz):
        div = uz.b * self.b
        res = Ulamek(self.a*uz.b + self.b*uz.a, div)
        return res

    def odejmij(self, uz):
        div = uz.b * self.b
        res = Ulamek(self.a*uz.b - self.b*uz.a, div)
        return res

    def mnoz(self, uz):
        return Ulamek(self.a*uz.a, self.b*uz.b)

    def dziel(self, uz):
        return Ulamek(self.a*uz.b, self.b*uz.a)

    def __str__(self) -> str:
        return f"({self.a})/({self.b})"


class UlamekD(Ulamek):
    def __init__(self, a: int, b: int) -> None:
        if not (10 <= b <= 10**4):
            raise ValueError("Mianownik musi być w przedziale od 10 do 10^4")
        super().__init__(a, b)


class UlamekZ(Ulamek):
    def __str__(self) -> str:
        skrocona = self.skroc()
        return f"({skrocona.a})/({skrocona.b})"

    def skroc(self):
        gcd = math.gcd(int(self.a), int(self.b))
        return UlamekZ(int(self.a / gcd), int(self.b / gcd))


def test_funkcjaKwadratowa():
    f1 = FunkcjaKwadratowa(1, -4, 4)  # ax^2+bx+c
    f2 = FunkcjaKwadratowa(0, 2, 3)  # bx+c
    # f3 = FunkcjaKwadratowa(0,0,3) # Error: Funkcja nie ma rozwiązań w dziedzienie rzeczywistej
    f4 = FunkcjaKwadratowa(0, 0, 0)  # 0

    assert f1.Rozwiaz() == (2.0, 2.0)
    assert f2.Rozwiaz() == -1.5
    assert f4.Rozwiaz() == math.inf

    print("Przykładowe rozwiązania funkcji kwadratowej:\n")
    print(f1.pretty, ':', f1.Rozwiaz())
    print(f2.pretty, ':', f2.Rozwiaz())
    # print(f3.pretty, ':', f3.Rozwiaz())
    print(f4.pretty, ':', f4.Rozwiaz())


def test_funkcjaLiniowa():
    f1 = FunkcjaLiniowa(1, -4)  # ax+b
    # Error: Funkcja nie ma rozwiązań w dziedzienie rzeczywistej dla a = 0
    # f2 = FunkcjaLiniowa(0, 2)

    assert f1.Rozwiaz() == 4
    # f2.Rozwiaz()

    print("Przykładowe rozwiązania funkcji liniowej:\n")
    print(f1.pretty, ':', f1.Rozwiaz())
    # print(f2.pretty, ':', f2.Rozwiaz())


def test_Zespolona():
    print("Przykładowe liczby zespolone:\n")
    z1 = Zespolona(1, 1)
    z2 = Zespolona(1, 0)
    z3 = Zespolona(0, 1)
    z4 = Zespolona(0, 0)
    z5 = Zespolona(21, 5678)
    print(z1.pretty, z2.pretty, z3.pretty, z4.pretty,)
    print("z1.dodaj(zx)")
    print(z1.pretty, '+', z3.pretty, '=', z1.dodaj(z3).pretty)
    print(z4.pretty, '+', z3.pretty, '=', z4.dodaj(z3).pretty)
    print(z1.pretty, '+', z4.pretty, '=', z1.dodaj(z4).pretty)
    print("z1.mnoz(zx)")
    print(z1.pretty, '*', z3.pretty, '=', z1.mnoz(z3).pretty)
    print(z4.pretty, '*', z3.pretty, '=', z4.mnoz(z3).pretty)
    print(z1.pretty, '*', z4.pretty, '=', z1.mnoz(z4).pretty)
    print("z1.modul")
    print(z1.modul)
    print(z2.modul)
    print(z3.modul)
    print(z4.modul)
    print(z5.modul)


def test_Rzeczywista():
    print("Przykładowe liczby rzeczywiste:\n")
    rz1 = Rzeczywista(1)
    rz2 = Rzeczywista(321)
    rz3 = Rzeczywista(12)
    rz4 = Rzeczywista(32)
    print(rz1, rz2, rz3, rz4)
    print("rz1.dodaj(rz)")
    print(rz1, '+', rz3, '=', rz1.dodaj(rz3))
    print(rz4, '+', rz3, '=', rz4.dodaj(rz3))
    print(rz1, '+', rz4, '=', rz1.dodaj(rz4))
    print("rz1.mnoz(rz)")
    print(rz1, '*', rz3, '=', rz1.mnoz(rz3))
    print(rz4, '*', rz3, '=', rz4.mnoz(rz3))
    print(rz1, '*', rz4, '=', rz1.mnoz(rz4))
    print("rz1.odejmij(rz)")
    print(rz1, '-', rz3, '=', rz1.odejmij(rz3))
    print(rz4, '-', rz3, '=', rz4.odejmij(rz3))
    print(rz1, '-', rz4, '=', rz1.odejmij(rz4))
    print("rz1.dziel(rz)")
    print(rz1, '/', rz3, '=', rz1.dziel(rz3))
    print(rz4, '/', rz3, '=', rz4.dziel(rz3))
    print(rz1, '/', rz4, '=', rz1.dziel(rz4))


def test_UlamekZ():
    print("Przykładowe ulamkiZ:\n")
    uz1 = UlamekZ(1, 1)
    # uz2 = UlamekZ(1,0) # Error: mianownik ułamka nie moze byc rowny 0
    uz3 = UlamekZ(0, 1)
    uz4 = UlamekZ(24, 96)
    print(uz1, uz3, uz4)
    print("dodaj(self, uz):")
    print(uz1, '+', uz3, '=', uz1.dodaj(uz3))
    print(uz4, '+', uz3, '=', uz4.dodaj(uz3))
    print(uz1, '+', uz4, '=', uz1.dodaj(uz4))
    print("odejmij(self, uz):")
    print(uz1, '-', uz3, '=', uz1.odejmij(uz3))
    print(uz4, '-', uz3, '=', uz4.odejmij(uz3))
    print(uz1, '-', uz4, '=', uz1.odejmij(uz4))
    print("mnoz(self, uz):")
    print(uz1, '*', uz3, '=', uz1.mnoz(uz3))
    print(uz4, '*', uz3, '=', uz4.mnoz(uz3))
    print(uz1, '*', uz4, '=', uz1.mnoz(uz4))
    print("dziel(self, uz):")
    # print(uz1,'/',uz3,'=', uz1.dziel(uz3)) # Error: mianownik nie moze byc rowny zero
    # print(uz4,'/',uz3,'=',uz4.dziel(uz3)) Error: mianownik nie moze byc rowny zero
    print(uz1, '/', uz4, '=', uz1.dziel(uz4))


def test_UlamekD():
    print("Przykładowe ulamkiD:\n")
    ud1 = UlamekD(1, 10000)
    # ud2 = UlamekD(1,0) # Error: mianownik ułamka musi znajdować się pomiędzy 10-10^4
    ud3 = UlamekD(0, 1000)
    ud4 = UlamekD(24, 96)
    # Error: mianownik ułamka musi znajdować się pomiędzy 10-10^4
    # ud5 = UlamekD(1, 9)

    print(ud1, ud3, ud4)
    print("dodaj(self, uz):")
    print(ud1, '+', ud3, '=', ud1.dodaj(ud3))
    print(ud4, '+', ud3, '=', ud4.dodaj(ud3))
    print(ud1, '+', ud4, '=', ud1.dodaj(ud4))
    print("odejmij(self, uz):")
    print(ud1, '-', ud3, '=', ud1.odejmij(ud3))
    print(ud4, '-', ud3, '=', ud4.odejmij(ud3))
    print(ud1, '-', ud4, '=', ud1.odejmij(ud4))
    print("mnoz(self, uz):")
    print(ud1, '*', ud3, '=', ud1.mnoz(ud3))
    print(ud4, '*', ud3, '=', ud4.mnoz(ud3))
    print(ud1, '*', ud4, '=', ud1.mnoz(ud4))
    print("dziel(self, uz):")
    # print(ud1,'/',ud3,'=', ud1.dziel(uz3)) # Error: mianownik nie moze byc rowny zero
    # print(ud4,'/',ud3,'=',ud4.dziel(uz3)) Error: mianownik nie moze byc rowny zero
    print(ud1, '/', ud4, '=', ud1.dziel(ud4))


if __name__ == "__main__":
    print("""
    |==============================================|
    |Testowe uzycie klas i wszystkich ich metod:   |
    |==============================================|
    |- FunkcjaKwadratowa                           |
    |    - FunkcjaKwadratowa.Rozwiaz()             |
    |- FunkcjaLiniowa                              |
    |    - FunkcjaLiniowa.Rozwiaz()                |
    |- Zespolona                                   |
    |    - Zespolona.dodaj(Zespolona)              |
    |    - Zespolona.mnoz(Zespolona)               |
    |    - Zespolona.modul                         |
    |- Rzeczywista                                 |
    |    - Rzeczywista.dodaj(Rzeczywista)          |
    |    - Rzeczywista.mnoz(Rzeczywista)           |
    |    - Rzeczywista.dziel(Rzeczywista)          |
    |    - Rzeczywista.odejmij(Rzeczywista)        |
    |- UlamekZ                                     |
    |    - UlamekZ.dodaj(UlamekZ)                  |
    |    - UlamekZ.odejmij(UlamekZ)                |
    |    - UlamekZ.mnoz(UlamekZ)                   |
    |    - UlamekZ.dziel(UlamekZ)                  |
    |- UlamekD                                     |
    |    - UlamekD.dodaj(UlamekD)                  |
    |    - UlamekD.odejmij(UlamekD)                |
    |    - UlamekD.mnoz(UlamekD)                   |
    |    - UlamekD.dziel(UlamekD)                  |
    |==============================================|

        """)
    test_funkcjaKwadratowa()
    test_funkcjaLiniowa()
    test_Zespolona()
    test_Rzeczywista()
    test_UlamekZ()
    test_UlamekD()
