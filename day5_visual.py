import matplotlib.pyplot as plt

students = ["Meghana", "Ravi", "Anu"]
marks = [90, 85, 95]

plt.bar(students, marks, color="skyblue")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()