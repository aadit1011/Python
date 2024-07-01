# Using filter function
import numpy as np 

# Initialize the array
arr = np.array([1, 2, 3, 4, 5, 6])

# Initialize the filter with Boolean values
f = [True, False, True, True, True, False]

# Apply the filter to the array
var = arr[f]  

# Print the filtered array
print(var)
print()

# Using where function to search element in an array
# Find the index of the element with value 5
search = np.where(arr == 5)

# Find the index of the element with value 3
search2 = np.where(arr == 3)

# Print the indices where the elements are found
print()
print(search)
print()
print(search2)
print()

# Using searchsorted function
# Initialize another array
arr1 = np.array([70, 80, 10, 15, 9, 8, 7, 5, 1, 2, 4, 50])

# Sort the array
sor = np.sort(arr1)

# Print the sorted array
print()
print(sor) 
print()

# Find the index where the value 25 would fit into the sorted array
sort = np.searchsorted(sor, 25, side="left")

# Print the index where 25 would fit in the sorted array
print(sort) 
