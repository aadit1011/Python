import numpy as np

# Slicing and Iterating through arrays

# 1-dimensional array
print('for 1-dimensional array')
# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
print(f'Iterating {arr1} elements----')
# Iterating through each element in the 1D array
for a in arr1:
    print(a)
print()

# 2-dimensional array
print('for 2-dimensional array')
# Creating a 2D array
arr2 = np.array([[1, 2, 3, 4, 5, 6],
                 [9, 10, 11, 12, 13, 14]])
# Printing each row of the 2D array
for items in arr2:
    print(items)
print()

# Iterating through each element in the 2D array
for i in arr2:
    print(f"Printing {i} element----")
    for j in i:
        print(j)
print()

# 3-dimensional array
print('Printing 3-dimensional array----')
# Creating a 3D array
arr3 = np.array([[[1, 2, 3, 4, 5, 6],
                  [7, 8, 9, 10, 11, 12]],
                 [[13, 14, 15, 16, 17, 18],
                  [19, 20, 21, 22, 23, 24]],
                 [[25, 26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35, 36]]])
# Iterating through each subarray and element in the 3D array
for b in arr3:
    print(f' Printing {b} elements---')
    for c in b:
        print(f' Printing {c} elements---')
        for d in c:
            print(d)
