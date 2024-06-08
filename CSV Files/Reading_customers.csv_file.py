import csv;  # Import the csv module for handling CSV files

def main():
    try:
        # Open the CSV file in read mode with newline='' to handle different newline conventions across platforms
        with open('D:\\Python\\csv\\customers.csv', newline='') as file:
            # Use csv.reader to read the file and specify the delimiter as ','
            file = csv.reader(file, delimiter=',');
            
            # Iterate over each row in the CSV file
            for items in file:
                # Print each row
                print(items);
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the main function to execute the code
main();
