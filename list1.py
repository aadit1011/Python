students=["Aadit","Bardan","Max","Henry","Carthford"];
house=["Red","Green","Blue","Yellow","Purple"];

for student in students:
                    print(student);
#To print students along with their respective houses......                 
for i in range(len(students)):
               print(f"{i+1}.{students[i]} belongs to {house[i]} house.");
               
