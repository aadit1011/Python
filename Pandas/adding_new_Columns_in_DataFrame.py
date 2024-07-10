# Importing necessary libraries
import numpy as np 
import pandas as pd 

# Generating random data for columns 'A' and 'B'
data = {
    'A': np.random.randint(0, 40, 20),  # Random integers between 0 and 40 for column 'A'
    'B': np.random.randint(0, 40, 20)   # Random integers between 0 and 40 for column 'B'
}

# Creating a DataFrame from the generated data
df = pd.DataFrame(data)

# Adding comparison columns to the DataFrame
df['CompA'] = df['A'] >= 13   # True if 'A' is greater than or equal to 13, else False
df['CompB'] = df['B'] <= 13   # True if 'B' is less than or equal to 40, else False

# Adding columns for maximum and minimum values
df['Max(A)'] = df['A'].max()  # Maximum value in column 'A'
df['Min(A)'] = df['B'].min()  # Minimum value in column 'B'

# Performing arithmetic operations and adding the results as new columns
df['A+B'] = df['A'] + df['B']  # Sum of columns 'A' and 'B'
df['A-B'] = df['A'] - df['B']  # Difference between columns 'A' and 'B'
df['AXB'] = df['A'] * df['B']  # Product of columns 'A' and 'B'
df['A/B'] = df['A'] / df['B']  # Division of column 'A' by column 'B'

# Sorting the columns 'A' and 'B' and adding the results as new columns
df['AscA'] = np.sort(df['A'])  # Sorted values of column 'A' in ascending order
df['AscB'] = np.sort(df['B'])  # Sorted values of column 'B' in ascending order

# Adding comparison columns for equality, less than, and greater than
df['A=B'] = df['A'] == df['B']  # True if values in 'A' equal to values in 'B', else False
df['A<B'] = df['A'] < df['B']   # True if values in 'A' less than values in 'B', else False
df['A>B'] = df['A'] > df['B']   # True if values in 'A' greater than values in 'B', else False

# Adding statistical columns to the DataFrame
df['Mean(A)'] = np.mean(df['A'])    # Mean of column 'A'
df['Mean(B)'] = np.mean(df['B'])    # Mean of column 'B'
df['Median(A)'] = np.median(df['A']) # Median of column 'A'
df['Median(B)'] = np.median(df['B']) # Median of column 'B'

# Displaying the final DataFrame
print(df)

#Inserting new columns 

df.insert(17,'SD(A)',np.std(df['A']))
df.insert(18,'SD(B)',np.std(df['B']))
#Displaying yhr final DataFrame
df
