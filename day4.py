# Day 4 - Python Lists

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Printing the whole list
print("Fruits List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("orange")
print("After adding orange:", fruits)

# Inserting elements
fruits.insert(1, "grape")
print("After inserting grape at index 1:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing banana:", fruits)

# Popping elements
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("List after pop:", fruits)

# Changing an element
fruits[0] = "watermelon"
print("After changing first fruit:", fruits)

# Looping through a list
print("List of fruits:")
for fruit in fruits:
    print(fruit)

# Length of list
print("Number of fruits:", len(fruits))