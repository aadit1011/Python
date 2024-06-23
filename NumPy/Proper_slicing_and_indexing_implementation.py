import numpy as np
#INDEXING
# Indexing 1D array
print('Indexing 1D array')
# Generating a 1D array with 5 random integers between 1 and 20
arr = np.random.randint(1, 20, size=5)
print(arr)
print()

# Accessing the first element
print('First element:', arr[0])

# Finding the length of the array
l = len(arr)

# Accessing the first element using negative indexing
print('First element using negative indexing:', arr[-l])
print()

# Accessing the last element using positive and negative indexing
print('Last element using positive indexing:', arr[l-1])
print('Last element using negative indexing:', arr[-1])
print()

# Indexing 2D array
print('Indexing 2D array')
# Creating a 2D array
arr2d = np.array([[1, 2, 3], [5, 6, 7]])
print(arr2d)
print()

# Accessing elements in the 2D array
print('Element at (0, 0):', arr2d[0][0])
print('Element at (0, 2):', arr2d[0][2])
print('Last element in the first row:', arr2d[0][-1])
print()

# Indexing 3D array
print('Indexing 3D array')
# Creating a 3D array
arr3d = np.array([[[1, 2, 3], [4, 5, 7]], [[8, 9, 10], [11, 12, 13]]])
print(arr3d)
print()

# Accessing elements in the 3D array
print('Element at (0, 0, 0):', arr3d[0][0][0])
print('Last element in the first subarray, first row:', arr3d[0][0][-1])
print('Element at (0, 0, 0) using comma-separated indexing:', arr3d[0, 0, 0])

#SLICING
# Slicing 1-dimensional array
print('Slicing 1-dimensional array')

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Slicing the array from index 0 to 6
print('Slice from 1 to 7 is:', arr1[0:7])
print()

# Slicing the array from index 0 to 6 with a step of 2
print('Slice from 1 to 7 including 2 steps:', arr1[0:7:2])
print()

# Slicing 2-dimensional array
print('Slicing 2-dimensional array')
print()

# Creating a 2D array
arr2 = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

# Slicing the first row from index 0 to 3
print('Slice of 2-dimensional array from 1 to 4 is:', arr2[0][0:4])
print()

# Slicing the second row from index 0 to 3
print('Slice of 2-dimensional array from 6 to 9 is:', arr2[1][0:4])
print()

# Slicing the first row from index 0 to 3 with a step of 2
print('Slice of 2-dimensional array from 1 to 4 taking steps 2 is:', arr2[0][0:4:2])
print()

# Slicing the second row from index 0 to 3 with a step of 2
print('Slice of 2-dimensional array from 6 to 9 taking steps 2 is:', arr2[1][0:4:2])
print()

# Slicing 3-dimensional array
print('Slicing 3-dimensional array')
print()

# Creating a 3D array
arr3 = np.array([[[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]]])

# Printing the 3D array
print(arr3)
print()

# Slicing the first subarray, first row from index 0 to 3
print('Slice of 3-dimensional array from 1 to 4 is:', arr3[0][0][0:4])
print()

# Slicing the first subarray, second row from index 0 to 3
print('Slice of 3-dimensional array from 6 to 9 is:', arr3[0][1][0:4])
print()

# Slicing the first subarray, first row from index 0 to 3 with a step of 2
print('Slice of 3-dimensional array from 1 to 4 taking steps 2 is:', arr3[0][0][0:4:2])
print()

# Slicing the first subarray, second row from index 0 to 3 with a step of 2
print('Slice of 3-dimensional array from 6 to 9 taking steps 2 is:', arr3[0][1][0:4:2])
print()

# Slicing the second subarray, first row from index 0 to 3
print('Slice of 3-dimensional array from 11 to 14 is:', arr3[1][0][0:4])
print()

# Slicing the second subarray, second row from index 0 to 3
print('Slice of 3-dimensional array from 16 to 19 is:', arr3[1][1][0:4])
print()

# Slicing the second subarray, first row from index 0 to 3 with a step of 2
print('Slice of 3-dimensional array from 16 to 19 taking steps 2 is:', arr3[1][0][0:4:2])
print()

# Slicing the second subarray, second row from index 0 to 3 with a step of 2
print('Slice of 3-dimensional array from 16 to 19 taking steps 2 is:', arr3[1][1][0:4:2])
