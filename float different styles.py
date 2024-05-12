x=float(input("x="));
y=float(input("y="));
div=x/y;
#To print two numbers after .(dot)
print(f"{div:.2f}");
#To print just two numbers after .(dot)
div=round(div,2);
print(f"{div}");
# To print 3 numbers after decimal points
print(f"{div:.3f}");
#To print just three numbers after .(dot)
div=round(div,3);
print(f"{div}");