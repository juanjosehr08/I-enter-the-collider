#spizzle v.0.1
import random
print("Welcome to spizzle!v.0.1")
print("Please insert characters then type done")
count = 0
i = list()
while True:
    name = input("Insert name:")
    if name == "done":
        break
    i.append(name)
    x = len(i)
    ok = i[:]
    
#solution:
the_solution = random.choice(ok)
print("YOUR CHOICE IS", the_solution.upper(), "YAY!!!")