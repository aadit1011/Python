#To add 2 numbers
def add(num1,num2):
               result=num1+num2;
               return result;
#to subtract two numbers
def subtract(num1,num2):
               result=num1-num2;
               return result;
 #to multiply two numbers
def multiply(num1,num2):
               result=num1*num2;
               return result;
          
def division(num1,num2):
                    result=num1/num2;
                    return result;
def square(num):
            result=pow(num,2);
            return result;
def cube(num):
            result=pow(num,3);
            return result;
def squareRoot(num):
            result=pow(num,0.5);
            return result;

def remainder(num1,num2):
            result=num1%num2;
            return result;

while(1):               
                  x=int(input("x="));
                  y=int(input("y="));
                  choice=int(input("Enter\n1 for addition\n2 for subtraction\n3 for division \n4 for multiplication\n5 to find square of numbers\n6 to calculate the cube of numbers\n7 to calculate the square root of numbers\n8 to calculate the remainder\n9 to exit="));               
                  if(choice==1):
                        print(f"The sum of {x}and {y}is={add(x,y):,}");
                  elif(choice==2):
                        print(f"The difference of {x} and {y}={subtract(x,y):,}");
                  elif(choice==3):
                        print(f"The value after {x} is divided by {y}={division(x,y):,}");
                  elif(choice==4):
                        print(f"The multiplied value of {x} and {y}={multiply(x,y):,}");   
                  elif(choice==5):
                        print(f"The square of {x} is {square(x)} and {y} is {square(y):,}");
                  elif(choice==6):
                        print(f"The cube of {x} is {cube(x)} and {y} is {cube(y):,}");
                  elif(choice==7):
                        print(f"The square root of {x} is {squareRoot(x)} and {y} is {squareRoot(y):,}");
                  elif(choice==8):
                        print(f"The remainder of {x} and {y} is {remainder(x,y):,}");
                  else:
                        exit(0);


