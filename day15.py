# Day 15 - NumPy Basics

import numpy as np

# Creating NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1:", arr1)

# Creating 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Array properties
print("Shape of arr2:", arr2.shape)
print("Data type of arr1:", arr1.dtype)
print("Size of arr1:", arr1.size)

# Array operations
arr3 = np.array([10, 20, 30, 40, 50])
print("Sum of arrays:", arr1 + arr3)
print("Difference of arrays:", arr3 - arr1)
print("Multiply arrays:", arr1 * arr3)

# Scalar operations
print("Array multiplied by 2:", arr1 * 2)

# Useful NumPy functions
print("Zeros array:", np.zeros((2, 3)))
print("Ones array:", np.ones((2, 3)))
print("Random numbers:", np.random.randint(1, 10, size=(3, 3)))

# Indexing and slicing
print("First element of arr1:", arr1[0])
print("First 3 elements of arr1:", arr1[:3])
print("Last 2 elements of arr1:", arr1[-2:])