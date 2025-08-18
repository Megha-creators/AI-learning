import pandas as pd

data = {"Name": ["Meghana", "Ravi", "Anu", None], "Marks": [90, 85, None, 75]}
df = pd.DataFrame(data)

print("Before Cleaning:\n", df)

# Drop missing values
df = df.dropna()
print("After Cleaning:\n", df)