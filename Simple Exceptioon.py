try:
        num=int(input("Enter value of x?="));
        print(f"x value is {num}");
except ValueError:
        print("Please enter a integer value....");
#Also using else along 
try:
        num=int(input("Enter value of x?="));
except ValueError:
        print("Please enter a integer value....");
else:
        print(f"x value is {num}");
        
