# Day 23 - Logistic Regression with Scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset: Hours studied & Pass/Fail
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Splitting data into features (X) and target (y)
X = df[["Hours"]]
y = df["Pass"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Example prediction
sample_hours = [[4.5]]
predicted_class = model.predict(sample_hours)[0]
print("\nPredicted result for 4.5 hours of study:", "Pass" if predicted_class == 1 else "Fail")