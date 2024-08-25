import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Generate random data for the x and y axes
x = np.random.randint(0, 10, 20)  # Generates 20 random integers between 0 and 10 for the x-axis
y = np.random.randint(5, 16, 20)  # Generates 20 random integers between 5 and 16 for the y-axis (heights of the bars)

# Generate random data for coloring the bars
c = np.random.randint(0, 101, len(x))  # Generates random integers between 0 and 100 for each bar to determine its color

# Map the random integer values 'c' to colors using a colormap
# plt.cm.viridis is a colormap in matplotlib, which converts 'c' values into color values
# The colormap 'viridis' is known for being perceptually uniform and colorblind-friendly
col = plt.cm.viridis(c / max(c))  # Normalizing 'c' values by dividing by the maximum to keep values between 0 and 1

# Plot the bar chart with individual bar colors
plt.bar(x, y, color=col)  # Create a bar plot with x positions, y heights, and colors from 'col'

# Show the plot
plt.show()
