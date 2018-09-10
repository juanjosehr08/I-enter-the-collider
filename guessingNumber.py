#asking for a guess
print("Hello Pal, Whats your name?")
name = input(">")
print("Well", name, "I was thinkling in a game between 1 to 20. Can you guess?")
import random
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    try:
        print("take a guess:")
        guess = int(input(">"))
    except:
        print("please add an integer")
        continue
        
    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    elif guess != int(secretNumber):
        print("Sorry you took too many guesses")
    else:
        break #this condition is for the good guess.
       
try:        
    if guess == secretNumber:
        print("Good Job!", name)
        print("you guess my number in", str(guessesTaken), "guesses") 
    else: 
        print("Sorry you took too many guesses")
        print("the number I was thinking of was", str(secretNumber))   
except:
    quit()