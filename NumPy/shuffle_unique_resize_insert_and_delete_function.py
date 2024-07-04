import numpy as np

# Shuffle function to shuffle data
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

np.random.shuffle(arr1)  # Shuffle the array in place
print("Shuffled array:", arr1)
print()

# Using Unique function in different ways
arr = np.array([1, 2, 3, 4, 5, 5, 5, 1, 1, 2, 3, 4, 6, 7, 7, 7, 8, 8, 8, 9, 6, 5, 3, 2, 2, 62])

index = np.unique(arr, return_index=True)  # Get unique values and their first occurrence indices
reverse = np.unique(arr, return_inverse=True)  # Get unique values and the indices to reconstruct the original array
count = np.unique(arr, return_counts=True)  # Get unique values and their counts

print(f'Original Array={arr}')
print()
print(f'Indexed values and their first occurrence indices={index}')
print()
print(f'Unique values and indices to reconstruct the original array={reverse}')
print()
print(f'Unique values and their counts={count}')
print()

# Using Resize function
resize = np.resize(arr, (8, 3))  # Resize the array to 8x3
print(f'Resized array to shape (8, 3):\n{resize}')
print()

# Using Insert and Delete functions
# Initialize the array
m = np.array(['Aadit', 'Biyash','Prijal','Ashum','Nayan','Netra','Aman', 'Roshan', 'Harry', 'Harley', 'David', 'Ankit','Bipin'])
print("Initial array:\n", m)
print()

# Insert values into the array
n = int(input('Enter the number of values you want to insert: '))
for i in range(n):
    user = input('Enter the value to insert: ')
    m = np.insert(m, 1, user)  # Insert user input at index 1
print()
print(f'Array after insertion:\n{m}')
print()

# Delete value from the array
loc = int(input('Enter the index of the value you want to delete: '))
d = np.delete(m, loc)  # Delete the value at the specified index
print()
print(f'Array after deletion:\n{d}')
