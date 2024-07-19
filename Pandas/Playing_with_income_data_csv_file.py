import numpy as np  # Importing numpy for numerical operations (not directly used in this code)
import pandas as pd  # Importing pandas for data manipulation and analysis

# Reading the CSV file into a DataFrame
data = pd.read_csv('income_data.csv')
print(data)

# Reading the first five rows of the file
first = data.head()
print(first)

# Reading the last five rows of the file
last = data.tail()
print(last)

# Calculating the total number of rows and columns in the file
data.info()

# Reading the names of the columns in the dataset
no_of_cols = len(data.columns)  # Counting the total number of columns
print(no_of_cols)
names_of_cols = data.columns  # Getting the column names
names_of_cols = pd.DataFrame(names_of_cols)  # Converting the column names to a DataFrame
print(names_of_cols)

# Renaming all the columns in the CSV file
data_new = pd.read_csv('income_data.csv', names=['Id', 'Company Catagory', 'Bonus', 'Qualification', 'Martial Status', 'Profession', 'Family Status', 'Skin Complextion', 'Gender', '2174', '0', '40', 'Country', 'Income'])
print(data_new)

# Fetching data where the column '2174' equals 15024
filtered_data = data_new[data_new['2174'] == 15024]
print(filtered_data)

# Reading only the 'Country' and 'Income' columns
country = data[' United-States']
income = data[' <=50K']
dat = pd.DataFrame({'Country': country, 'Income': income})
print(dat)

# Renaming all the columns
data_new = pd.read_csv('income_data.csv', names=['Classification', 'Company Catagory', 'Bonus', 'Qualification', 'Martial Status', 'Profession', 'Family Status', 'Skin Complextion', 'Gender', '2174', '0', '40', 'Country', 'Income'])
print(data_new)

# Setting 'Company Catagory' as the new index
dat = data_new.set_index('Company Catagory')
print(dat)

# Setting 'Classification' as the new index
new = data_new.set_index('Classification')
print(new)

# Resetting the index to the default integer index
new = data_new.reset_index()
print(new)

# Displaying the first 10 rows of the reset index DataFrame
print(new[:10])

# Fetching rows from index 20 to 30
subset = new[20:31]
print(subset)

# Fetching data where 'Company Catagory' is less than 200000
income = new[new['Company Catagory'] < 200000]
print(new.info())
print(income)
print(income.info())

# Creating a DataFrame with only the 'Company Catagory' column
company_catagory_data = pd.DataFrame(new['Company Catagory'])

# Calculating and displaying statistical measures for 'Company Catagory'
mean = company_catagory_data.mean()  # Mean
print(f'Mean: {mean}')

median = company_catagory_data.median()  # Median
print(f'Median: {median}')

std_dev = company_catagory_data.std()  # Standard Deviation
print(f'Standard Deviation: {std_dev}')

max_value = company_catagory_data.max()  # Maximum value
print(f'Maximum: {max_value}')

min_value = company_catagory_data.min()  # Minimum value
print(f'Minimum: {min_value}')
