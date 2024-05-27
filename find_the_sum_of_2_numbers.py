def main():
     x=input("x=");
     y=input("y=");
     # choice=input("Enter\n1 for addition\n2 for subtraction\n3 for division \n 4 for multiplication=");

     sum=int(x)+int(y);
     sum=round(sum);

     if(sum>=1000): 
          #this helps to separate the certain digits of the number if they exceed 1000 
          print(f"{sum:,}");
     else:
          print(f"{sum}");

