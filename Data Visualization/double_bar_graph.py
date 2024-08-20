import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt 

# Data for plotting
name = ['Aadit', 'Prijal', 'Biyash', 'Bipin', 'Ankit', 'Roshan', 'Netra']  # Names corresponding to the data
number = [1000, 200, 300, 40, 500, 60, 700]  # First set of values representing some metric
number2 = [2000, 20, 800, 700, 1500, 600, 1700]  # Second set of values for comparison

# Width of each bar in the bar chart
width = 0.4  # Setting the width of the bars for both data sets

# Generate x positions for each name label
x = np.arange(len(name))  # Creating an array of positions, one for each name

# Plotting the first set of bars (number) shifted slightly to the left
plt.bar(x - width/2, number, color='red', width=width, label='Number', edgecolor='black')

# Plotting the second set of bars (number2) shifted slightly to the right
plt.bar(x + width/2, number2, color='blue', width=width, label='Number 2', edgecolor='black')

# Adding labels and titles to the plot for clarity
plt.xlabel('Names', fontsize=12)  # Label for the x-axis
plt.ylabel('Values', fontsize=12)  # Label for the y-axis
plt.title('Comparison of Two Sets of Numbers', fontsize=16)  # Title of the plot

# Customizing x-axis ticks to display the names
plt.xticks(ticks=x, labels=name)  # Setting the x-ticks to the names

# Display the legend to differentiate between the two datasets
plt.legend()

# Adjust layout to avoid overlap and show the final plot
plt.tight_layout()  # Automatically adjusts subplot parameters to give specified padding
plt.show()  # Display the plot
