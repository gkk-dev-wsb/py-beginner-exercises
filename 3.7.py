#!/usr/bin/env python
# Związek między temperaturą w skali Celsjusza, a temperaturą w skali Fahrenheita ma postać:
# • C = (F − 32) ∗ (5/9) (przy przeliczaniu skali Fahrenheita na Celsjusza),
# • F = (C ∗ (9/5))+ 32 (przy przeliczanniu skali Celsjusza na skalę Fahrenheita). Napisz dwie funkcje do przeliczania
# temperatur między poszczególnymi skalami.
# Sporządź dla powyższej funkcji dokumentację

def fahrenheitToCelsius(temp_in_fahrenheit:float) -> float:
    """
    Function returns temperature in celsius.
    
    Args:
        temp_in_fahrenheit (float): temperature in fahrenheit degrees to be
        converted to celsius.
    
    Returns:
        (float): temperature in celsius degrees 
    """
    return (temp_in_fahrenheit - 32) * (5 / 9)

def celsiusToFahrenheit(temp_in_celsius:float) -> float:
    """
    Function returns temperature in celsius.
    
    Args:
        temp_in_celsius (float): temperature in celsius degrees to be
        converted to fahrenheit.
    
    Returns:
        (float): temperature in fahrenheit degrees 
    """
    return (temp_in_celsius * (9 / 5)) + 32

if __name__ == '__main__':
    assert celsiusToFahrenheit(0) == 32
    assert celsiusToFahrenheit(24) == 75.2
    assert celsiusToFahrenheit(100) == 212
    assert round(fahrenheitToCelsius(0)) == round(-17.7778)
    assert round(fahrenheitToCelsius(24)) == round(-4.44444)
    assert round(fahrenheitToCelsius(100)) == round(37.7778)
