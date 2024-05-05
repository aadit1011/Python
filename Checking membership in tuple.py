#Tuples Membership test
membership_in_zym=('Aadit','Bardan','Bipin','Biyash','Ankit','Roshan');
small=[];

name=input('Enter the name to check membership for')
name=name.capitalize();
#Using value in tuple way to find membership
value=(name in membership_in_zym);
if value==True:
     print(f'{name} is a member of the membership list.')
else:
     print(f'{name} is not a member of the membership list.')
