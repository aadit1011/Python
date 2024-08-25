import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Generate random data for the histogram
x = np.random.randint(10, 101, 30)  # Generates 30 random integers between 10 and 100

# Create the first histogram plot
plt.figure(figsize=(10, 6))  # Set the figure size to make it clearer and more readable
plt.title('Histogram Plot', fontsize=16)  # Set the title of the plot with a larger font size for better readability
plt.hist(x, bins=10, edgecolor='black')  # Plot the histogram with specified bins and black edges for each bar
plt.xlabel('Value', fontsize=14)  # Label for the x-axis
plt.ylabel('Frequency', fontsize=14)  # Label for the y-axis
plt.grid(True, linestyle='--', alpha=0.7)  # Add a grid for better visualization, with dashed lines and some transparency
plt.show()  # Display the first plot

# Create a second histogram plot without the additional formatting
plt.figure(figsize=(10, 6))  # Again, set the figure size
plt.hist(x, bins=10)  # Plot the histogram without specifying edge color
plt.title('Histogram Plot Without Edge Color', fontsize=16)  # Differentiate the title to specify the change
plt.xlabel('Value', fontsize=14)  # Label for the x-axis
plt.ylabel('Frequency', fontsize=14)  # Label for the y-axis
plt.grid(True, linestyle='--', alpha=0.7)  # Add a grid to this plot as well
plt.show()  # Display the second plot
