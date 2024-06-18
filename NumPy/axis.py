import numpy as np;

# Create a 2D numpy array with specified elements
arr = np.array([[1, 2, 3, 4, -1, -2], [4, 5, 6, 7, 10, 14]]);

# Print the original array
print(arr);
print();

# Find the minimum value along each row (axis=1)
z = np.min(arr, axis=1);
print(z);  # Print the minimum values for each row
print();

# Find the minimum value along each column (axis=0)
z1 = np.min(arr, axis=0);
print(z1);  # Print the minimum values for each column
print();

# Find the maximum value along each row (axis=1)
p = np.max(arr, axis=1);
print(p);  # Print the maximum values for each row
print();

# Find the maximum value along each column (axis=0)
p1 = np.max(arr, axis=0);
print(p1);  # Print the maximum values for each column

# Get the size of one array element in bytes
siz = arr.itemsize;
print(siz);  # Print the size of one array element in bytes
