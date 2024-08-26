import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Define data for plotting
# 'data' represents the y-values (heights) of the points to plot
data = [1, 2, 3, 4, 5]

# 'name' represents the x-values (labels) for the points
name = ['A', 'B', 'C', 'D', 'E']

# Create a line plot with the provided data
# 'name' is plotted along the x-axis and 'data' along the y-axis
# 'ro--' specifies the plot style: 'r' for red color, 'o' for circular markers, '--' for dashed line style
plt.plot(name, data, 'ro--', label='name')

# Draw a horizontal line at y=0 across the entire plot
# 'color' sets the line color to red, 'linewidth' sets the line thickness to 2
plt.axhline(0, color='r', linewidth=2)

# Draw a vertical line at x=0 across the entire plot
# 'color' sets the line color to red, 'linewidth' sets the line thickness to 2
plt.axvline(0, color='r', linewidth=2)

# Display the legend on the plot
# The legend shows labels for the plotted data; 'label' in plt.plot() is used here
plt.legend()

# Display the plot to the screen
plt.show()
