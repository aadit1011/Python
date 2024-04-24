finalResult=0;
while True:
  try:
      a=int(input("Enter the value of a="));
      b=int(input("Enter the value of b="));
      choice=int(input("Enter\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for exit"));
      if choice==1:
                        finalResult=a+b;
                        print(f"The sum of {a} and {b} is {finalResult}.");
      elif choice==2:
                        finalResult=a-b;
                        print(f"The difference between {a} and {b} is {finalResult}");
      elif choice==3:
                        finalResult=a*b;
                        print(f"The difference between {a} and {b} is {finalResult}");
      elif choice==4:
                        print("Terminating the program.....");
                        break;
  except ValueError:
            print("Please Enter the integer value.......");
            