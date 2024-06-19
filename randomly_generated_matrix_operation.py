import numpy as np;  # Importing NumPy library

# Generating two random 1D arrays of 9 elements each within the range 1 to 10
matrix_a = np.random.randint(1, 11, size=9);  # Random matrix A
matrix_b = np.random.randint(1, 11, size=9);  # Random matrix B

# Reshaping the 1D arrays into 2D arrays (3x3)
matrix_a = np.array(matrix_a).reshape(3, 3);  # Reshape matrix A
matrix_b = np.array(matrix_b).reshape(3, 3);  # Reshape matrix B

# Printing the generated matrices
print('Matrix A:');
print(matrix_a);
print();
print('Matrix B:');
print(matrix_b);
print();

# Calculating the transpose of both matrices
transpose_a = np.transpose(matrix_a);  # Transpose of matrix A
transpose_b = np.transpose(matrix_b);  # Transpose of matrix B

# Performing matrix operations: addition, subtraction, and element-wise multiplication
addition = np.add(matrix_a, matrix_b);  # Addition of matrices
subtraction = np.subtract(matrix_a, matrix_b);  # Subtraction of matrices
multiplication = np.multiply(matrix_a, matrix_b);  # Element-wise multiplication of matrices

# Printing the results of matrix operations
print(f'The addition of \n{matrix_a} \nand \n{matrix_b} \nis \n{addition}');
print();
print(f'The subtraction of \n{matrix_a} \nfrom \n{matrix_b} \nis \n{subtraction}');
print();
print(f'The element-wise multiplication of \n{matrix_a} \nand \n{matrix_b} \nis \n{multiplication}');
print();

# Printing the transpose of the matrices
print(f'The transpose of \n{matrix_a} \nis \n{transpose_a}');
print();
print(f'The transpose of \n{matrix_b} \nis \n{transpose_b}');
