# Importing the NumPy library
import numpy as np 

# Using the power function to raise each element of 'arra' to the power of the corresponding element in 'arrb'
arra = np.array([1, 2, 3])
arrb = np.array([4, 5, 6])
array1 = np.power(arra, arrb) 
print(array1)  # Output: [  1  32 729]

# Using the sqrt function to calculate the square root of each element in 'arr1'
arr1 = np.array([4, 16, 64])
array2 = np.sqrt(arr1) 
print(array2)  # Output: [2. 4. 8.]

print()

# Creating 2D arrays 'arr3' and 'arr4'
arr3 = np.array([[2, 2, 2], 
                 [2, 2, 2]])
arr4 = np.array([2, 3, 4])

# Using the power function to raise each element of 'arr3' to the power of the corresponding element in 'arr4'
print(np.power(arr3, arr4))  # Output: [[ 4  8 16] [ 4  8 16]]

# Creating 2D arrays 'arra' and 'arrb'
arra = np.array([[1, 2], 
                 [4, 5]])
arrb = np.array([[12, 13]])

# Using the concatenate function to concatenate 'arra' and 'arrb' along axis 0 (rows)
new = np.concatenate((arra, arrb), axis=0) 
print(new)  # Output: [[ 1  2] [ 4  5] [12 13]]

# Using the transpose function to transpose 'arrb' and then concatenate 'arra' and transposed 'arrb' along axis 1 (columns)
new = np.concatenate((arra, arrb.transpose()), axis=1) 
print(new)  # Output: [[ 1  2 12] [ 4  5 13]]
