# Wzorzec 3: Metoda Szablonowa
#
# Metoda Szablonowa to wzorzec projektowy, który definiuje szkielet algorytmu w
# klasie bazowej, ale pozwala podklasom na przesłonięcie niektórych kroków
# algorytmu bez zmiany jego struktury.
# Przykład: Proces wytwarzania napojów


from abc import ABC, abstractmethod


class BeverageMaker(ABC):
    """Klasa bazowa z metodą szablonową"""

    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Gotowanie wody...")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Nalewanie napoju do filiżanki...")

    @abstractmethod
    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        return True


class TeaMaker(BeverageMaker):
    """Klasa konkretna 1: Parzenie herbaty"""

    def brew(self):
        print("Parzenie herbaty...")

    def add_condiments(self):
        print("Dodawanie cytryny...")


class CoffeeMaker(BeverageMaker):
    """Klasa konkretna 2: Parzenie kawy"""

    def brew(self):
        print("Parzenie kawy...")

    def add_condiments(self):
        print("Dodawanie cukru i mleka...")


# Przykład użycia
if __name__ == '__main__':
    tea_maker = TeaMaker()
    tea_maker.prepare_beverage()

    coffee_maker = CoffeeMaker()
    coffee_maker.prepare_beverage()
