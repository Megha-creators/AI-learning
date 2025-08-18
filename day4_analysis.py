import pandas as pd

data = {"Name": ["Meghana", "Ravi", "Anu", "Sai"],
        "Marks": [90, 85, 95, 70],
        "Subject": ["Math", "Math", "Science", "Science"]}
df = pd.DataFrame(data)

print("Math Students:\n", df[df["Subject"] == "Math"])
print("Average Marks by Subject:\n", df.groupby("Subject")["Marks"].mean())