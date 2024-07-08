import pandas as pd  # Importing the pandas library for data manipulation and analysis

# Creating a list of dictionaries, where each dictionary represents an employee's data
emp = [
    {'Name': 'Aadit Sharma', 'Age': 21, 'Salary': 992130939, 'Address': 'Pepsicola'},
    {'Name': 'Prijal Khadka', 'Age': 21, 'Salary': 42130939, 'Address': 'Pepsicola'},
    {'Name': 'Ashum Shrestha', 'Age': 21, 'Salary': 52130939, 'Address': 'Pepsicola'},
    {'Name': 'Pranil Shrestha', 'Age': 21, 'Salary': 62130939, 'Address': 'Pepsicola'},
    {'Name': 'Roshan Pandey', 'Age': 21, 'Salary': 72130939, 'Address': 'Pepsicola'},
    {'Name': 'Rosan Shrestha', 'Age': 21, 'Salary': 82130939, 'Address': 'Pepsicola'},
    {'Name': 'Ankit Nepali', 'Age': 21, 'Salary': 92130939, 'Address': 'Pepsicola'},
    {'Name': 'Rosan Shrestha', 'Age': 21, 'Salary': 223130939, 'Address': 'Chabahil'},
    {'Name': 'Netra Pokhrel', 'Age': 20, 'Salary': 276130939, 'Address': 'Pepsicola'},
    {'Name': 'Aman Rai', 'Age': 21, 'Salary': 29567, 'Address': 'Pepsicola'},
    {'Name': 'Santosh Pokhrel', 'Age': 20, 'Salary': 276130939, 'Address': 'Pepsicola'}
]

# Creating a pandas DataFrame from the list of dictionaries
empS = pd.DataFrame(emp)

# Printing the entire DataFrame
print(empS)

# Displaying the first few rows of the DataFrame
empS.head()

# Displaying the last few rows of the DataFrame
empS.tail()

# Selecting and printing the 'Age' column from the DataFrame
age = empS['Age']
print(age)

# Selecting and printing the 'Name' column from the DataFrame
name = empS['Name']
print(name)

# Filtering and printing the DataFrame for employees with salary greater than 500000
sal = empS['Salary'] > 500000  # Creating a boolean mask for salaries greater than 500000
print()
print("Salary greater than 500000")
print()
print(empS[sal])  # Printing rows where the salary is greater than 500000

# Printing a concise summary of the DataFrame
empS.info()

# Printing descriptive statistics for the DataFrame
empS.describe()
