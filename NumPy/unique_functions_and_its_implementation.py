import numpy as np 

# Create an array with some duplicate values
arr = np.array([1, 2, 3, 4, 5, 5, 5, 1, 1, 2, 3, 4, 6, 7, 7, 7, 8, 8, 8, 9, 6, 5, 3, 2, 2, 62])

# Get the unique values in the array and their first occurrence indices
index = np.unique(arr, return_index=True)

# Get the unique values in the array and the indices to reconstruct the original array
reverse = np.unique(arr, return_inverse=True)

# Get the unique values in the array and their counts
count = np.unique(arr, return_counts=True)

# Print the original array
print(f'Original Array={arr}')
print()

# Print the unique values and their first occurrence indices
print(f'Indexed value={index}')
print()

# Print the unique values and the indices to reconstruct the original array
print(f'Reversed value={reverse}')
print()

# Print the unique values and their counts
print(f'Count value={count}')
print()
