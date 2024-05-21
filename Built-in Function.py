#Using absolute function.
#abs()
def main():
     num=int(input("Enter number="));
     numb=abs(num);
     print(f'The absolute value of {num} is {numb}');
     
main();


#Using eval function
#eval()

def main():
     operation=input('Please Input the mathematical operation you want to perform=');
     operation=eval(operation);
     print(f'The final result of the operation you performed is:{operation}')
     
main();

#Using exec function..
#exec()

operation1='''
num1=int(input('Enter the a='));
num2=int(input('Enter the b='));
sum=num1+num2;
print(f'The sum of two numbers {num1} and {num2} is:{sum}')
''';
exec(operation1);

