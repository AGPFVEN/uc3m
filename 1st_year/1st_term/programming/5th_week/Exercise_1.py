import random

number = random.randrange(1, 21)
n = int(input("Guess the secret number:\n"))

while (n != number):
    n = int(input("Bad luck... Try again:\n"))

print("Well done")