list1=['Aadit','Bipin','Ankit','Biyash'];
#Repetition in list
list1=list1*2;
for item in list1:
     print(item);
     

#Concatenation in List
list2=['Name:Aadit','Email:vardanshiwakoti123@gmail.com'];
list3=['Address:Pepsicola','Mobile Number:9863034804'];
detail_list=list2+list3;
for _ in detail_list:
     print(_);
     
#Finding the Length of the list
list4=['Name:Aadit Sharma','Number:9863034803','Roll number:210108','Email:vardanshiwakoti123@gmail.com'];
num=len(list4);
print(num);
#Lenght is the sum of length of all the items inside the list4
length=0;
for items in list4:
     length+=len(items);

print(length);