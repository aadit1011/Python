import numpy as np
import pandas as pd

# Reading the CSV file into a DataFrame
file = pd.read_csv('data.csv')

# Displaying information about the DataFrame, including the data types and non-null counts
file.info()

# Printing the number of columns in the DataFrame
print(f'The number of columns in the data set is: {len(file.columns)}')

# To check whether there are any null values in the given dataset or not
null_values = file.isnull()  # This will return a DataFrame of the same shape as `file` with boolean values indicating whether the data is null or not
print(null_values)

# Checking if any column contains null values
nul = null_values.any()  # This will return a Series indicating if any column contains null values
print(nul)

# Filling the null values with 'Aadit'
filled = file.fillna('Aadit')  # This will replace all the NaN values in the DataFrame with the string 'Aadit'
print(filled)
