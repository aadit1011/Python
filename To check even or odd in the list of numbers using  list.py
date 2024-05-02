numbers=[];
check=[];
even_num=[];odd_num=[];
set=int(input('Enter the total sets of numbers you want to check even and odd::'))
for _ in range(set):
     numbers.append(int(input('Please ENter the numbers to find odd or even::')));

for i in range(len(numbers)):
     if int(numbers[i])%2==0:
          even_num.append(numbers[i]);
          check.append('e');
     else:
          odd_num.append(numbers[i]);
          check.append('o');
          
even=check.count('e');
odd=check.count('o');
print(f'In your list, there were {even} even numbers and {odd} odd numbers.');

print('In your list the even numbers were:');
for num in even_num:
     print(num);

print('In your list the odd numbers were:');
for nums in odd_num:
     print(nums);