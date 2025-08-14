# Day 17 - Matplotlib Basics

import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Simple Line Plot
plt.plot(x, y, label="Line Graph", color="blue", marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart
categories = ["A", "B", "C", "D"]
values = [4, 7, 1, 8]

plt.bar(categories, values, color="orange")
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()

# Pie Chart
sizes = [40, 30, 20, 10]
labels = ["Python", "Java", "C++", "Others"]
colors = ["skyblue", "lightgreen", "lightcoral", "gold"]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("Programming Language Usage")
plt.show()