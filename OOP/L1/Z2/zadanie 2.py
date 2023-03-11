class Punkt:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        print(f"Utworzono punkt ({self.x},{self.y})")

    def wyswietl(self):
        print(f"({self.x},{self.y})")

    def pobierzX(self):
        return self.x

    def pobierzY(self):
        return self.y

    def pobierzWsp(self):
        return Punkt(self.x, self.y)

    # Ad. 6
    # def ustawXY(self, x, y):
    #     self.x = x
    #     self.y = y

    def ustawXY(self, p):
        self.x = p.x
        self.y = p.y


class Test:
    def main(self):
        p1 = Punkt(1, 2)
        p2 = Punkt(5, 3)
        print("Współrzędne punktu p1 to:")
        p1.wyswietl()
        print("Współrzędne punktu p2 to:")
        p2.wyswietl()
        # Ad. 6
        # p1.ustawXY(22,11)
        # p1.wyswietl()
        p1.ustawXY(Punkt(11, 22))
        p1.wyswietl()

        p3 = Punkt(1, 2)
        p4 = Punkt(3, 4)
        p5 = Punkt(6, 5)
        p6 = Punkt(7, 8)
        p7 = Punkt(10, 9)

        # Ad. 10
        # TypeError: Punkt.__init__() missing 2 required positional arguments: 'x' and 'y'
        # p8 = Punkt()


if __name__ == "__main__":
    t = Test()
    t.main()
