import numpy as np  # Importing the numpy library for numerical operations
import pandas as pd  # Importing the pandas library for data manipulation and analysis

# Reading the CSV file into a DataFrame
df = pd.read_csv('mt_everest.csv')
# Displaying the DataFrame
print(df)

# Converting the data type of the '_id' column to float while reading the CSV file
df2 = pd.read_csv('mt_everest.csv', dtype={'_id': float})
# Displaying the DataFrame with the '_id' column as float
print(df2)
