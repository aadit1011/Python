#To delete the items in set
#Using remove and discard methods

sets={'January','February','March','April','May','June','July','August','September','October','November','December'};
def Using_Remove(para1):
          if para1 in sets:
               sets.remove(para1);
               print(f'{para1} has been successfully removed from the list.');
          else:
               print(f'{para1} does not exits in the list.')
          
def Using_Discard(para1):
      if para1  in sets:
          sets.discard(para1);
          print(f'{para1} has been successfully discarded from the list.');
      else:
           print(f'Items {para1} does not exits in the list.');


Using_Remove('January');
#Throws error when non existing items are tried to remove from the list
Using_Remove('Baisakh');
Using_Discard('February');
#But using discard method if non existing items are tried to remove from the list it handles the case without throwing an error

Using_Discard('Asad');

#Using clear function to delete whole set
sets.clear();
if sets==True:
     for items in sets:
          print(items);
          
else:
     print('Already deleted....');

sets2={'January','February','March','April','May','June','July','August','September','October','November','December'}; 
#Removes an item everytime it is used
sets2.pop();
print(sets2);
#To empty the whole set
sets2.clear();
print(sets2);
