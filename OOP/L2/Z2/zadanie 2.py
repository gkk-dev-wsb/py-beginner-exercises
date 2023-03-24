# > Jako komentarz dodać swoje uwagi na temat dziedziczenia, polimorfi,
# > hermetyzacji. Zaobserwowane wady i zalety. Min jedno zdanie, ale do trzech
# > na każdą technikę programowania obiektowego.

# Dziedziczenie to proces, w którym klasa dziedziczy zachowania i właściwości
# po innej klasie. Zaletą dziedziczenia jest możliwość ponownego użycia kodu
# i łatwiejsze zarządzanie hierarchią klas. Jednakże, zbyt wiele poziomów
# dziedziczenia może prowadzić do trudniejszego debugowania i utrzymania kodu.

# Polimorfizm pozwala na tworzenie kodu, który może działać z różnymi typami
# obiektów, co zwiększa elastyczność i modularność kodu. Wadą polimorfizmu jest to,
# że wymaga on znajomości typów i interfejsów obiektów, z którymi pracujemy, co
# może być trudne w większych projektach.

# Hermetyzacja to mechanizm zapewniający kontrolowany dostęp do danych i funkcji
# wewnątrz klasy. Zaletą hermetyzacji jest zwiększenie bezpieczeństwa kodu,
# ponieważ ogranicza to dostęp do wrażliwych danych tylko do klasy, która ma do
# nich dostęp. Jednakże, zbyt duża hermetyzacja może prowadzić do trudniejszej
# obsługi kodu i utrudniać testowanie.

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, weight, name):
        self._weight = weight
        self._name = name

    def show_weight(self):
        print(self.getWeight())

    def setWeight(self, weight):
        self._weight = weight

    def getWeight(self):
        return self._weight

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    @abstractmethod
    def howIsTheWeight(self):
        pass


class Human(Animal):
    def __init__(self, respect, expertise, cash, weight, stamina, name):
        super(Human, self).__init__(weight, name)
        self.respect = respect
        self.expertise = expertise
        self.cash = cash
        self.stamina = stamina

    def __calculateBMI(self):
        return self.stamina / self.getWeight() - self.cash

    def howIsTheWeight(self):
        if self.__calculateBMI() == 0:
            return "niedowaga"
        elif self.__calculateBMI() == 1:
            return "waga prawidłowa"
        else:
            return "nadwaga"

    def show_respect(self):
        print(f"Twój poziom respektu: {self.respect}")

    def show_human(self):
        print("This is a human:")
        print("respect: ", self.respect)
        print("expertise: ", self.expertise)
        print("cash: ", self.cash)
        print("weight: ", self.getWeight())
        print("stamina: ", self.stamina)

    def calculate_strength(self):
        return self.respect * 2 + self.cash / self.getWeight()

    def setExpertise(self, expertise):
        self.expertise = expertise

    def setStamina(self, stamina):
        self.stamina = stamina

    def earn_repect(self, respect_earned):
        print(f"Wow! You've earned {respect_earned} point! Keep it up CJ")
        self.respect *= respect_earned

    def setCashFromDollars(self):
        dolars = input("podaj kwote (w $): ")
        print(f"Settings cash from Dollars")
        print("4 PLN = 1$")
        self.cash = dolars * 4

    def setCashFromPounds(self):
        pounds = input("podaj kwote (w GBP): ")
        print(f"Settings cash from Pounds")
        print("5 PLN = 1 GBP")
        self.cash = pounds * 5

    def setCashFromPLN(self):
        pln = input("podaj kwote (w PLN): ")
        self.cash = pln


class Cat(Animal):
    def __init__(self, name, age, color, race, weight):
        super(Cat, self).__init__(weight, name)
        self._name = name
        self._age = age
        self._color = color
        self._race = race

    def __calculateBMI(self):
        return self.getWeight() / self.getAge()

    def howIsTheWeight(self):
        if self.__calculateBMI() == 0:
            return "nadwaga"
        elif self.__calculateBMI() == 1:
            return "waga prawidłowa"
        else:
            return "niedowaga"

    def setAge(self, age):
        self._age = age

    def setColor(self, color):
        self._color = color

    def setRace(self, race):
        self._race = race

    def getAge(self):
        return self._age

    def getColor(self):
        return self._color

    def getRace(self):
        return self._race

    def miau(self):
        print(f"Hi, I'm {self.getName()} and I'm {self.getRace()} so I say:")
        for i in range(self.getAge()):
            print('miau!')

    def sayMyName(self):
        print(f"My name is {self.getName()}")

    def show_importance(self):
        importance = self._age * 2 + self._weight
        print(importance)
        return importance


class Dog(Animal):
    def __init__(self, weight, foodAmount, name):
        super(Dog, self).__init__(weight, name)
        self.foodAmount = foodAmount

    def __calculateBMI(self):
        return self.foodAmount / self.getWeight()

    def eat(self, amountEaten):
        print("om nom nom... woof!")
        self.foodAmount -= amountEaten

    def howIsTheWeight(self):
        if self.__calculateBMI() == 0:
            return "niedowaga"
        elif self.__calculateBMI() == 1:
            return "nadwaga"
        else:
            return "waga prawidłowa"


def test_human(h: Human):
    print("Showing human...")
    h.show_respect()
    h.show_weight()
    h.show_human()
    print("Doing human methods-things...")
    h.earn_repect(1000)
    h.calculate_strength()
    print("Doing human cash calculation (please provide examplary numbers)...")
    h.setCashFromDollars()
    h.setCashFromPLN()
    h.setCashFromPounds()
    print("Setting all of human properties...")
    h.setExpertise('scrum')
    h.setStamina(200)


def test_cat(c: Cat):
    print("Getting all of cat properties...")
    print(c.getAge())
    print(c.getColor())
    print(c.getName())
    print(c.getRace())
    print(c.getWeight())
    print("Setting all of cat properties...")
    c.setAge(21)
    c.setColor('black')
    c.setName('Bonifacy')
    c.setRace('british')
    c.setWeight(120.12)
    print("Run all of cat methods...")
    c.miau()
    c.sayMyName()
    c.show_importance()


def test_dog(d: Dog):
    print(d.getWeight())
    print(d.getName())
    d.eat(20)


def test_abstract(h: Human, c: Cat, d: Dog):
    print(f"how Is The {h.getName()} Weight", h.howIsTheWeight())
    print(f"how Is The {c.getName()} Weight", c.howIsTheWeight())
    print(f"how Is The {d.getName()} Weight", d.howIsTheWeight())


if __name__ == "__main__":
    h = Human(100, 'enginnering', 1000, 90, 20, "Janusz")
    test_human(h)
    c = Cat('Filemon', 12, 're`d', 'persian', 1.5)
    test_cat(c)
    d = Dog(10, 1000, "Fafik")
    test_dog(d)
    test_abstract(h, c, d)
