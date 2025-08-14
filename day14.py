# Day 14 - Tuples and Sets

# ---- Tuples ----
# Creating a tuple
my_tuple = ("apple", "banana", "cherry")
print("Tuple:", my_tuple)

# Accessing elements
print("First fruit:", my_tuple[0])

# Tuples are immutable
# my_tuple[0] = "grape"  # This will give an error

# Tuple unpacking
fruit1, fruit2, fruit3 = my_tuple
print("Unpacked:", fruit1, fruit2, fruit3)

# ---- Sets ----
# Creating a set
my_set = {"apple", "banana", "cherry"}
print("Set:", my_set)

# Adding elements to a set
my_set.add("mango")
print("After adding mango:", my_set)

# Removing elements
my_set.remove("banana")
print("After removing banana:", my_set)

# Sets automatically remove duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Unique numbers set:", numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)