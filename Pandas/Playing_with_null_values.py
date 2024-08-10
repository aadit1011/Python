import pandas as pd
import numpy as np

# Creating a DataFrame with 20 rows and 4 columns, including various null value scenarios
data = {
    'Column1': [np.nan, 1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10, 11, 12, np.nan, 14, np.nan, 16, 17, np.nan, 19],
    'Column2': [21, np.nan, 23, 24, np.nan, 26, 27, 28, np.nan, 30, 31, 32, 33, np.nan, np.nan, 36, 37, np.nan, 39, 40],
    'Column3': [np.nan, np.nan, 43, 44, 45, np.nan, np.nan, 48, 49, 50, np.nan, 52, 53, np.nan, 55, 56, np.nan, 58, 59, np.nan],
    'Column4': [61, 62, np.nan, 64, 65, 66, np.nan, np.nan, 69, np.nan, 71, 72, 73, np.nan, np.nan, 76, 77, 78, 79, np.nan]
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame with various null value scenarios
print("Original DataFrame with various null value scenarios:")
print(df)

# Dropping rows where all elements are NaN
# This operation removes rows that are entirely made up of NaN values.
v = df.dropna(how='all')
print("\nDataFrame after dropping rows where all values are NaN:")
print(v)

# Dropping rows where any element is NaN
# This operation removes rows that contain at least one NaN value.
w = df.dropna(how='any')
print("\nDataFrame after dropping rows where any value is NaN:")
print(w)

# Dropping rows with NaN values specifically in 'Column4'
# This operation focuses on rows with missing data in a specific column.
z1 = df.dropna(subset=['Column4'])
print("\nDataFrame after dropping rows with NaN values in 'Column4':")
print(z1)

# Dropping rows with NaN values in both 'Column4' and 'Column3'
# This operation filters out rows that have NaN values in either of the specified columns.
z2 = df.dropna(subset=['Column4', 'Column3'])
print("\nDataFrame after dropping rows with NaN values in both 'Column4' and 'Column3':")
print(z2)
