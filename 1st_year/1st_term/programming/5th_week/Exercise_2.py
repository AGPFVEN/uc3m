import random

#Asking for values 
first_value = int(input("Enter two integers that between them should minimum 5 numbers:\n"))
second_value = int(input())

#loop for invalid values
while ((abs((first_value - second_value))) < 5):
    first_value = int(input("Your values are not valid, try again:\n"))
    second_value = int(input())

print("\nThis are our random values alternating them between even or odd")

#This will be my approach, I will take a random value until it is even or odd and then print it
result = random.randrange(first_value, second_value + 1)
while (result % 2 != 0):
    result = random.randrange(first_value, second_value + 1)

print(result)

#Do it two times so it will print 4 values and the fifth is the previous one
for i in range(2):
    
    result = random.randrange(first_value, second_value + 1)
    while (result % 2 == 0):
        result = random.randrange(first_value, second_value + 1)

    print(result)

    while(result % 2 != 0):
        result = random.randrange(first_value, second_value + 1)

    print(result)