import random
import sys
import string

def asker_function():
    inp = int(input("Input a positive number between 1 and 10: "))

    while (inp < 0 or inp > 10):
        inp = int(input("Invalid input, input a positive number between 1 and 10"))

    return inp

def generate_password(length): # I reused code from last week

    #Empty string to manipulate
    password = []

    #Loop to fill the string randomly
    for _ in range(length):
        choice_maker = random.randrange(0, 2)

        if(choice_maker == 0):
            password.append(random.randrange(-(sys.maxsize), sys.maxsize))
        
        if(choice_maker == 1):
            password.append(random.uniform(-(sys.maxsize), sys.maxsize))
        
    return password

def find_minimum(ls):
    #Declaring variable
    minimum = ls[0]

    #Loop to locate the maximum
    for i in ls:
        if(i < minimum):
            minimum = i

    return minimum

#Test
result_ls = generate_password(asker_function())
print(result_ls, find_minimum(result_ls))