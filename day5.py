# Day 5 - Python Dictionaries

# Creating a dictionary
student = {
    "name": "Meghana",
    "age": 18,
    "course": "BCA",
    "goal": "AI Engineer"
}

# Printing dictionary
print("Student Info:", student)

# Accessing values
print("Name:", student["name"])
print("Course:", student.get("course"))

# Adding new key-value pair
student["college"] = "Osmania University"
print("After adding college:", student)

# Updating values
student["goal"] = "Data Scientist"
print("After updating goal:", student)

# Removing a key-value pair
student.pop("age")
print("After removing age:", student)

# Looping through dictionary
print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# Length of dictionary
print("Number of items in dictionary:", len(student))