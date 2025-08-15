# Day 30 - Iris Flower Prediction AI Project

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "iris_model.pkl")
print("Model saved as iris_model.pkl")

# Example prediction
sample = [[5.1, 3.5, 1.4, 0.2]]
predicted_class = model.predict(sample)[0]
print("Predicted Class:", iris.target_names[predicted_class])