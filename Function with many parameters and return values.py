#Taking many parameters and multiple returning
def performing(a,b,c,d,e,f):
          adding_all=a+b+c+d+e+f;
          subtracting_all=a-b-c-d-f-e-f;
          multiplying_all=a*b*c*d*e*f;
          return adding_all,subtracting_all,multiplying_all;
       
def main():
          print('Please Enter a,b,c,d,e,f=');
          a=int(input("a="));
          b=int(input("b="));
          c=int(input("c="));
          d=int(input("d="));
          e=int(input("e="));
          f=int(input("f="));
          add, sub, mul=performing(a,b,c,d,e,f);
          print("addition= ",add);
          print("subtraction= ",sub);
          print("multiplication= ",mul);
          
          
main();
          