# Day 29 - K-Means Clustering with Scikit-learn

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data

# Create KMeans model (3 clusters for 3 iris species)
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# Cluster labels
labels = model.labels_
print("Cluster labels:", labels)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering - Iris Dataset")
plt.show()

# Example prediction
sample = [[6.0, 2.9, 4.5, 1.5]]
predicted_cluster = model.predict(sample)[0]
print("Predicted Cluster:", predicted_cluster)