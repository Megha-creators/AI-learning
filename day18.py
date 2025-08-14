# Day 18 - Data Preprocessing with Pandas

import pandas as pd

# Sample dataset
data = {
    "Name": ["Meghana", "Rahul", "Anita", "Raj", None],
    "Age": [18, 20, None, 21, 22],
    "Marks": [85, 90, 88, None, 75]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Handling missing values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter handling missing values:")
print(df)

# Converting data types
df["Age"] = df["Age"].astype(int)

# Normalizing Marks (0 to 1 scale)
df["Marks_Normalized"] = df["Marks"] / 100

print("\nAfter normalizing marks:")
print(df)

# Filtering data (Marks > 80)
filtered_df = df[df["Marks"] > 80]
print("\nStudents with Marks > 80:")
print(filtered_df)