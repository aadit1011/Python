# Import necessary libraries
import pandas as pd  # pandas is used for data manipulation and analysis
import numpy as np  # numpy is used for numerical operations
import matplotlib.pyplot as plt  # matplotlib is used for data visualization

# Sample data for plotting
data = [1, 2, 3, 4, 5]  # List of y-values to plot
name = ['A', 'B', 'C', 'D', 'E']  # List of x-values (labels) to plot

# Plotting the data
plt.plot(name, data, 'ro--', label='name')  # 'ro--' means red color (r), circles (o), dashed line (--)

# Adding a legend to the plot
plt.legend()  # Display the legend on the plot

# Displaying the plot
plt.show()  # Show the plot on the screen
