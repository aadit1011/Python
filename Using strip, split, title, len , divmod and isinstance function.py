
#to capitalize the string
name=input("Enter your name=");
name=name.capitalize();
name=name.strip();
num=len(name);
num=str(num);
print("Name is =" + name + " and your name has letters="+num,sep='',end='');
name=input("Enter your name again=");
name=name.title();
print("Your full name is="+name,sep='',end='');

# making it more short 
first,last=input("Enter your full name=").strip().title().split(" ");
num=len(first)+len(last);
num=str(num);
print("Hey!! "+first,sep='',end='\n');
print(f"Your name has {num} letters");

#Using split function to split address

address=input("Enter your address=");
city,street=address.split(" ");
print("You live in "+city+" city");

#Using divmod function to find division and remainder
num1,num2=divmod(15,2);
print(num1);
print(num2);

#Using isinstance function 
num=isinstance(5.4,float);
print(num);

name=isinstance("Aadit",str);
print(name);
