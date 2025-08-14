# Day 9 - Python Classes & Objects

# Creating a class
class Student:
    # Constructor (runs when creating a new object)
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

# Creating objects of Student class
student1 = Student("Meghana", 18, "BCA")
student2 = Student("Rahul", 20, "Computer Science")

# Calling methods
student1.display_info()
print()  # blank line
student2.display_info()