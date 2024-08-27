# Import necessary libraries
import pandas as pd  # Pandas is used for data manipulation and analysis
import numpy as np  # NumPy is used for numerical operations on large, multi-dimensional arrays and matrices
import matplotlib.pyplot as plt  # Matplotlib is used for creating static, animated, and interactive visualizations in Python

# Data for the bar chart
name = ['Aadit', 'Ankit', 'Bipin']  # List of names (categories) for the x-axis
value = [1, 2, 3]  # Corresponding values for each name (height of the bars)

# Creating a bar chart
bars = plt.bar(name, value)  # 'plt.bar' creates a bar chart and returns a list of bar objects

# Adding hatch patterns to the bars for better visual distinction
bars[0].set_hatch('o')  # Sets a circular hatch pattern for the first bar (Aadit)
bars[1].set_hatch('-')  # Sets a dashed hatch pattern for the second bar (Ankit)
bars[2].set_hatch('*')  # Sets a star hatch pattern for the third bar (Bipin)

# Display the plot
plt.show()  # 'plt.show()' displays the current figure (the bar chart)
