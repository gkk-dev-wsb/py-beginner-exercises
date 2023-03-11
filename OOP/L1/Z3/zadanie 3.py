class human:
    def __init__(self, respect, expertise, cash, weight, stamina):
        self.respect = respect
        self.expertise = expertise
        self.cash = cash
        self.weight = weight
        self.stamina = stamina

    def show_respect(self):
        print(f"Twój poziom respektu: {self.respect}")

    def show_weight(self):
        print(self.weight)

    def show_human(self):
        print("This is a human:")
        print("respect: ", self.respect)
        print("expertise: ", self.expertise)
        print("cash: ", self.cash)
        print("weight: ", self.weight)
        print("stamina: ", self.stamina)

    def calculate_strength(self):
        return self.respect * 2 + self.cash / self.weight

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


class cat():
    def __init__(self, name, age, color, race, weight):
        self._name = name
        self._age = age
        self._color = color
        self._race = race
        self._weight = weight

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        self._age = age

    def setColor(self, color):
        self._color = color

    def setRace(self, race):
        self._race = race

    def setWeight(self, weight):
        self._weight = weight

    def getWeight(self):
        return self._weight

    def getName(self):
        return self._name

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


if __name__ == "__main__":
    h = human(100, 'enginnering', 1000, 90, 20)
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

    c = cat('Filemon', 12, 'red', 'persian', 1.5)
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
