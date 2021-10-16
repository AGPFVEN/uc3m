import random

#Create the list of 20 elements
list_1 = []
for i in range(20):
    list_1.append(random.randrange(1, 10))

#Input
inp = int(input("Input an integer between 1 and 9 (1 and 9 included): "))

#Make sure that inp is inside of the valid range
while (inp < 0 or inp > 10):
    inp = int (input("Input a valid integer"))

#Print the positions where it appears on the list
if (list_1.count(inp) != 0):
    for i in range(len(list_1)):
        if(list_1[i] == inp):
            print(inp, " is located in position: ", i)
else:
    print("Your number is not on the list")