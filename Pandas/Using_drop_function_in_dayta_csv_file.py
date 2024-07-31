import pandas as pd
import numpy as np

# Load the dataset from a CSV file
file = pd.read_csv('data.csv')

# Drop specific columns from the dataframe and create a new dataframe 'new3'
# Columns dropped: 'id', 'diagnosis', 'radius_mean', 'texture_mean'
new3 = file.drop(['id', 'diagnosis', 'radius_mean', 'texture_mean'], axis=1, inplace=False)

# Display the resulting dataframe 'new3'
print(new3)

# Drop the 'id' column from the dataframe and create a new dataframe 'new'
new = file.drop('id', axis=1, inplace=False)

# Display the original dataframe 'file' to ensure it's unchanged
print(file)

# Display the resulting dataframe 'new'
print(new)

# Drop a specific row (index 2) from the dataframe and create a new dataframe 'new2'
new2 = file.drop([2], axis=0, inplace=False)

# Display the resulting dataframe 'new2'
print(new2)

# Drop multiple specific rows (indexes 2, 3, 4, 5, 6) from the dataframe and create a new dataframe 'new2'
new2 = file.drop([2, 3, 4, 5, 6], axis=0, inplace=False)

# Display the resulting dataframe 'new2'
print(new2)


# Drop another set of columns
new4 = file.drop(['area_mean', 'smoothness_mean'], axis=1, inplace=False)
print(new4)

# Drop another single column
new5 = file.drop('perimeter_mean', axis=1, inplace=False)
print(new5)

# Drop different specific rows
new6 = file.drop([7, 8, 9], axis=0, inplace=False)
print(new6)

# Drop more specific rows
new7 = file.drop([10, 11, 12, 13], axis=0, inplace=False)
print(new7)
