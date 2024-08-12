import pandas as pd
import numpy as np

# Creating a dictionary to simulate a dataset with various null value scenarios
data = {
    'Column1': [np.nan, 1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10, 11, 12, np.nan, 14, np.nan, 16, 17, np.nan, 19],
    'Column2': [21, np.nan, 23, 24, np.nan, 26, 27, 28, np.nan, 30, 31, 32, 33, np.nan, np.nan, 36, 37, np.nan, 39, 40],
    'Column3': [np.nan, np.nan, 43, 44, 45, np.nan, np.nan, 48, 49, 50, np.nan, 52, 53, np.nan, 55, 56, np.nan, 58, 59, np.nan],
    'Column4': [61, 62, np.nan, 64, 65, 66, np.nan, np.nan, 69, np.nan, 71, 72, 73, np.nan, np.nan, 76, 77, 78, 79, np.nan]
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Filling NaN values with specific string values for each column
# This replaces NaN values in each column with the designated string.
df_filled = df.fillna({'Column1': 'Col1', 'Column2': 'Col2', 'Column3': 'Col3', 'Column4': 'Col4'})
print("\nDataFrame after filling NaN values with specific strings for each column:")
print(df_filled)

# Backward filling NaN values along columns (axis=1)
# This fills NaN values using the next valid value in the same row, moving from left to right.
df_bfill_col = df.fillna(method='bfill', axis=1)
print("\nDataFrame after backward filling NaN values along columns:")
print(df_bfill_col)

# Forward filling NaN values along columns (axis=1)
# This fills NaN values using the previous valid value in the same row, moving from left to right.
df_ffill_col = df.fillna(method='ffill', axis=1)
print("\nDataFrame after forward filling NaN values along columns:")
print(df_ffill_col)

# Forward filling NaN values along rows (axis=0)
# This fills NaN values using the previous valid value in the same column, moving from top to bottom.
df_ffill_row = df.fillna(method='ffill', axis=0)
print("\nDataFrame after forward filling NaN values along rows:")
print(df_ffill_row)

# Backward filling NaN values along rows (axis=0)
# This fills NaN values using the next valid value in the same column, moving from top to bottom.
df_bfill_row = df.fillna(method='bfill', axis=0)
print("\nDataFrame after backward filling NaN values along rows:")
print(df_bfill_row)
