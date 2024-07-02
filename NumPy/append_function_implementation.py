import numpy as np 

# Define the original arrays
array = np.array([[1, 2, 3, 4, 5, 6],
                  [7, 8, 9, 10, 11, 12]])

array2 = np.array([[13, 14, 15, 16, 17, 18],
                   [19, 20, 21, 22, 23, 24]])

# Append along axis 0
axis0 = np.append(array, array2, axis=0)

# Append along axis 1
axis1 = np.append(array, array2, axis=1)

# Print the original array
print()
print(f'Original array =\n{array}')
print()
print()

# Print the appended arrays
print(f'The appended value along axis 0 is =\n{axis0}')
print()
print()
print(f'The appended value along axis 1 is =\n{axis1}')
print()
print()
