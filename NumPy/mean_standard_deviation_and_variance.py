import numpy as np;  # Importing the NumPy library

# Taking input for lower limit, upper limit, and the number of trials
low, upp, trials = map(int, input('Enter the lower limit, upper limit and the total no. of trials=').split());

# Generating an array of random integers within the given range
arr = np.random.randint(low, upp, size=trials);

# Finding the maximum value in the array
maximum = np.max(arr);
print(f'Maximum = {maximum}');  # Printing the maximum value

# Finding the minimum value in the array
minimum = np.min(arr);
print();
print(f'Minimum = {minimum}');  # Printing the minimum value

# Calculating the sum of the array
add = np.sum(arr);
print(f'Sum of the data\'s are = {add}');  # Printing the sum of the array

# Calculating the mean of the array
means = np.mean(arr);
print();
print(f'Mean is {means}');  # Printing the mean value

# Initializing the value for variance calculation
value = 0;

# Looping through each element in the array to calculate the variance
for i in range(trials): 
    value = value + pow((arr[i] - means), 2);  # Calculating the squared difference from the mean

# Calculating the variance
variance = value / trials;
print(f'The variance of the data is {variance}');  # Printing the variance

# Calculating the standard deviation
sd = np.sqrt(variance);
print(f'The value of standard deviation is = {sd}');  # Printing the standard deviation
