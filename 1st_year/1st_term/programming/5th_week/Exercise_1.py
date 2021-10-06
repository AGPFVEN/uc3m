import random

#Generate a random number and ask for another one
number = random.randrange(1, 21)
n = int(input("Guess the secret number:\n"))

#Loop till the user guess the secret number
while (n != number):
    n = int(input("Bad luck... Try again:\n"))

print("Well done")