# Importing necessary libraries
import pandas as pd
import numpy as np

# Generating random data for columns 'A' and 'B'
data = {
    'A': np.random.randint(1, 100, 200),  # Random integers between 1 and 100 for column 'A'
    'B': np.random.randint(1, 100, 200)   # Random integers between 1 and 100 for column 'B'
}

# Creating a DataFrame from the generated data
daf = pd.DataFrame(data)

# Saving the DataFrame to a CSV file named 'file.csv'
daf.to_csv('file.csv', index=False)  # index=False to not include row indices in the CSV file

# Printing the DataFrame to the console
print(daf)

# Generating another set of random data for columns 'A' and 'B'
data = {
    'A': [np.random.randint(1, 100, 200)],  # Random integers between 1 and 100 for column 'A'
    'B': [np.random.randint(1, 100, 200)]   # Random integers between 1 and 100 for column 'B'
}

# Creating another DataFrame from the new set of generated data
df = pd.DataFrame(data)

# Saving the new DataFrame to a CSV file named 'second.csv'
df.to_csv('second.csv', index=False)  # index=False to not include row indices in the CSV file

# Displaying the new DataFrame
df
