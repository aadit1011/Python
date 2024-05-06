#Unions in set
set1={"Aadit Sharma",'Pepsicola',210108};
set2={9841917760,9841760848,986303483,9860503130};
set4={'Dubai','Nepal','Bel Air','Beverly Hills','Switzerland','Boca Raton'};
set3=set();
# set5=set();
set_all=set3.union(set1,set2);
# set5=set5.union(set3,set4);

print(set_all);
# print(set5);

#another way to find teh set union.
seta={'Aadit','Panaroma','Pramilla','Jenny'};
setb={'Max','Glenn'};
setc={'Harry','Shubham'};
print(seta|setb|setc);