import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot library for plotting

# Data for the outer pie chart
x = [10, 20, 15, 5, 30, 18, 2]  # Values for each slice of the outer pie chart
y = [20, 30, 50]  # Values for each slice of the inner pie chart
name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # Labels for the slices of both pie charts

# Plot the outer pie chart
plt.pie(x, radius=1.5, labels=name)  # 'x' values are used for the outer pie chart; radius is set to 1.5 to make it larger

# Plot the inner pie chart
plt.pie(y, radius=1, labels=name[:3])  # 'y' values are used for the inner pie chart; radius is set to 1 to make it smaller
# 'name[:3]' is slicing the first three labels ('A', 'B', 'C') for the inner pie chart

plt.show()  # Display the concentric pie charts
