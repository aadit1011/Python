import numpy as np 
import pandas as pd 

# Creating the DataFrame with the given data and NaN values
data = {
    'A': [6.0, np.nan, 4.0, 4.0, 8.0, np.nan, 6.0, 3.0, 5.0, np.nan],
    'B': [7.0, 9.0, np.nan, np.nan, 7.0, 8.0, 8.0, np.nan, 2.0, 6.0],
    'C': [np.nan, 5.0, 4.0, 1.0, np.nan, np.nan, 1.0, 3.0, 4.0, 9.0],
    'D': [2.0, 4.0, 4.0, 4.0, 8.0, 1.0, np.nan, np.nan, np.nan, 8.0]
}

# Creating a DataFrame using the dictionary 'data'
df = pd.DataFrame(data)

# Displaying the original DataFrame with NaN values
print("Original DataFrame with NaN values:")
print(df)

# To check whether there are any null values in the given dataset or not
# Using the isnull() function to identify null values and sum() to count them
null_values = df.isnull().sum()
print(f'The null values are:\n{null_values}')
print()
print(f'The total number of null values in the given data set is: {null_values.sum()}')

# Filling all NaN values with the constant value 12
# The fillna() function is used to replace null values
filled = df.fillna(12)
print(f'Previously:\n{df}')
print()
print(f'New DataFrame with NaN values filled with 12:\n{filled}')

# Alternatively, filling NaN values in each column with different strategies

# Creating a copy of the DataFrame to play with NaN values
df_play = df.copy()

# Filling NaN values in column 'A' with a string 'A_e'
df_play['A'] = df_play['A'].fillna('A_e')

# Filling NaN values in column 'B' using forward fill method (fill with previous value)
df_play['B'] = df_play['B'].fillna(method='ffill')

# Filling NaN values in column 'C' using backward fill method (fill with next value)
df_play['C'] = df_play['C'].fillna(method='bfill')

# Filling NaN values in column 'D' with a string 'D'
df_play['D'] = df_play['D'].fillna('D')

# Displaying the modified DataFrame with filled NaN values
print("\nModified DataFrame after handling NaN values with different strategies:")
print(df_play)
