import matplotlib.pyplot as plt  # Import the matplotlib library for plotting graphs and charts
import numpy as np  # Import numpy for numerical operations, especially useful for generating random numbers

# Data for the pie chart
# Updated data for the pie chart
number = [15, 25, 35, 10, 5, 10]  # List representing the size of each slice in the pie chart
name = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig']  # New labels for each slice of the pie chart
exp = [0, 0, 0.1, 0, 0, 0]  # 'explode' parameter to offset the slices; the third slice  is slightly offset

l = len(name)  # Calculate the number of slices based on the length of the 'name' list

# Generate random integers to use as color indices for the pie chart
c = np.random.randint(0, 101, l)  # Generates 'l' random integers between 0 and 101 for color mapping

# Map the random integers to colors using the 'plasma' colormap
c = plt.cm.plasma(c)  # Converts the random integers to RGBA color values using the 'plasma' colormap

# Create the pie chart with the specified parameters
plt.pie(number, explode=exp, labels=name, colors=c)  # 'number' defines the size of each slice, 'explode' adds space between slices, 'labels' defines the slice names, and 'colors' defines the slice colors

# Display the pie chart
plt.show()  # Show the pie chart plot to the screen
