#Using function nditer to iterate over the array 

print('Printing 1 dimensional array----')
print()
#for 1 dimensional array
arr1=np.array([1,2,3,4,5])
print(f'Printing {arr1}---')
print()
for items in np.nditer(arr1): 
    print(items); 
    print()
print('Printing 2 dimensional array-----')
print()
#for 2 dimensional array 
arr2=np.array([[1,2,3,4,5],
               [6,7,8,9,10]]); 
print(f'Printing {arr2}------')
print()
for i in np.nditer(arr2):
    print(i);
print()
print('Printing 3 dimensional array------')
print()
#for 3 dimensional array 
arr3=np.array([[[1,2,3,4,5],
               [6,7,8,9,10]],
               [[11,12,13,14,15], 
               [16,17,18,19,20]]]); 
print(f'Printing {arr3}------'); 
print()
for a in np.nditer(arr3): 
    print(a);
