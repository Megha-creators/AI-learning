# Day 20 - Seaborn Basics

import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
df = sns.load_dataset("iris")

# Display first 5 rows
print(df.head())

# Scatter plot
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
plt.title("Sepal Length vs Width")
plt.show()

# Histogram
sns.histplot(data=df, x="petal_length", bins=20, kde=True)
plt.title("Petal Length Distribution")
plt.show()

# Box plot
sns.boxplot(data=df, x="species", y="petal_width")
plt.title("Petal Width by Species")
plt.show()

# Pair plot
sns.pairplot(df, hue="species")
plt.show()