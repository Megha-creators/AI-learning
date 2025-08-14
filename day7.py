# Day 7 - Python Loops

# For loop with a list
fruits = ["apple", "banana", "cherry"]
print("Fruit list:")
for fruit in fruits:
    print(fruit)

# For loop with range
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop example
count = 1
print("\nWhile loop counting:")
while count <= 5:
    print("Count is:", count)
    count += 1

# Loop with break
print("\nLoop with break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Loop with continue
print("\nLoop with continue:")
for i in range(6):
    if i == 3:
        continue
    print(i)

# Nested loops
print("\nNested loop example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")