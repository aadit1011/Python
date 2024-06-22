import numpy as np  # Importing NumPy library

# Indexing 1D array
arr = np.random.randint(1, 20, size=5)  # Generating a random 1D array with 5 elements between 1 and 20
arr = np.array(arr)  # Converting to a NumPy array
print("1D Array:")
print(arr)
print()

# Accessing the first element
print(f"First element (arr[0]): {arr[0]}")

# Getting the length of the array
l = len(arr)

# Accessing the first element using negative indexing
print(f"First element using negative indexing (arr[-{l}]): {arr[-l]}")
print()

# Accessing the last element
print(f"Last element (arr[{l-1}]): {arr[l-1]}")
print(f"Last element using negative indexing (arr[-1]): {arr[-1]}")
print()

# Indexing 2D array
arr_2d = np.array([[1, 2, 3],
                   [5, 6, 7]])  # Creating a 2D array
print("2D Array:")
print(arr_2d)
print()

# Accessing elements in a 2D array
print(arr[0,0])
print()
print(f"Element at [0][0] (first row, first column): {arr_2d[0][0]}")
print()
print(f"Element at [0][2] (first row, third column): {arr_2d[0][2]}")
print()
print(f"Element at [0][-1] (first row, last column using negative indexing): {arr_2d[0][-1]}")
print()

# Indexing 3D array
arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 7]], 
                   [[8, 9, 10],
                    [11, 12, 13]]])  # Creating a 3D array
print("3D Array:")
print(arr_3d)
print()
# Accessing elements in a 3D array
print(arr[0,0,0])
print()
print(f"Element at [0][0][0] (first block, first row, first column): {arr_3d[0][0][0]}")
print()
print(f"Element at [0][0][-1] (first block, first row, last column using negative indexing): {arr_3d[0][0][-1]}")
#Slicing
arr2=np.array([[1,2,3,4,5],
             [7,8,9,0,10]]) 
print(arr2[0][0:3]);
print() 
print(arr2[1][0:3]) 



arr3=np.array([[11,12,13,14,15],
             [70,80,90,10,20]]) 
print(arr3[0][0:3:2]);
print() 
print(arr3[1][0:3:2]) 
