# Day 11 - Python Modules & Libraries

# Importing built-in modules
import math
import random

# Using math module
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Pi value:", math.pi)

# Using random module
print("\nRandom number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(["AI", "Python", "Data Science"]))

# Importing custom module
# Let's create a small custom module in the same directory

# Save this code below in a file called mymodule.py:
# def welcome(name):
#     return f"Welcome {name} to Python learning!"

# Then import it like this:
# import mymodule
# print(mymodule.welcome("Meghana"))