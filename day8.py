# Day 8 - Python Functions

# Basic function
def greet():
    print("Hello, welcome to Python learning!")

# Function with parameters
def greet_person(name):
    print(f"Hello {name}, welcome to Python learning!")

# Function with return value
def add_numbers(a, b):
    return a + b

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

# Calling functions
greet()
greet_person("Meghana")

sum_result = add_numbers(10, 5)
print("Sum:", sum_result)

print("Square of 4:", power(4))
print("4 to the power of 3:", power(4, 3))