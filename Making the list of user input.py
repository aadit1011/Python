quest=[];
question=['username','address','email','password'];
for i in range(0,4):
          quest.append(input(f"Please Enter your {question[i]}::"));
          
for i,j in zip(question,quest):
     print(i+'='+j);