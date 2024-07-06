import numpy as np  # Import NumPy for numerical operations

# Create two NumPy arrays with integer elements
arr1 = np.array([1, 2, 3, 4, 5, 12])
arr2 = np.array([12, 13, 14, 15, 16, 17])

# Perform element-wise comparison: Check if elements in arr1 are greater than elements in arr2
comp = arr1 > arr2

# Perform element-wise comparison: Check if elements in arr1 are less than elements in arr2
comp2 = arr1 < arr2 

# Use np.any() to check if any element in arr1 is greater than the corresponding element in arr2
comp = np.any(arr1 > arr2)

# Use np.all() to check if all elements in arr1 are less than the corresponding elements in arr2
comp2 = np.all(arr1 < arr2)

# Print the result of np.any() comparison
print(comp)  # This will print True if any element in arr1 is greater than the corresponding element in arr2

# Print the result of np.all() comparison
print(comp2)  # This will print True if all elements in arr1 are less than the corresponding elements in arr2
