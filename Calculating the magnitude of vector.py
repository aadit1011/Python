#Calculating the magnitude of the vector in math..
import math;

def magnitude():
     val1, val2=input('Enter the magnitudes of the vector=').split();
     val1=int(val1); val2=int(val2);
     magnitud=math.sqrt(val1**2+val2**2);
     magnitud=abs(magnitud);
     return magnitud, val1, val2;
     
def main():
     value, val1, val2=magnitude();
     print(f'The magnitude of the vector {val1} and {val2}={value}');
     
main();  
