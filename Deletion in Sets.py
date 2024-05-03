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
