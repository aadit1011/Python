# Importing necessary libraries
import numpy as np 
import pandas as pd 

# Reading the entire CSV file into a DataFrame
file = pd.read_csv('mt_everest.csv')

# Displaying the entire DataFrame
print("Entire DataFrame:\n", file)

# Reading the first 3 rows of the CSV file into a DataFrame
file2 = pd.read_csv('mt_everest.csv', nrows=3)

# Displaying the DataFrame containing the first 3 rows
print("\nFirst 3 Rows of DataFrame:\n", file2)

# Reading specific columns ('NAME' and 'COUNTRY') from the CSV file into a DataFrame
file3 = pd.read_csv('mt_everest.csv', usecols=['NAME', 'COUNTRY'])

# Displaying the DataFrame containing only the 'NAME' and 'COUNTRY' columns
print("\nDataFrame with 'NAME' and 'COUNTRY' columns:\n", file3)

# Reading specific columns (by index) and skipping the first 2 rows from the CSV file into a DataFrame
file4 = pd.read_csv('mt_everest.csv', usecols=[0, 1, 2, 3], skiprows=2)

# Displaying the DataFrame with specific columns and skipped rows
print("\nDataFrame with specific columns and skipped rows:\n", file4)

# Reading the CSV file with 'NAME', 'COUNTRY', and 'YEAR' as index columns
fil = pd.read_csv('mt_everest.csv', index_col=['NAME', 'COUNTRY', 'YEAR'])

# Displaying the DataFrame with multi-index columns
print("\nDataFrame with 'NAME', 'COUNTRY', and 'YEAR' as index columns:\n", fil)

# Reading the CSV file starting from the 3rd header row
rd = pd.read_csv('mt_everest.csv', header=2)

# Displaying the DataFrame starting from the 3rd header row
print("\nDataFrame starting from the 3rd header row:\n", rd)

# Reading the CSV file with custom column names
rd2 = pd.read_csv('mt_everest.csv', names=['col1', 'col2', 'col3']) 

# Displaying the DataFrame with custom column names
print("\nDataFrame with custom column names:\n", rd2)
