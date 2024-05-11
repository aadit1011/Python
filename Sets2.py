detail=set();

question=['Name','Age','Gender','Address'];

def main():
     global detail;
     for i in range(len(question)):
          detail.add(f'{question[i]}='+input(f"{question[i]}="));
     display();

def display():
      print(detail);
          
main();