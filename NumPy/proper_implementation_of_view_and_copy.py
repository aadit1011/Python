import numpy as np
import time as t

# Initialize an empty list to hold array elements
arr = []

# Get the number of elements from the user
n = int(input('Please Enter the total number of elements in array='))

# Loop to get each element of the array from the user
for i in range(n):
    mat = int(input(f'Please!!!Enter the {i}th element='))
    arr.append(mat)

# Convert the list to a NumPy array
arr = np.array(arr)

# Pause for 3 seconds
t.sleep(3)
print('Now copying the array........')

# Create a deep copy of the array
arrc = arr.copy()

# Pause for 3 seconds
t.sleep(3)
print('Array copied successfully..........')

# Ask the user if they want to make changes to the array
c = input('Enter \'y\' to make changes in the array and \'n\' to not make any changes=')

# If the user chooses to make changes
if c == 'y' or c == 'Y':
    # Get the position and new value from the user
    pos = int(input('Please Enter the position of the element you want to change='))
    elem = int(input(f'Please Enter the new value of the element at position {pos}='))

    # Update the array with the new value at the specified position
    arr[pos] = elem
else:
    print('Nothing changed..........')

# Pause for 3 seconds
t.sleep(3)
print('The new values inside the elements are.....')

# Iterate through the updated array and print each index and value
for index, items in np.ndenumerate(arr):
    print(f'{index}={items}')

# Print a message indicating the old values in the copied array
print('The old values inside the array were......')

# Iterate through the copied array and print each index and value
for index, item in np.ndenumerate(arrc):
    print(f'{index}={item}')
