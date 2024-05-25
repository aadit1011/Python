#Using anonymous function
#Also known as lambda function
def main():  
     number=int(input('Please!Enter a number='));
     num=int(input('Please Enter another number='));
     add=lambda number, num:number+num;
     sub=lambda number,num:number-num;
     mul=lambda number,num:number*num; 
     print('Add=',add(number,num));
     print('Sub=',sub(number,num));
     print('Mul=',mul(number,num));
     
     
main();
