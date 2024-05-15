from math import fabs

# Solution of Non-Linear Equation Using Newton Raphson Method
x0 = None
x1 = None
value1 = None
value2 = None
num = None
tol = None
value = None
count = 1

# Define the function whose solution is to be found.
def function(num):
    return (num * num * num) - num - 1

# Return the derivative value of the same function
def derivative_function(num):
    return (3 * num * num) - 1

def scan_function():
    global x0
    x0 = float(input('Enter the initial guess: '))

def finding_approximation():
    global x1, x0, value1
    x1 = x0 - (function(x0) / derivative_function(x0))
    value1 = function(x1)
    if value1 == 0:
        print(f"{x1} is the root of the function.")
    else:
        x0 = x1

def main():
    global value2, tol, x0, x1, value, count
    scan_function()
    value2 = derivative_function(x0)
    if value2 == 0:
        print("The derivative is zero at the initial guess. Please enter a different initial guess.");
        return

    tol = float(input('Please Enter the Tolerable Error: '));
    finding_approximation();
    value = fabs(function(x1));
    while value > tol:
        print(f'\t{count}\t{x0:.6f}\t{value1:.6f}\t{value2:.6f}');
        count += 1;
        finding_approximation();
        value = fabs(function(x1));

    print(f"{x1:.6f} is the root of the function.") 

main()


          
main();