import pandas as pd 
import numpy as np 

# Reading the CSV file into a DataFrame
read = pd.read_csv('climate.csv')

# Printing the entire DataFrame to inspect the data
print(read)

# Checking the indexing details of the DataFrame
print(read.index)

# Printing column details
print('Columns Details.....')
print(read.columns)

# Generating and printing descriptive statistics for the DataFrame
print(read.describe())

# Note: 'read.describe' will just print a reference to the method, not its output. Use 'read.describe()' instead.
print(read.describe())
