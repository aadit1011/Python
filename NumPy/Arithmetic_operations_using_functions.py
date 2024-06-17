import numpy as np;  # Import the NumPy library

a = np.array([1, 2, 3, 4, 5, 6]);  # Create a NumPy array 'a' with values [1, 2, 3, 4, 5, 6]
b = np.array([4, 5, 6, 7, 8, 9]);  # Create a NumPy array 'b' with values [4, 5, 6, 7, 8, 9]

su = np.add(a, b);  # Perform element-wise addition of arrays 'a' and 'b'
sub = np.subtract(a, b);  # Perform element-wise subtraction of arrays 'a' and 'b'
mul = np.multiply(a, b);  # Perform element-wise multiplication of arrays 'a' and 'b'
divid = np.divide(a, b);  # Perform element-wise division of arrays 'a' and 'b'
remain = np.mod(a, b);  # Compute element-wise modulus (remainder) of arrays 'a' and 'b'
recip_a = np.reciprocal(1 / a);  # Calculate the reciprocal of each element in array 'a'
recip_b = np.reciprocal(1 / b);  # Calculate the reciprocal of each element in array 'b'
power = np.power(a, b);  # Perform element-wise exponentiation of 'a' to the power of 'b'

# Print the results
print(f'Addition of a and b:\n{su}'); 
print(f'Multiplication of a and b:\n{mul}'); 
print(f'Subtraction of a from b:\n{sub}'); 
print(f'Division of a by b:\n{divid}'); 
print(f'Remainder of a divided by b:\n{remain}'); 
print(f'Reciprocal of elements in a:\n{recip_a}'); 
print(f'Reciprocal of elements in b:\n{recip_b}'); 
print(f'a raised to the power of b:\n{power}');
