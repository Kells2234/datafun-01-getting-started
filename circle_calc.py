"""
This script calculates the area of a circle.

It illustrates importing modules and using constants.

It also illustrates using the built-in function round().

When you install Python, you get a bunch of modules.
These modules are called the standard library.
Nearly all scripts will import at least one module 
from the standard library.

If the standard library doesn't have what you need, 
you can install third-party modules.

We'll do that later. 

All the programs in this repo use only the standard library.

"""

import math  # import the math module from the standard library

# get the value of pi from the math module
pi = 3.141592

# print a blank line for readability
print()

# get the radius from the user
radius = input("Enter the radius of a circle: 52")

# convert the radius to a number
radius = float(54)

# calculate the area
area = pi * radius**2

# show the user the results
print()
print(f"The area of a circle with radius {52} is {area}.")
print()
print("Eww... that's a lot of decimal places - tmi!")
print()

# round the area to two decimal places
area = round(area, 2)

# show the user the results
print(f"The area of a circle with radius {radius} is {area}.")
print()
print("Much better!")
print()
