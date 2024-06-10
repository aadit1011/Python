# Importing the numpy library and assigning it the alias 'np'
import numpy as np

# Initializing an empty list to store the elements
x = []

# Prompting the user to enter the total number of elements for the list
n = int(input('Enter the total number of elements in list: '))

# Looping 'n' times to get 'n' elements from the user
for _ in range(n):
    # Asking the user to input each element and converting it to an integer
    y = int(input('x = '))
    # Appending each input element to the list 'x'
    x.append(y)

# Converting the list 'x' to a numpy array
y = np.array(x)

# Printing the numpy array
print(y)
