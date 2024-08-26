import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating x-axis data using NumPy array ranging from 1 to 10
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Creating y-axis data using NumPy's arange function from 0 to 100 with step 10 and slicing to exclude the first value
y = np.arange(0, 101, 10)[1:]

# Setting up the plot figure with a specific size (5x3 inches) and resolution (300 DPI for high quality)
plt.figure(figsize=(5, 3), dpi=300)

# Plotting the first segment of the square function (x^2) in red solid line style
plt.plot(x[:6], x[:6]**2, 'r', label='Square')

# Plotting the second segment of the square function (x^2) in red dashed line style to differentiate segments
plt.plot(x[5:], x[5:]**2, 'r--')

# Plotting a linear function (y = 10x) in blue to compare against the quadratic function
plt.plot(x, y, 'b', label='Linear')

# Adding a legend to indicate which plot corresponds to each function
plt.legend()

# Labeling the x-axis as 'X--->'
plt.xlabel('X--->')

# Labeling the y-axis as 'Y--->'
plt.ylabel('Y--->')

# Setting the title of the plot to 'X-Y and X-X^2'
plt.title('X-Y and X-X^2')

# Displaying the plot on the screen
plt.show()

# Plotting a Linear Function
# Generating x values using linspace for smooth plotting between -20 and 20 with 200 intervals
x = np.linspace(-20, 20, 200)

# Taking input for the slope (m) and y-intercept (c) from the user
m = float(input('Enter the value of slope (m)='))
c = float(input('Enter the value of y intercept (c)='))

# Calculating y values for the linear function using the formula y = mx + c
y = m * x + c

# Plotting the linear function with the given slope and intercept
plt.plot(x, y, label=f'y = {m}x + {c}', color='blue')

# Adding labels and title to the plot for clarity
plt.xlabel('x')  # x-axis label
plt.ylabel('y')  # y-axis label
plt.title(f'Plot of Linear Function: y = {m}x + {c}')  # Title with dynamic formula

# Adding horizontal and vertical lines at 0 for better visual reference of axes
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal reference line
plt.axvline(0, color='black', linewidth=0.5)  # Vertical reference line

# Enabling grid for better readability with a dashed line style and some transparency
plt.grid(True, linestyle='--', alpha=0.7)

# Setting up the plot figure with a specific size (5x3 inches) and resolution (300 DPI for high quality)
plt.figure(figsize=(5, 3), dpi=300)

# Adding a legend to the plot
plt.legend()

# Displaying the plot on the screen
plt.show()

# Plotting a Quadratic Function
# Taking input from the user for graph range and interval
l = float(input('Enter the lower limit of graph (x-axis)='))
u = float(input('Enter the upper limit of graph (x-axis)='))
i = int(input('Enter the number of intervals in the graph='))

# Generating x values using linspace for the specified range and intervals
x = np.linspace(l, u, i)

# Taking input for coefficients of the quadratic equation y = ax^2 + bx + c
a = float(input('Enter the value of a='))
b = float(input('Enter the value of b='))
c = float(input('Enter the value of c='))

# Calculating y values for the quadratic function using the formula y = ax^2 + bx + c
y = a * x**2 + b * x + c

# Plotting the quadratic function with the user-provided coefficients
plt.plot(x, y, 'r', label=f'Quadratic Function: y = {a}x^2 + {b}x + {c}')

# Adding legend, axis labels, title, and grid for better visualization
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal reference line at y=0
plt.axvline(0, color='black', linewidth=0.5)  # Vertical reference line at x=0
plt.xlabel('x')  # x-axis label
plt.ylabel('y')  # y-axis label
plt.title('Plot of Quadratic Function')  # Plot title
plt.figure(figsize=(5, 3), dpi=300)  # Figure size and resolution
plt.grid(True, linestyle='--', alpha=0.7)  # Grid settings

# Displaying the plot on the screen
plt.show()

# Plotting a Cubic Function
# Taking input from the user for graph range and interval
l = float(input('Enter the lower limit of graph (x-axis)='))
u = float(input('Enter the upper limit of graph (x-axis)='))
i = int(input('Enter the number of intervals in the graph='))

# Generating x values using linspace for the specified range and intervals
x = np.linspace(l, u, i)

# Taking input for coefficients of the cubic equation y = ax^3 + bx^2 + cx + d
a = float(input('Enter the value of a='))
b = float(input('Enter the value of b='))
c = float(input('Enter the value of c='))
d = float(input('Enter the value of d='))

# Calculating y values for the cubic function using the formula y = ax^3 + bx^2 + cx + d
y = a * x**3 + b * x**2 + c * x + d

# Plotting the cubic function with the user-provided coefficients
plt.plot(x, y, 'r', label=f'Cubic Function: y = {a}x^3 + {b}x^2 + {c}x + {d}')

# Adding legend, axis labels, title, and grid for better visualization
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal reference line at y=0
plt.axvline(0, color='black', linewidth=0.5)  # Vertical reference line at x=0
plt.xlabel('x')  # x-axis label
plt.ylabel('y')  # y-axis label
plt.title('Plot of Cubic Function')  # Plot title
plt.figure(figsize=(5, 3), dpi=300)  # Figure size and resolution
plt.grid(True, linestyle='--', alpha=0.7)  # Grid settings

# Displaying the plot on the screen
plt.show()
