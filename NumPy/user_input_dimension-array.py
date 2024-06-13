import numpy as np;  # Importing the numpy library for handling arrays

y = [];  # Initialize an empty list to store the values

# Loop to get valid user inputs for dimension, number of matrices, and number of values inside each matrix
while True:
    try:
        # Asking the user for the dimension of the array matrix
        dimen = int(input('Enter the dimension of the array matrix: '));  
        if dimen < 0:
            print("Dimension must be non-negative. Please try again.");
            continue;  # If the dimension is negative, ask for input again
        
        # Asking the user for the number of matrices
        n = int(input('Enter the number of matrices: '));  
        if n < 0:
            print("Number of matrices must be non-negative. Please try again.");
            continue;  # If the number of matrices is negative, ask for input again
        
        # Asking the user for the number of values inside each matrix
        v = int(input('Enter the number of values inside each matrix: '));  
        if v < 0:
            print("Number of values must be non-negative. Please try again.");
            continue;  # If the number of values is negative, ask for input again
        
        break;  # Exit loop if all inputs are valid
    except ValueError:
        print("Invalid input. Please enter an integer value.");
        continue;  # If input is not an integer, ask for input again

# Loop to get the elements for each matrix
for i in range(n):
    m = [];  # Initialize an empty list for each matrix
    for j in range(v):
        ask = int(input(f'Enter the {j+1}th element inside {i+1} matrix: '));  # Get the element value from user
        m.append(ask);  # Append the element to the matrix list
    y.append(m);  # Append the matrix to the main list

print(f'The required {dimen}-dimension matrix you entered is:');

# Convert the list to a numpy array with specified dimension
user = np.array(y, ndmin=dimen);  
print(user);  # Print the final array
