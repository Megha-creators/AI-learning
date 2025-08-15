# Day 21 - Data Cleaning for AI

import pandas as pd

# Sample messy dataset
data = {
    "Name": [" Meghana ", "Rahul", None, "Anita", "Raj"],
    "Age": ["18", "20 years", None, "21", "22"],
    "Marks": ["85", "Ninety", "88", None, "75"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 1: Remove leading/trailing spaces in strings
df["Name"] = df["Name"].astype(str).str.strip()

# Step 2: Fill missing names with "Unknown"
df["Name"].replace("None", "Unknown", inplace=True)
df["Name"].fillna("Unknown", inplace=True)

# Step 3: Clean Age column (extract numbers)
df["Age"] = df["Age"].astype(str).str.extract("(\d+)").astype(float)
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Step 4: Clean Marks column
def convert_marks(value):
    try:
        return float(value)
    except:
        return None

df["Marks"] = df["Marks"].apply(convert_marks)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nCleaned DataFrame:")
print(df)