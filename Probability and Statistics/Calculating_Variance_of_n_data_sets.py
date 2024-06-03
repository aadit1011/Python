# Initialize global variables for variance, mean, and data list
variance = 0
mean = 0
data = []

def main():
    """
    Main function to input the data sets and trigger the variance calculation.
    """
    # Get the number of data sets from the user
    n = int(input("Enter the number of data sets: "))
    
    # Loop to collect data values from the user
    for i in range(n):
        value = int(input(f"Enter the {i+1} data set: "))
        data.append(value)
    
    # Call the function to calculate the variance
    calculateVariance()
    
def calculateVariance():
    """
    Function to calculate the variance of the data sets.
    """
    # Declare global variables to modify them inside the function
    global variance
    global mean
    global data
    
    # Calculate the mean of the data sets
    mean = sum(data) / len(data)
    
    # Calculate the sum of the squared differences from the mean
    for i in range(len(data)):
        variance += (data[i] - mean) ** 2
    
    # Divide by the number of data points to get the variance
    variance = variance / len(data)
    
    # Print the calculated variance
    print(f"The variance of the given data sets is {variance}")

# Call the main function to start the program
main()
