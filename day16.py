# Day 16 - Pandas Basics

import pandas as pd

# Creating a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:")
print(series)

# Creating a DataFrame from dictionary
data_dict = {
    "Name": ["Meghana", "Rahul", "Anita"],
    "Age": [18, 20, 22],
    "Course": ["BCA", "B.Tech", "MBA"]
}
df = pd.DataFrame(data_dict)
print("\nDataFrame:")
print(df)

# Reading data from CSV (example.csv should exist in the same folder)
# df_from_csv = pd.read_csv("example.csv")
# print("\nData from CSV:")
# print(df_from_csv)

# Accessing columns
print("\nNames Column:")
print(df["Name"])

# Accessing rows
print("\nFirst Row:")
print(df.loc[0])

# Adding a new column
df["Marks"] = [85, 90, 88]
print("\nDataFrame with Marks column:")
print(df)

# Filtering data
filtered_df = df[df["Marks"] > 85]
print("\nStudents with marks > 85:")
print(filtered_df)