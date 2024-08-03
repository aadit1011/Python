# Importing necessary libraries
import pandas as pd
import numpy as np

# Reading the CSV file into a pandas DataFrame
data = pd.read_csv('data.csv')

# Display the entire DataFrame
print("Displaying the entire DataFrame:")
print(data)
print()

# Displaying a specific element in the DataFrame using iloc
# iloc is used to select by row and column indices (0-based indexing)
# Here, we select the element at the first row and first column
print("Element at the first row and first column (0,0):")
print(data.iloc[0, 0])
print()

# Displaying specific rows and columns using iloc
# iloc[[row_indices], [column_indices]] allows us to select specific rows and columns by their indices
# Here, we select rows 0 to 6 and columns 1, 2, 3, 4, 5, and 0
print("Displaying rows 0 to 6 and columns 1, 2, 3, 4, 5, and 0:")
print(data.iloc[[0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 0]])
print()

# Displaying a single column using iloc
# Here, we select the first column and all its rows
print("Displaying the first column (all rows):")
print(data.iloc[:, 0])
print()

# Displaying multiple columns using iloc
# Here, we select the first three columns and all their rows
print("Displaying the first three columns (all rows):")
print(data.iloc[:, [0, 1, 2]])
print()

# Displaying a single row using iloc
# Here, we select the first row and all its columns
print("Displaying the first row (all columns):")
print(data.iloc[0, :])
print()

# Displaying multiple rows using iloc
# Here, we select the first five rows and all their columns
print("Displaying the first five rows (all columns):")
print(data.iloc[:5, :])
print()

# Displaying a specific range of rows and columns using iloc
# Here, we select rows 2 to 5 and columns 1 to 3
print("Displaying rows 2 to 5 and columns 1 to 3:")
print(data.iloc[2:6, 1:4])
print()

# Displaying data using negative indices with iloc
# Negative indices can be used to select data from the end
# Here, we select the last row and last column
print("Displaying the last row and last column:")
print(data.iloc[-1, -1])
print()

# Displaying every other row using iloc
# Here, we select every other row starting from the first row
print("Displaying every other row (all columns):")
print(data.iloc[::2, :])
print()

# Displaying every other column using iloc
# Here, we select every other column starting from the first column
print("Displaying every other column (all rows):")
print(data.iloc[:, ::2])
print()
