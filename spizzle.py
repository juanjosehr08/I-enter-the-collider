#spizzle v.0.1
import random
print("Welcome to spizzle!v.0.1")
a = input("Insert First Name: ")
b = input("Insert Second Name: ")
c = input("Insert Third Name: ")



def insertName(theName):
    if theName == 1:
        return a 
    if theName == 2:
        return b
    if theName == 3:
        return c
print("YOUR CHOICE IS", insertName(random.randint(1,3)).upper(), "YAY!!!")

