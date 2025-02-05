# CS 1101 - Week 11 Videos - SciPy - Exercise 02

import scipy as sp

print(sp.__version__)
print()

# Mathematical Constants
from scipy.constants import pi, golden_ratio

print(f"pi = {pi}")
print(f"Golden Ratio = {golden_ratio}")
radius = 5
print(f"Area = {pi * radius * radius}")
print()

# Physical Constants
from scipy.constants import m_n, Avogadro

print(f"Mass of Neutron : {m_n} Kg")
print(f"Avagadro's Number : {Avogadro}")

from scipy.constants import physical_constants  # Dictionary

print(physical_constants["alpha particle mass"])
for key, value in physical_constants.items():
    print(f"{key} : {value}")
print()

# Conversion Units
from scipy.constants import kilo, yotta

print(kilo)
meters = 800
print(f"In Yotta : {meters / yotta}")

# Conversion Temperature
from scipy.constants import convert_temperature
temperature_in_fahrenheit = 90
temperature_in_celsius = convert_temperature(temperature_in_fahrenheit, 'F', 'C')
print(f"Temperature in Celsius: {temperature_in_celsius}°C")
