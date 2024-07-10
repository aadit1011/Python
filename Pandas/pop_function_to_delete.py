# Importing necessary libraries
import numpy as np
import pandas as pd

# Generating random data for columns 'A' and 'B'
data = {
    'A': np.random.randint(0, 12, 10),  # Random integers between 0 and 12 for column 'A'
    'B': np.random.randint(0, 12, 10)   # Random integers between 0 and 12 for column 'B'
}

# Creating a DataFrame from the generated data
df = pd.DataFrame(data)

# Selecting a subset of the data from index 2 to 7 (inclusive) for columns 'A' and 'B'
df['partA'] = df['A'][2:8]  # Subset of column 'A' from index 2 to 7
df['partB'] = df['B'][2:8]  # Subset of column 'B' from index 2 to 7

# Inserting a new column 'partA+partB' at index 2 which is the sum of 'partA' and 'partB'
df.insert(2, 'partA+partB', df['partA'] + df['partB'])

# Printing the DataFrame to see the changes
print(df)

# Removing the column 'partA+partB' using the pop method
df.pop('partA+partB')

# Deleting the column 'partB' using the del keyword
del df['partB']

# Printing the DataFrame to see the changes
print(df)

# Deleting the column 'partA' using the del keyword
del df['partA']

# Displaying the final DataFrame
df
