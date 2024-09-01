import pandas as pd  # Import pandas for data manipulation and analysis (not used in this code but often used in conjunction with matplotlib)
import matplotlib.pyplot as plt  # Import matplotlib's pyplot module for plotting
import numpy as np  # Import numpy for numerical operations (not used directly in this example)

# Data to plot
number = [10, 20, 50, 5, 15]  # A list representing the sizes of each slice of the pie chart
name = ['C++', 'JAVA', 'Python', 'JS', 'SQL']  # A list of labels for each slice of the pie chart

# Creating a pie chart
plt.pie(number, labels=name)  # Generate a pie chart with 'number' as the data and 'name' as the corresponding labels

# Display the plot
plt.show()  # Display the pie chart in a window
