import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot library for plotting

# Data for the pie chart
x = [10, 20, 15, 5, 30, 18, 2]  # Values for each slice of the pie chart
name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # Labels for each slice

# Plot the main pie chart
plt.pie(x, radius=1.5, labels=name)  # Create a pie chart with a larger radius of 1.5 to form the outer circle

# Plot an inner white pie chart to create a "donut" or ring effect
plt.pie([1], radius=1, colors='white')  
# A second pie chart with a single slice (value of 1) and a radius of 1
# The 'colors' parameter is set to 'white' to match the background, creating a hole in the middle

# Display the pie chart
plt.show()  # Render and display the ring (donut) pie chart
