import numpy as np  # Import the numpy library for numerical operations

# Generate a 3x4 array with random values between 0 and 1
array = np.random.random((3, 4)) 
print("Original 3x4 array with random values:")
print(array) 
print()

# Reverse the array along all axes
rev = np.flip(array)
print("Reversed array (flip along all axes):")
print(rev)
print()

# Define a 2-dimensional array
arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8]])
print("Original 2D array:")
print(arr2)
print()

# Reverse the 2-dimensional array along all axes
print("Reversed 2D array (flip along all axes):")
print(np.flip(arr2)) 
print()

# Generate a 1-dimensional array with 9 random integers between 0 and 20
arr_rand = np.random.randint(0, 20, size=9)
# Reshape the 1-dimensional array to a 3-dimensional array with minimum 3 dimensions
arr_rand = np.array(arr_rand, ndmin=3)
print("Random 1D array reshaped to 3D (ndmin=3):")
print(arr_rand)
print()

# Correctly reshape the array to a specific 3D shape (1, 3, 3)
arr_rand = np.reshape(arr_rand, (1, 3, 3))
print("Reshaped array to shape (1, 3, 3):")
print(arr_rand) 
