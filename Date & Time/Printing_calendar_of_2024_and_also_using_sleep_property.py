import calendar  # Importing the calendar module to work with dates
import time  # Importing the time module to introduce delays

# Loop through each month from 0 to 11 (which corresponds to January to December)
for i in range(0, 12):
    # Print the calendar for each month of the year 2024
    # `i+1` is used because months are 1-indexed (1 for January, 2 for February, etc.)
    print(calendar.month(2024, i+1))
    
    # Introduce a delay of 5 seconds before printing the next month's
    time.sleep(5)

#printing the calendar of the whole year.
print(calendar.prcal(2023));
