import numpy as np

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])

# Create a copy of the array
# `arrc` is a deep copy of `arr`. Changes in `arr` will not affect `arrc` and vice versa.
arrc = arr.copy()

# Modify an element in the original array
# Changing the second element of `arr` from 2 to 20
arr[1] = 20

# Print the copied version of the array
# `arrc` remains unchanged because it is a deep copy of the original array.
print(f'The copied version of the array {arr} is-------')
print()
print(f'{arrc}')
print()

# Create a view of the array
# `arrv` is a shallow copy (view) of `arr`. Changes in `arr` will be reflected in `arrv` and vice versa.
arrv = arr.view()

# Print the view version of the array
# `arrv` reflects the changes made to `arr`.
print(f'The view version of the array {arr} is------')
print()
print(f'{arrv}')
