# Import the seaborn library, which is used for creating statistical graphics.
import seaborn as sbn

# Import the matplotlib library, which is used for plotting graphs. 'pyplot' is a module for MATLAB-style plotting.
import matplotlib.pyplot as plt 

# Load the 'iris' dataset into the variable 'data'. This dataset is built into seaborn and contains measurements of iris flowers.
data = sbn.load_dataset('iris')

# Create a line plot using seaborn. The x-axis is set to 'sepal_length', and the y-axis is set to 'sepal_width' from the 'data' dataset.
sbn.lineplot(x='sepal_length', y='sepal_width', data=data)

# Display the plot using matplotlib's 'show' function.
plt.show()
