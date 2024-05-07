#Set difference 
seta={'Aadit','Bardan','Ankit','Roshan','Bipin','Biyash'};
setb={'Prijal','Nabin','Abhishek','Biyash'};
      
print(seta-setb);

#set difference in another way
setp={'Apple','mango','Banana','Grapes'};
setq={'Apple','tomato','Banana'};
print(setp-setq);

#Frozen sets
set_frozen=frozenset({'Aadit','Pepsicola','Tohoma'});
try:
     set_frozen.add('Bardan');
     
     
except Exception:
     print('Frozen sets cannot be updated.')
else:
     print('Updated Successfully');
     
for items in set_frozen:
          print(items);