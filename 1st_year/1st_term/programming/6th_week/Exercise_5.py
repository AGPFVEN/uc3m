from math import pi
import random

print("Think about a number between 1 and 100")

#Initializing my variables
tried = []
guess = 1
inp = ""

#Loop till guessed or there are no more numbers left
while (inp != "y"):

    if(len(tried) < 99):

        print(tried.count(guess) == 0)
        #Generate a number till it is not on the list of tried ones
        while(tried.count(guess) != 0):
            guess = random.randrange(1, 101)
    
        #Question
        inp = input(str(str(guess) + " Is your number (y/n): "))
        tried.append(guess)
    
    else:
        inp = "y"
        print("You are lying")