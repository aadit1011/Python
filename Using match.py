x=int(input("Enter x="));
y=int(input("Enter y="));
choice=int(input("Enter\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 to exit"));
match choice:
          case 1:
                add=x+y;
                print(f"The sum of {x}and {y}is={add}");
                
          case 2:
                sub=x-y;
                print(f"The difference of {x} and {y}={sub}");
                
          case 3:
                mul=x*y;
                print(f"The value after {x} is multiplied with {y}={mul}");
                
          case 4:
                div=x/y;
                print(f"The  value of {x} when divided by {y}={div}");   
                
          case 5:
                exit();
          case _:
               print("Please Enter the Correct choice Value......");
