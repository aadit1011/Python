import numpy as np  # Import NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib library for plotting

# Define an array of angles (in radians)
angle = np.array([0, np.pi/2, np.pi])

# Calculate the sine and cosine of the angles
value1 = np.sin(angle)
value2 = np.cos(angle)

# Print the calculated sine and cosine values
print("Sine values:", value1)
print("Cosine values:", value2)

# Plot sine vs cosine values
plt.plot(value1, value2, label='sin vs cos')  # Plot the sine values against the cosine values
plt.xlabel('value')  # Set the x-axis label
plt.ylabel('sine(value),cos(value)')  # Set the y-axis label

# Calculate the exponential of the angles
expon = np.exp(angle)
print("Exponential values:", expon)

# Plot the exponential values
plt.plot(angle, expon, label='exp')  # Plot the exponential values against the angles
plt.xlabel('value')  # Set the x-axis label
plt.ylabel('exp(value)')  # Set the y-axis label

# Add a legend to the plot for better understanding
plt.legend()

# Display the plot
plt.show()
