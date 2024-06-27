import numpy as np  # Importing the NumPy library

# Creating an array of characters
arr = np.array(['s', 'h', 'a', 'r', 'm', 'a'])

# Sorting the array in alphabetical order
arr_sorted = np.sort(arr)
print('Sorted array:', arr_sorted)

# Creating an array of integers
arr1 = np.array([1, 2, 3, 4, 5, 6])

# Splitting the array into 3 equal parts
arr_a, arr_b, arr_c = np.array_split(arr1, 3)

# Printing each part of the split array
print()
print('First part of the split array:', arr_a)
print()
print('Second part of the split array:', arr_b)
print()
print('Third part of the split array:', arr_c)
