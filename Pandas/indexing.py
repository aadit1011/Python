import pandas as pd  # Importing the pandas library for data manipulation and analysis

# Creating a list of marks
marks = [98, 99, 97, 96, 95, 99, 92, 91, 90, 92]

# Creating a pandas Series with specified indices (student names)
markS = pd.Series(marks, index=['Aadit Sharma', 'Ankit Ramtel', 'Rosan Shrestha', 'Roshan Pandey', 'Prijal Khadka', 
                                'Biyash Shrestha', 'Ashum Shrestha', 'Aman Rai', 'Pranil Barahi', 'Nayan Chaudhary'])

# Printing the entire Series
print(markS)

# Filtering and printing marks greater than 95
greater = markS[markS > 95]  # Select elements where marks are greater than 95
print('Greater than 95')
print()  # Print an empty line for readability
print(greater)
print()  # Print an empty line for readability

# Filtering and printing marks smaller than 95
smaller = markS[markS < 95]  # Select elements where marks are smaller than 95
print('Smaller than 95')
print()  # Print an empty line for readability
print(smaller)
print()  # Print an empty line for readability

# Filtering and printing marks equal to 92
equal = markS[markS == 92]  # Select elements where marks are equal to 92
print('Equals to 92')
print()  # Print an empty line for readability
print(equal)
