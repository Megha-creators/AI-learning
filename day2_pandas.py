import pandas as pd

data = {"Name": ["Meghana", "Ravi", "Anu"], "Marks": [90, 85, 95]}
df = pd.DataFrame(data)
print(df)

print("Average Marks:", df["Marks"].mean())