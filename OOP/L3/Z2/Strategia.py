# Wzorzec 1: Strategia
#
# Strategia to wzorzec projektowy, który pozwala na definiowanie rodziny
# algorytmów, umieszczenie każdego z nich w osobnej klasie i sprawienie,
# aby były one wzajemnie zamienne. Dzięki temu algorytm może być wybierany
# dynamicznie w trakcie działania programu.
# Przykład: Prosty system obliczania kosztów wysyłki

from abc import ABC, abstractmethod


class ShippingCostStrategy(ABC):
    """Klasa bazowa dla strategii"""
    @abstractmethod
    def calculate(self, weight):
        pass


class FixedShippingCost(ShippingCostStrategy):
    """Strategia 1: Wysyłka stała"""

    def calculate(self, weight):
        return 10


class WeightBasedShippingCost(ShippingCostStrategy):
    """Strategia 2: Wysyłka zależna od wagi"""

    def calculate(self, weight):
        return 5 + weight * 2


class ShippingCostCalculator:
    """Kontekst"""

    def __init__(self, strategy: ShippingCostStrategy):
        self.strategy = strategy

    def calculate_shipping_cost(self, weight):
        return self.strategy.calculate(weight)


# Przykład użycia
if __name__ == '__main__':
    package_weight = 10

    fixed_strategy = FixedShippingCost()
    weight_based_strategy = WeightBasedShippingCost()

    calculator = ShippingCostCalculator(fixed_strategy)
    print("Obliczenie kosztu używając strategii kosztu stałego:",
          calculator.calculate_shipping_cost(package_weight))

    calculator = ShippingCostCalculator(weight_based_strategy)
    print("Obliczenie kosztu używając strategii kosztu bazującego na wadze przesyłki:",
          calculator.calculate_shipping_cost(package_weight))
