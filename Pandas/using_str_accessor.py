import pandas as pd  # Import the pandas library for data manipulation and analysis

# Prompt the user to enter their email address and store the input in the variable 'email'
email = input('Enter your email address=')

# Create a DataFrame 'table' with a single entry: the user's email
# The email is placed inside a list ([]) to ensure it's treated as a single element column
table = pd.DataFrame({'Email': [email]})

# Add a new column 'Domain' to the DataFrame
# The 'Domain' column extracts the domain part of the email address (after the '@' symbol)
# 'str.split('@')' splits the email string into two parts: the part before '@' and the part after '@'
# 'str[-1]' selects the last element from the split result, which is the domain
table['Domain'] = table['Email'].str.split('@').str[-1]

# Display the DataFrame 'table' which now includes both the original email and its extracted domain
table
