import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv("student_data.csv")

print("📊 Student Data:\n", df)

# Average marks
print("\nAverage Marks:", df["Marks"].mean())

# Highest scorer
highest = df.loc[df["Marks"].idxmax()]
print("\nHighest Scorer:", highest["Name"], "with", highest["Marks"], "marks")

# Subject-wise performance
print("\nSubject-wise Average:\n", df.groupby("Subject")["Marks"].mean())

# Visualization
plt.bar(df["Name"], df["Marks"], color="skyblue")
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()