detail={'Name:Aadit Sharma','Roll number:21012323','Address:Pepsicola'};
for items in detail:
    print(items);
    
#Example 2
#This is the valid way to create set
example2={1,2,3,4,"Aadit Sharma",'Pepsicola'};

try:
     for items in example2:
          print(items);  
except Exception:
     print("Sets cannot contain mutable elements"); 
else:
     print("Sets can only contain immutable elements");

