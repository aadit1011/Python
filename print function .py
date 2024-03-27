#Prints 2 different print function on different lines 
name=input("Name= ");
print("Name is "+name,);
print("This is in different lines");

#Prints 2 different print function on same line

print("Name is "+name,end=' ');
print("This is on same line");

#Using Special String
print(f"Name is {name}");

#Using seprator explicitly
print("Name is",sep=" ");

name="Varun";

#Using Sep to separate here sep=2 whitespace
print("Name is",name,sep='  ');
