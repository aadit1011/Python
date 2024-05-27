from math import fabs

 
# Global variables
x0 = None  # Initial guess
x1 = None  # Next guess
value1 = None  # Function value at x1
value2 = None  # Derivative value at x0
tol = None  # Tolerable error
value = None  # Absolute value of function at x1
count = 1  # Iteration counter

# Define the function whose root is to be found
def function(num):
    return (num * num * num) - num - 1

# Define the derivative of the function
def derivative_function(num):
    return (3 * num * num) - 1

# Function to read the initial guess from the user
def scan_function():
    global x0
    x0 = float(input('Enter the initial guess: '))

# Function to find the next approximation using Newton-Raphson method
def finding_approximation():
    global x1, x0, value1
    x1 = x0 - (function(x0) / derivative_function(x0))
    value1 = function(x1)
    if value1 == 0:
        print(f"{x1} is the root of the function.")
    else:
        x0 = x1

# Main function
def main():
    global value2, tol, x0, x1, value, count
    # Read initial guess
    scan_function()
    
    # Calculate derivative at the initial guess
    value2 = derivative_function(x0)
    
    # Check if the derivative is zero at the initial guess
    if value2 == 0:
        print("The derivative is zero at the initial guess. Please enter a different initial guess.")
        return

    # Read the tolerable error from the user
    tol = float(input('Please Enter the Tolerable Error: '))
    
    # Perform the first approximation
    finding_approximation()
    
    # Calculate the absolute value of the function at x1
    value = fabs(function(x1))
    
    # Iterate until the error is within the tolerable limit
    while value > tol:
        print(f'\tIteration: {count}\tCurrent Guess: {x0:.6f}\tFunction Value: {value1:.6f}\tDerivative Value: {value2:.6f}')
        count += 1
        finding_approximation()
        value = fabs(function(x1))

    # Print the final root found
    print(f"{x1:.6f} is the root of the function.") 

# Run the main function
main()
