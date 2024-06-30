class Animal:
    def __init__(self): 
        self.name=None 
        self.catagory=None
    def ask(self):
        self.name= input('Enter the animal name=')
        self.catagory= input('Enter the catagory of animal=')
    def show(self):
        print(f'Name={self.name}\nCatagory={self.catagory}')
        
my_dog=Animal()
my_dog.ask()
my_dog.show()
