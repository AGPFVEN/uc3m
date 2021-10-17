import random

#Ask for a value, it is assumed that the user will enter an int correctly
inp = int(input("Enter an integer: "))
total = 0

#Loop to check if the integer is positive
while (inp < 0):
    inp = int(input("Enter a valid positive integer: "))

#Loop to fill the list with random values
list_1 = []
for i in range(inp):
    list_1.append(random.randrange(1,50))
    total += list_1[i]

print(list_1, "\n", total)