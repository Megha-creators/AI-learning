# Day 26 - Support Vector Machines (SVM) with Scikit-learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create SVM model
model = SVC(kernel='linear')  # You can also use 'rbf', 'poly'
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Example prediction
sample = [[6.0, 2.9, 4.5, 1.5]]
predicted_class = model.predict(sample)[0]
print("Predicted Class:", iris.target_names[predicted_class])