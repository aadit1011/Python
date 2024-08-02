import pandas as pd 
import numpy as np 

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('data.csv')

# Initialize empty lists to store row and column indices to be displayed
row = []
col = []

# Get a list of all column names in the dataset for validation
match = data.columns.to_list()

# Prompt the user to enter the number of rows they want to display
nrow = int(input('Enter the total number of rows you want to display: '))
for i in range(nrow):
    print()
    # Prompt the user to enter the row index they want to display
    val = int(input(f'Enter the row number index you want to display ({i+1}/{nrow}): '))
    row.append(val)

print()

# Prompt the user to enter the number of columns they want to display
ncol = int(input('Enter the total number of columns you want to display: '))
for i in range(ncol):
    a = True
    while a:
        # Prompt the user to enter the column name they want to display
        val = input(f'Enter the name of the column you want to display ({i+1}/{ncol}): ')
        if val in match:
            # If the entered column name is valid, exit the loop
            a = False
        else:
            # If the entered column name is invalid, prompt the user to try again
            print()
            print('Invalid column name. Please enter a correct column name. Try again...')
            print()
    col.append(val)

# Use the .loc method to select the specified rows and columns from the DataFrame
data_set = data.loc[row, col]

# Display the selected subset of the DataFrame
print(data_set)
