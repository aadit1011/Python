import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Define the data for the x and y axes
# x represents the positions on the x-axis, and y represents the corresponding values on the y-axis.
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# Define a list of colors for the bars in the bar charts
# This list assigns a color to each bar.
colors = ['r', 'b', 'y', 'g', 'b']

# Plot a simple line graph
# This line plot connects each point (x, y) with a straight line.
plt.plot(x, y)
plt.title("Line Plot of X vs Y")  # Add a title to the plot
plt.xlabel("X Axis")  # Label for the x-axis
plt.ylabel("Y Axis")  # Label for the y-axis
plt.show()  # Display the line plot

# Plot a basic bar chart with default alignment and width
# Each bar's height corresponds to the value in the 'y' list, with colors defined by the 'colors' list.
plt.bar(x, y, color=colors, width=0.8)
plt.title("Bar Chart with Default Alignment")  # Add a title to the plot
plt.xlabel("X Axis")  # Label for the x-axis
plt.ylabel("Y Axis")  # Label for the y-axis
plt.show()  # Display the bar chart

# Plot a bar chart with bars aligned to the edges of the positions
# The bars are aligned to the edge of each x position using 'align=edge'.
plt.bar(x, y, color=colors, width=0.8, align='edge')
plt.title("Bar Chart with Edge Alignment")  # Add a title to the plot
plt.xlabel("X Axis")  # Label for the x-axis
plt.ylabel("Y Axis")  # Label for the y-axis
plt.show()  # Display the bar chart

# Plot a bar chart with bars aligned to the center of the positions
# The bars are centered on each x position using 'align=center'.
plt.bar(x, y, color=colors, width=0.8, align='center')
plt.title("Bar Chart with Center Alignment")  # Add a title to the plot
plt.xlabel("X Axis")  # Label for the x-axis
plt.ylabel("Y Axis")  # Label for the y-axis
plt.show()  # Display the bar chart

# Plot a bar chart with enhanced bar edges
# This plot adds an edge color and line width to the bars for better visibility and aesthetics.
plt.bar(x, y, color=colors, width=0.8, align='center', edgecolor='black', linewidth=3)
plt.title("Bar Chart with Enhanced Edges")  # Add a title to the plot
plt.xlabel("X Axis")  # Label for the x-axis
plt.ylabel("Y Axis")  # Label for the y-axis
plt.show()  # Display the bar chart
