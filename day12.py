# Day 12 - Python Exceptions (Error Handling)

# Basic try-except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Handling multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Finally block
try:
    print("Trying something risky...")
    x = 10 / 0
except ZeroDivisionError:
    print("Oops! Can't divide by zero.")
finally:
    print("This will always run, error or not.")