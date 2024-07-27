import numpy as np 
import pandas as pd 

# Reading the CSV file into a DataFrame
file = pd.read_csv('climate.csv')

# Display the DataFrame
print(file)

# To create the array of an index
index_array = file.index.array
print("Index Array:")
print(index_array)

# Question number 2
print("Question number 2:")

# Selecting the subset of the columns
print("Available columns in the DataFrame:")
print(file.columns)

# Selecting specific columns from the DataFrame
basic = file[['_id', 'DATE', 'YEAR', 'MONTH', 'DISTRICT']]
print("Subset of columns:")
print(basic)

# Renaming the columns
new = basic.rename(columns={
    '_id': 'ID',
    'DATE': 'Date',
    'MONTH': 'Month',
    'DISTRICT': 'District'
})

# Adding a new column based on a condition
new['Dis=Arghakhachi'] = new['District'] == 'Arghakhanchi'
print("DataFrame with renamed columns and new conditional column:")
print(new)

# Converting the DataFrame to a numpy array
numpy_array = new.to_numpy()
print("DataFrame converted to numpy array:")
print(numpy_array)

# Deleting the column
new.pop('Dis=Arghakhachi')
print("DataFrame after deleting the 'Dis=Arghakhachi' column:")
print(new)
