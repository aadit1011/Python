import numpy as np;  # Import numpy for matrix operations

# Initialize matrices and operation results
matrix_a = [];  # Matrix A
matrix_b = [];  # Matrix B
add = [];  # Addition result
sub = [];  # Subtraction result 
mul = [];  # Multiplication result

# Input handling and matrix dimensions
while True:
    try:
        rowA, colA = map(int, input('Enter the number of rows and columns of matrix A : ').split());  # Input dimensions for matrix A
        if rowA <= 0 or colA <= 0:  # Check for positive dimensions
            print('Enter positive integer values for matrix dimensions.'); 
            continue;  # Prompt user again if dimensions are not positive

        rowB, colB = map(int, input('Enter the number of rows and columns of matrix B : ').split());  # Input dimensions for matrix B
        if rowB <= 0 or colB <= 0:  # Check for positive dimensions
            print('Enter positive integer values for matrix dimensions.'); 
            continue;  # Prompt user again if dimensions are not positive

        break;  # Exit loop if valid dimensions are entered
    except ValueError: 
        print('Please enter the values correctly.');  # Error message for invalid input

# Input values for matrix A
print('Now enter the values for matrix A:'); 
for i in range(rowA): 
    y = [];  # Initialize a row for matrix A
    for j in range(colA): 
        val = int(input(f'Enter the element at position ({i}, {j}): '));  # Input element for matrix A
        y.append(val);  # Append element to the row
    matrix_a.append(y);  # Append row to matrix A

# Input values for matrix B
print('Now enter the values for matrix B:'); 
for i in range(rowB): 
    y = [];  # Initialize a row for matrix B
    for j in range(colB): 
        val = int(input(f'Enter the element at position ({i}, {j}): '));  # Input element for matrix B
        y.append(val);  # Append element to the row
    matrix_b.append(y);  # Append row to matrix B

# Convert lists to numpy arrays
matrix_a = np.array(matrix_a);  # Convert matrix A to numpy array
matrix_b = np.array(matrix_b);  # Convert matrix B to numpy array
print('Your matrices are successfully recorded.'); 

# Choose the operation
choice = int(input('Enter\n1 for addition of Matrix\n2 for subtraction of A and B\n3 for multiplication of A and B\n4 to exit: ')); 

# Perform the chosen operation
match choice:
    case 1: 
        if matrix_a.shape == matrix_b.shape:  # Check if dimensions match for addition
            add = matrix_a + matrix_b;  # Perform addition
            print(f'The result of addition of\n{matrix_a}\nand\n{matrix_b}\nis:\n{add}'); 
        else:
            print('Matrix addition requires both matrices to have the same dimensions.');  # Error message for dimension mismatch
    case 2: 
        if matrix_a.shape == matrix_b.shape:  # Check if dimensions match for subtraction
            sub = matrix_a - matrix_b;  # Perform subtraction
            print(f'The result of subtraction of\n{matrix_b}\nfrom\n{matrix_a}\nis:\n{sub}'); 
        else:
            print('Matrix subtraction requires both matrices to have the same dimensions.');  # Error message for dimension mismatch
    case 3: 
        if colA == rowB:  # Check if dimensions match for multiplication
            mul = np.dot(matrix_a, matrix_b);  # Perform multiplication
            print(f'The result of multiplication of\n{matrix_a}\nand\n{matrix_b}\nis:\n{mul}'); 
        else:
            print('Matrix multiplication requires the number of columns in matrix A to be equal to the number of rows in matrix B.');  # Error message for dimension mismatch
    case 4:
        exit();  # Exit the program
    case _: 
        print('Please enter a valid choice.');  # Error message for invalid choice


