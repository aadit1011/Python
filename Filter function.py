#Using filter function  to filter EVEN numbers from the list of numbers
list_numbers=[];
even_number=[];
def even_calculator(num):
     if num%2==0:
          return num;
quantity=int(input('Please Enter the number of numbers to filter='));
for _ in range(quantity) :
     list_numbers.append(int(input(f'Please Enter the {_+1} number=')));


even_number=list(filter(even_calculator,list_numbers));   
           
print('In your list of supplied numbers there were following even numbers=');

for p in range(len(even_number)):
     print(even_number[p]);
     
     
