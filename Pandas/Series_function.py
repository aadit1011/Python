import pandas as pd  # Importing the pandas library, which is used for data manipulation and analysis.
import numpy as np  # Importing the numpy library, which is used for numerical computations and array operations.

# Creating a NumPy array with elements 1 through 8.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Converting the NumPy array into a pandas Series.
pan = pd.Series(arr)

# Printing a message to indicate the display of the NumPy array.
print('Array of data.........')
print()  # Printing an empty line for better readability.
print() 

# Printing the NumPy array.
print(arr)
print() 
print()  

# Printing a message to indicate the conversion from a NumPy array to a pandas Series.
print('Converting it into the Series Data Structure.......')
print()  

# Printing the pandas Series.
print(pan)
print() 
