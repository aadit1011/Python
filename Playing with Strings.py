detail='Aadit Sharma Pepsicola DataScience&Dance';
#To split the string when white space
first_name, last_name, address, life=detail.split(" ");
print(first_name, last_name, address, life,sep=", ");
detail=detail.replace("Pepsicola", "Dubai-AbuDhabi");
first_name, last_name, address, life=detail.split(" ");
print(first_name, last_name, address, life,sep=", ");
#To capitalize the string 
first_name=first_name.capitalize();
print(first_name,sep=', ');

last_name=last_name.capitalize();
print(last_name,sep=', ');
