#To create file 
#TO store the user input details
detail=[];
#To store the respective user input questions
question=['Name','Address','Phone Number','Email'];
#To create new file or write inside the file
with open('D:\\Python\\hello.txt','w') as file:
     for i in range(len(question)):
          detail.append(input(f"Please enter your {question[i]}="));
          store=f"Your {question[i]} is {detail[i]}\n";
          file.write(store);
          
#To write content inside any existing file in the desired location
with open('hi.txt','w') as file:
     name="Hey it's the text inside from the hi file";
     file.write(name);

#If in any other  location than working directory then the full path of the file should be given..     

#To read contents inside of file from a location
with open('content.txt','r') as file:
     inside=file.read();
     print(inside);