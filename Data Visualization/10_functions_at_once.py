import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_function(x, y, label, title):
    """
    Utility function to plot graphs with a consistent style.
    
    Parameters:
    - x (numpy.ndarray): Array of x-axis values.
    - y (numpy.ndarray): Array of y-axis values corresponding to the x-axis values.
    - label (str): The label for the plot line (used in the legend).
    - title (str): The title of the plot.
    """
    plt.figure(figsize=(5, 3), dpi=300)  # Set figure size and resolution for the plot
    plt.plot(x, y, 'r', label=label)  # Plot the function with red color and given label
    plt.axhline(0, color='black', linewidth=0.5, alpha=0.8)  # Add a horizontal reference line at y=0
    plt.axvline(0, color='black', linewidth=0.5, alpha=0.8)  # Add a vertical reference line at x=0
    plt.xlabel('x')  # Label for x-axis
    plt.ylabel('y')  # Label for y-axis
    plt.title(title)  # Title for the plot
    plt.legend()  # Show the legend
    plt.grid(True, linestyle='--', alpha=0.7)  # Enable grid with dashed lines and set transparency
    plt.show()  # Display the plot

def get_user_inputs(inputs):
    """
    Utility function to get multiple numeric inputs from the user.
    
    Parameters:
    - inputs (list): List of parameter names to prompt for user input.
    
    Returns:
    - List of user-provided values as floats.
    """
    return [float(input(f'Enter the value of {param}=')) for param in inputs]

def choose_function():
    """
    Display a menu for the user to select a mathematical function to plot.
    
    Returns:
    - The user's choice as an integer.
    """
    print("Choose a function to plot:")
    print("1. Linear Function: y = mx + c")
    print("2. Quadratic Function: y = ax^2 + bx + c")
    print("3. Cubic Function: y = ax^3 + bx^2 + cx + d")
    print("4. Exponential Function: y = a * e^(bx)")
    print("5. Logarithmic Function: y = a * log_b(x)")
    print("6. Sine Function: y = a * sin(bx + c)")
    print("7. Cosine Function: y = a * cos(bx + c)")
    print("8. Tangent Function: y = a * tan(bx + c)")
    print("9. Reciprocal Function: y = a / x + b")
    print("10. Gaussian Function: y = a * e^(-(x-b)^2 / (2c^2))")
    
    return int(input("Enter the number corresponding to your choice: "))

def main():
    """
    Main function to execute the program. Handles user input, computes function values,
    and calls the plotting function based on user selection.
    """
    choice = choose_function()  # Get the user's choice of function

    # Get the range and interval details from the user
    lower_limit = float(input('Enter the lower limit of graph (x-axis)='))
    upper_limit = float(input('Enter the upper limit of graph (x-axis)='))
    intervals = int(input('Enter the number of intervals in the graph='))

    # Create an array of x values from the specified range and intervals
    x = np.linspace(lower_limit, upper_limit, intervals)

    # Match the user's choice to the corresponding function and plot it
    match choice:
        case 1:  # Linear Function
            m, c = get_user_inputs(['m (slope)', 'c (y-intercept)'])
            y = m * x + c
            plot_function(x, y, f'y = {m}x + {c}', 'Linear Function')

        case 2:  # Quadratic Function
            a, b, c = get_user_inputs(['a', 'b', 'c'])
            y = a * x**2 + b * x + c
            plot_function(x, y, f'y = {a}x^2 + {b}x + {c}', 'Quadratic Function')

        case 3:  # Cubic Function
            a, b, c, d = get_user_inputs(['a', 'b', 'c', 'd'])
            y = a * x**3 + b * x**2 + c * x + d
            plot_function(x, y, f'y = {a}x^3 + {b}x^2 + {c}x + {d}', 'Cubic Function')

        case 4:  # Exponential Function
            a, b = get_user_inputs(['a', 'b'])
            y = a * np.exp(b * x)
            plot_function(x, y, f'y = {a}e^({b}x)', 'Exponential Function')

        case 5:  # Logarithmic Function
            a, b = get_user_inputs(['a', 'b'])
            y = a * np.log(x) / np.log(b)  # Compute logarithm base b
            plot_function(x, y, f'y = {a}log_{b}(x)', 'Logarithmic Function')

        case 6:  # Sine Function
            a, b, c = get_user_inputs(['a', 'b', 'c'])
            y = a * np.sin(b * x + c)
            plot_function(x, y, f'y = {a}sin({b}x + {c})', 'Sine Function')

        case 7:  # Cosine Function
            a, b, c = get_user_inputs(['a', 'b', 'c'])
            y = a * np.cos(b * x + c)
            plot_function(x, y, f'y = {a}cos({b}x + {c})', 'Cosine Function')

        case 8:  # Tangent Function
            a, b, c = get_user_inputs(['a', 'b', 'c'])
            y = a * np.tan(b * x + c)
            plot_function(x, y, f'y = {a}tan({b}x + {c})', 'Tangent Function')

        case 9:  # Reciprocal Function
            a, b = get_user_inputs(['a', 'b'])
            y = a / x + b
            plot_function(x, y, f'y = {a}/x + {b}', 'Reciprocal Function')

        case 10:  # Gaussian Function
            a, b, c = get_user_inputs(['a', 'b', 'c'])
            y = a * np.exp(-(x-b)**2 / (2 * c**2))  # Gaussian function formula
            plot_function(x, y, f'y = {a}e^(-((x-{b})^2)/(2*{c}^2))', 'Gaussian Function')

        case _:  # Handle invalid choices
            print("Invalid choice! Please run the program again and choose a number between 1 and 10.")

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
