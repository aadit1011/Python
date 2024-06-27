import numpy as np

# Creating the first 1D array
arr_a = np.array([1, 2, 3, 4, 5])

# Creating the second 1D array
arr_b = np.array([6, 7, 8, 9, 10])

# Stacking arr_a and arr_b along the second axis (axis=1)
# This stacks the arrays column-wise, resulting in a 2D array with shape (5, 2)
arr1 = np.stack((arr_a, arr_b), axis=1)

# Stacking arr_a and arr_b along the first axis (axis=0)
# This stacks the arrays row-wise, resulting in a 2D array with shape (2, 5)
arr2 = np.stack((arr_a, arr_b), axis=0)

# Vertically stacking arr_a and arr_b
# This is equivalent to stacking along the first axis, resulting in a 2D array with shape (2, 5)
arr3 = np.vstack((arr_a, arr_b))

# Horizontally stacking arr_a and arr_b
# This concatenates the arrays along the second axis, resulting in a 1D array with shape (10,)
arr4 = np.hstack((arr_a, arr_b))

# Printing the original arrays
print('Array a:')
print(arr_a)
print()
print('Array b:')
print(arr_b)
print()

# Printing the stacked arrays
print('Stacked along axis=1 (column-wise):')
print(arr1)
print()
print('Stacked along axis=0 (row-wise):')
print(arr2)
print()
print('Vertically stacked:')
print(arr3)
print()
print('Horizontally stacked:')
print(arr4)
print()
