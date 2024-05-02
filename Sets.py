detail={'Name:Aadit Sharma','Roll number:21012323','Address:Pepsicola'};
for items in detail:
    print(items);
    
#Example 2
#This is the valid way to create a set
example2={1,2,3,4,"Aadit Sharma",'Pepsicola'};

try:
     for items in example2:
          print(items);  
except Exception:
     print("Sets cannot contain mutable elements"); 
else:
     print("Sets can only contain immutable elements");

#This creates an empty dictionary instead of creating an empty set
example1={};

#To create an empty set we can use set()
example2=set();

print('Type of example1-',type(example1),sep=': ');
print('Type of example2-',type(example2),sep=': ');
