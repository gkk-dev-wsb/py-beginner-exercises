import math


class FunkcjaKwadratowa:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def pretty(self) -> str:
        return f"({self.a})x^2+({self.b})x+({self.c})"

    def __noRealSolution(self) -> None:
        e = f"Podana funkcja: {self.pretty} nie"\
            f"ma rozwiązań w dziedzienie rzeczywistej"
        raise ValueError(e)

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


class Zespolona:
    def __init__(self, re: int, im: int) -> None:
        self.re = re
        self.im = im

    @property
    def pretty(self) -> str:
        return f"({self.re})+({self.im})i"

    @property
    def modul(self):
        return math.sqrt(self.re**2+self.im**2)

    def dodaj(self, z):
        return Zespolona(self.re + z.re, self.im + z.im)

# TODO: How to type anotate class in itselfs?
# inside Zespolona > def mnoz(self, z2:Zespolona):
# https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation
    def mnoz(self, z):
        return Zespolona((self.re*z.re - self.im*z.im), (self.re*z.im+self.im*z.re))


class UlamekZ:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        if b == 0:
            raise ValueError("Mianownik nie moze byc równy 0")
        else:
            self.b = b

    @property
    def pretty(self) -> str:
        skrocona = self.skroc()
        return f"({skrocona.a})/({skrocona.b})"

    def skroc(self):
        gcd = math.gcd(int(self.a), int(self.b))
        return UlamekZ(int(self.a / gcd), int(self.b / gcd))

    def dodaj(self, uz):
        div = uz.b * self.b
        res = UlamekZ(self.a*uz.b + self.b*uz.a, div)
        return res.skroc()

    def odejmij(self, uz):
        div = uz.b * self.b
        res = UlamekZ(self.a*uz.b - self.b*uz.a, div)
        return res.skroc()

    def mnoz(self, uz):
        return UlamekZ(self.a*uz.a, self.b*uz.b).skroc()

    def dziel(self, uz):
        return UlamekZ(self.a*uz.b, self.b*uz.a).skroc()


if __name__ == "__main__":
    print("""
|==============================================|
|Testowe uzycie klas i wszystkich ich metod:   |
|==============================================|
|- FunkcjaKwadratowa                           |
|    - FunkcjaKwadratowa.Rozwiaz()             |
|- Zespolona                                   |
|    - Zespolona.dodaj(Zespolona)              |
|    - Zespolona.mnoz(Zespolona)               |
|    - Zespolona.modul                         |
|- UlamekZ                                     |
|    - UlamekZ.dodaj(UlamekZ)                  |
|    - UlamekZ.odejmij(UlamekZ)                |
|    - UlamekZ.mnoz(UlamekZ)                   |
|    - UlamekZ.dziel(UlamekZ)                  |
|==============================================|

    """)
    f1 = FunkcjaKwadratowa(1, -4, 4)  # ax^2+bx+c
    f2 = FunkcjaKwadratowa(0, 2, 3)  # bx+c
    # f3 = FunkcjaKwadratowa(0,0,3) # Error: Funkcja nie ma rozwiązań w dziedzienie rzeczywistej
    f4 = FunkcjaKwadratowa(0, 0, 0)  # 0

    assert f1.Rozwiaz() == (2.0, 2.0)
    assert f2.Rozwiaz() == -1.5
    assert f4.Rozwiaz() == math.inf

    print("Przykładowe rozwiązania funkcji:\n")
    print(f1.pretty, ':', f1.Rozwiaz())
    print(f2.pretty, ':', f2.Rozwiaz())
    # print(f3.pretty, ':', f3.Rozwiaz())
    print(f4.pretty, ':', f4.Rozwiaz())

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
    print(z1.pretty, '+', z3.pretty, '=', z1.mnoz(z3).pretty)
    print(z4.pretty, '+', z3.pretty, '=', z4.mnoz(z3).pretty)
    print(z1.pretty, '+', z4.pretty, '=', z1.mnoz(z4).pretty)
    print("z1.modul")
    print(z1.modul)
    print(z2.modul)
    print(z3.modul)
    print(z4.modul)
    print(z5.modul)

    print("Przykładowe ulamki:\n")
    uz1 = UlamekZ(1, 1)
    # uz2 = UlamekZ(1,0) # Error: mianownik ułamka nie moze byc rowny 0
    uz3 = UlamekZ(0, 1)
    uz4 = UlamekZ(24, 96)
    print(uz1.pretty, uz3.pretty, uz4.pretty)
    print("dodaj(self, uz):")
    print(uz1.pretty, '+', uz3.pretty, '=', uz1.dodaj(uz3).pretty)
    print(uz4.pretty, '+', uz3.pretty, '=', uz4.dodaj(uz3).pretty)
    print(uz1.pretty, '+', uz4.pretty, '=', uz1.dodaj(uz4).pretty)
    print("odejmij(self, uz):")
    print(uz1.pretty, '-', uz3.pretty, '=', uz1.odejmij(uz3).pretty)
    print(uz4.pretty, '-', uz3.pretty, '=', uz4.odejmij(uz3).pretty)
    print(uz1.pretty, '-', uz4.pretty, '=', uz1.odejmij(uz4).pretty)
    print("mnoz(self, uz):")
    print(uz1.pretty, '*', uz3.pretty, '=', uz1.mnoz(uz3).pretty)
    print(uz4.pretty, '*', uz3.pretty, '=', uz4.mnoz(uz3).pretty)
    print(uz1.pretty, '*', uz4.pretty, '=', uz1.mnoz(uz4).pretty)
    print("dziel(self, uz):")
    # print(uz1.pretty,'/',uz3.pretty,'=', uz1.dziel(uz3)) # Error: mianownik nie moze byc rowny zero
    # print(uz4.pretty,'/',uz3.pretty,'=',uz4.dziel(uz3).pretty) Error: mianownik nie moze byc rowny zero
    print(uz1.pretty, '/', uz4.pretty, '=', uz1.dziel(uz4).pretty)
