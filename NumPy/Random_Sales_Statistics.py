# Sales Data Analysis for a Shop
# This program analyzes the sales data for jackets and sneakers sold in a shop
# It generates random sales data, calculates various statistics, and prints a summary report

import numpy as np
import time

# Get the current year and time
current_year = time.localtime().tm_year
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Take input for shop name and number of items sold
shop_name = input('Enter your shop name=')
nj = int(input('Enter the total number of jackets sold this year='))
ns = int(input('Enter the total number of sneakers sold this year='))

# Generate random sales data for jackets and sneakers
sales_jacket = np.random.randint(100000, 200000, size=nj)
sales_snickers = np.random.randint(100000, 1000000, size=ns)

# Convert sales data to numpy arrays
sales_jacket = np.array(sales_jacket)
sales_snickers = np.array(sales_snickers)

# Calculate total sales, min, and max for jackets and sneakers
sum_jacket = np.sum(sales_jacket)
sum_snickers = np.sum(sales_snickers)
min_jacket = np.min(sales_jacket)
min_snicker = np.min(sales_snickers)
max_jacket = np.max(sales_jacket)
max_snicker = np.max(sales_snickers)

# Concatenate the sales data of jackets and sneakers
join = np.concatenate((sales_jacket, sales_snickers))

# Print the shop name and current time
print()
print(f'..........................{shop_name}............................')
print(f'Current Date and Time: {current_time}')
print()
print()

# Print the sales information for jackets
print('For Jackets')
print()
print(f'The total number of jackets sold this year was {nj}.')
print()
print(f'The total worth of jackets sold this year was Rs. {sum_jacket}')
print()
print(f'The jacket sold with the lowest price was Rs. {min_jacket}')
print()
print(f'The jacket sold with the maximum price was Rs. {max_jacket}')
print()
print(f'The total number of jackets priced Rs. {max_jacket} sold this year was: {np.sum(sales_jacket == max_jacket)}')
print()

# Print the sales information for sneakers
print('For Sneakers')
print()
print(f'The total number of sneakers sold this year was {ns}')
print()
print(f'The total worth of sneakers sold this year was Rs. {sum_snickers}')
print()
print(f'The sneaker sold with the lowest price was Rs. {min_snicker}')
print()
print(f'The sneaker sold with the maximum price was Rs. {max_snicker}')
print()
print(f'The total number of sneakers priced Rs. {max_snicker} sold this year was: {np.sum(sales_snickers == max_snicker)}')
print()

# Calculate the total sales of jackets and sneakers combined
join_sum = np.sum(join)
print(f'The total sales done by {shop_name} in the year {current_year} is Rs. {join_sum}')
