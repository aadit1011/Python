# Importing the numpy library and assigning it the alias 'np'
import numpy as np;

# Creating a first-dimensional (1D) numpy array
first = np.array([1, 2, 3, 4]);
# Printing the first-dimensional array
print(first);
# Printing the number of dimensions of the first-dimensional array
print(first.ndim);

# Creating a second-dimensional (2D) array using a list of lists
p = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]];
# Converting the list of lists into a 2D numpy array
x = np.array(p);
# Printing the second-dimensional array
print(x);
# Printing the number of dimensions of the second-dimensional array
print(x.ndim);

# Creating a third-dimensional (3D) array using nested lists
y = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [8, 9, 0, 1], [12, 13, 14, 15]]]);
# Printing the third-dimensional array
print(y);
# Printing the number of dimensions of the third-dimensional array
print(y.ndim);
