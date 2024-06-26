import numpy as np

# Create the first 2x2 array
arr1 = np.array([[1, 2], [3, 4]])

# Create the second 2x2 array
arr2 = np.array([[6, 7], [8, 9]])

# Concatenate arr1 and arr2 along the default axis (axis=0)
# This stacks the arrays vertically (row-wise)
arr = np.concatenate((arr1, arr2))
print('Concatenated array along the default axis (axis=0):')
print(arr)
print()

# Concatenate arr1 and arr2 along axis=1
# This stacks the arrays horizontally (column-wise)
arr_axis = np.concatenate((arr1, arr2), axis=1)
print('Concatenated array along axis=1 (horizontal stacking):')
print(arr_axis)
print()

# Concatenate arr1 and arr2 along axis=0
# This is the same as the default behavior, stacking the arrays vertically (row-wise)
arr_axis2 = np.concatenate((arr1, arr2), axis=0)
print('Concatenated array along axis=0 (vertical stacking):')
print(arr_axis2)
