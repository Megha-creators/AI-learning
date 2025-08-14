# Day 13 - Advanced Python Lists

# List comprehension - creating a list from 1 to 10
numbers = [x for x in range(1, 11)]
print("Numbers 1-10:", numbers)

# List comprehension with condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Nested list comprehension (multiplication table)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table (1 to 5):", table)

# Sorting a list
fruits = ["banana", "apple", "mango", "cherry"]
fruits.sort()
print("Sorted fruits:", fruits)

# Sorting in reverse
fruits.sort(reverse=True)
print("Reverse sorted fruits:", fruits)

# Sorting by key length
fruits.sort(key=len)
print("Sorted by length:", fruits)

# Filtering a list
numbers = [5, 10, 15, 20, 25]
filtered = list(filter(lambda x: x > 10, numbers))
print("Numbers greater than 10:", filtered)