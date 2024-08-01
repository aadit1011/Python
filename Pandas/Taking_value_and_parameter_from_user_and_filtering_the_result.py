import pandas as pd
import numpy as np

# Reading the CSV file into a DataFrame
file = pd.read_csv('data.csv')

# Displaying the original DataFrame
print("Original DataFrame:")
print(file)

# Displaying the column names of the DataFrame
print("\nThe columns given in this data set are:")
print(file.columns.to_list())  # Correct way to display column names as a list

# Prompting the user to select the required column for filtering
print("\nFrom all of the above, select the required one:")

# Loop until a valid column name is provided
while True:
    parameter = input('Please enter the parameter through which you want to filter row: ')
    if parameter in file.columns:
        break
    else:
        print(f"Column '{parameter}' not found in the DataFrame. Please try again.")

# Taking user input for the value to filter by (assuming the value to be float)
value = float(input('Please Enter the value for the above parameter: '))

# Filtering the DataFrame based on the user input
# Here, file[parameter] == value creates a boolean series for the condition
result = file[file[parameter] == value]

# Checking if the filtered result is empty
if result.empty:
    print(f"No rows found with {parameter} equal to {value}.")
else:
    # Displaying the filtered result
    print("\nThe searched result:")
    print(result)
