# Day 22 - Linear Regression with Scikit-learn

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample dataset: Study Hours vs Marks
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 85]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Splitting into X (features) and y (target)
X = df[["Hours"]]  # Independent variable
y = df["Marks"]    # Dependent variable

# Creating and training the model
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted_marks = model.predict([[7]])
print("\nPredicted Marks for 7 study hours:", predicted_marks[0])

# Plotting the regression line
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks - Linear Regression")
plt.legend()
plt.show()