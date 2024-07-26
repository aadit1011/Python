import numpy as np
import pandas as pd

# Reading the CSV file into a DataFrame
file = pd.read_csv('climate.csv')

# Displaying the DataFrame to inspect the data
print(file)

# Asking the user for the number of rows to display from the top and the bottom
first = int(input('Enter the total number of rows to display from the top='))
last = int(input('Enter the total number of rows to display from the bottom='))

# Displaying the first 'first' rows as per user input
print(f'The first {first} rows are------')
print()
fir = file.head(first)
fir = pd.DataFrame(fir)
print(fir)
print('And their description is---------')
print(fir.describe())
print()

# Displaying the last 'last' rows as per user input
las = file.tail(last)
las = pd.DataFrame(las)
print(f'The last {last} rows are------')
print()
print(las)
print('And their description is-------')
print(las.describe())

# Finding and displaying the shape of the DataFrame (number of rows and columns)
print('Shape of the DataFrame:')
print(file.shape)

# Displaying detailed information about the DataFrame including column data types and non-null values
print('Detailed information about the DataFrame:')
print(file.info())
