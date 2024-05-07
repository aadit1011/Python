#Using Function that takes address default value in case where parameter is not provided.

def function(name,email,number,address='Pepsicola'):
     nam=f"Your name is {name}";
     add=f'Your address is {address}';
     num=f"Your number is {number}";
     ema=f"Your email is {email}";
     
     return nam, add, num, ema;


def main():
     name=input("Please enter your name=");
     # address=input("Please enter your address=");
     email=input("Please enter your email=");
     number=int(input("Please enter your number="));
     nam, add, num, ema=function(name,email,number);
     print(nam);
     print(add);
     print(num);
     print(ema);
     
     
main();

#Setting the parameters values in different ways......Using keyword argument method
def add(a,b):
     print("A=",a);
     print("B=",b);
     
add(b=5,a=2);

add(a=13,b=16);

#Function with variable length argument.....
#*args and **kargs
def function(*args_list):
     ans=[];
     for i in args_list:
          ans.append(i);
     return ans;

obj=function("Aadit Sharma",'Bhaktapur','Dubai','Boca Raton','Miami','Bel Air');
print(obj);
def function(**kargs_list):
     ans=[];
     for key,value in kargs_list.items():
          ans.append([key,value]);
     return ans;

obj=function(Name="Aadit",Address="Dubai",Number=92148392213);
print(obj); 

#OR
def function(*list):
     name=[];
     for i in list:
          name.append(i);
     return name;

print(function("Aadit",'Bipin','Ankit','Biyash'));

def function2(**list2):
     detail=[];
     for i,j in list2.items():
          detail.append([i,j]);
     return detail;
print(function2(Name="Aadit Sharma",Address="Dubai",City="Abu"));
