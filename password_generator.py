#Welcome to password generator by Aadit Sharma
import random
import string
password='';
def main():
    print("Welcome to password generator by Aadit Sharma");
    print("Let's start the password generation........");
    length=int(input("Enter the length of the password you want to generate="));
    finalValue=generate(length);
    print(finalValue+" is the randomly generated password..");

def generate(length):
        global password;
        char=string.ascii_letters+string.digits+',.!@#$%^&*()';
        for _ in range(length):        
                        password+=random.choice(char);
        return password;
main();
