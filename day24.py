# Day 24 - Decision Trees with Scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Sample dataset: Weather and Play decision
data = {
    "Weather": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny", "Sunny", "Rain"],
    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild"],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

# Convert categorical data to numbers
df_encoded = pd.get_dummies(df[["Weather", "Temperature"]])
X = df_encoded
y = df["Play"].map({"No": 0, "Yes": 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Plot Decision Tree
plt.figure(figsize=(8, 5))
plot_tree(model, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.show()