import pandas as pd  # Importing pandas library for data manipulation
import numpy as np  # Importing numpy library for numerical operations

# Defining a dictionary to create a DataFrame
data = {
    'A': [1, 2, 3],  # Column A
    'B': [4, 5, 6],  # Column B
    'C': [7, 8, 9]   # Column C
}

# Creating a DataFrame from the dictionary
df = pd.DataFrame(data)
print(df)  # Displaying the DataFrame

# Accessing elements using iloc (integer-location based indexing)
print(df.iloc[1:, 1:])  # Accessing elements starting from row 1 and column 1
print() 

# Accessing elements using loc (label-location based indexing)
print(df.loc[1:, 'B':])  # Accessing elements starting from row 1 and column 'B'

# Accessing single element (value 6) using iloc
print(df.iloc[2, 1])  # Accessing the element at row 2, column 1
print() 

# Accessing single element (value 6) using loc
print(df.loc[2, 'B'])  # Accessing the element at row 2, column 'B'

# Accessing entire row (3, 6, 9) using iloc
print(df.iloc[2, 0:])  # Accessing the row at index 2
print() 

# Accessing entire row (3, 6, 9) using loc
print(df.loc[2, 'A':])  # Accessing the row at index 2

# Accessing subset of DataFrame (147 and 258) using iloc
print(df.iloc[0:2, 0:])  # Accessing the first two rows and all columns
print()  

# Accessing subset of DataFrame (147 and 258) using loc
print(df.loc[0:1, 'A':])  # Accessing rows 0 and 1, and all columns

# Creating two Series with different lengths
ser1 = pd.Series(156, index=[1, 2, 3, 4, 5, 6, 7])
ser2 = pd.Series(156, index=[1, 2, 3, 4])

# Adding the Series together, resulting in missing values being handled
ser = ser1 + ser2
print(f'Now printing the addition of \n\n{ser1} and \n\n{ser2} is =\n\n{ser}')
print()  

# Creating a dictionary with information
info = {
    'name': ['Aadit Sharma', 'Tom Cruise', 'Carl Runefelt', 'Akshay Kumar'],
    'Phone Number': [98283283, 98243938, 93284834, 9384934],
    'Address': ['Dubai', 'USA', 'Dubai', 'India']
}

# Creating a Series from the dictionary
inf = pd.Series(info)
print(inf)  # Displaying the Series

# Creating a NumPy array
arr1 = np.array([1, 2, 3, 4, 5])

# Converting the NumPy array to a Pandas Series with custom index
ser = pd.Series(arr1, index=['a', 'b', 'c', 'd', 'e'])
print()
print(ser)  # Displaying the Series

# Changing the data type of the Series
arr_new = pd.Series(arr1, index=['s', 't', 'u', 'v', 'w'], dtype=float, name='array1')
print()
print(arr_new)  # Displaying the Series with float data type

# Changing the data type to string
arr_new1 = pd.Series(arr1, index=['s', 't', 'u', 'v', 'w'], dtype=str)
print()
print(arr_new1)  # Displaying the Series with string data type

# Creating a Series from a character array
ar = np.array(['A', 'a', 'd', 'i', 't', 'S', 'h', 'a', 'r', 'm', 'a'])
arn = pd.Series(ar, index=['A', 'a', 'd', 'i', 't', 'S', 'h', 'a', 'r', 'm', 'a'], name='My Identity')
print()
print(arn)  # Displaying the character Series

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Converting the NumPy array to a Pandas Series
pan = pd.Series(arr)
print('Array of data.........')
print()
print(arr)  # Displaying the NumPy array

print()
print('Converting it into the Series Data Structure.......')
print()
print(pan)  # Displaying the Series

# Defining a dictionary to create a DataFrame
datas = {
    'Name': ['Aadit Sharma', 'Carl Runefelt', 'Joe Dispenza'],
    'Roll': [7, 8, 9],
    'Address': ['Dubai', 'Abu Dhabi', 'USA']
}

# Creating a DataFrame from the dictionary
data = pd.DataFrame(datas)
print(data)  # Displaying the DataFrame

print()
print('.....................Address........................')
print()
print(data['Address'])  # Displaying the Address column

print()
print('.....................Name.............................')
print()
print(data['Name'])  # Displaying the Name column

print()
print('......................Roll Number......................')
print()
print(data['Roll'])  # Displaying the Roll column
