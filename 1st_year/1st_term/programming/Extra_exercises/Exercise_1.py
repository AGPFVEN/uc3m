import random

#Print list
def print_list(ls:list):
    #Creating empty string
    final_string = "The generated list is: \n "

    #Loop the list to enter values in string
    for i in ls:
        final_string += " " + str(int(i))

    print(final_string)

#Return random list in a range
def partially_random(length:int, start:float, final:float):
    #Initializing empty list
    ls = []

    #Loop to fill the list
    for _ in range(length):
        ls.append(random.uniform(start, final))

    #Print list
    print_list(ls)

    #Return list
    return ls

def fully_random():
    #Random length of list
    length = random.randint(1, 1000)

    #Start of random range of list (included)
    start = 1

    #End of random range of list (excluded)
    final = 1000

    return partially_random(length, start, final)

def manual_filling():
    #Initialize empty list
    ls = []

    #Input length of list
    length = int(input("Input the number of elements of the wanted list: "))

    #Loop to let the user fill the list
    for _ in range(length):
        ls.append(int(input("Input a number for your list: ")))

    return ls

def shrink_by_adding(ls:list):
    #Initializing resulting list
    final_ls = []

    #Aux variable to check if the list is even or odd
    odd = False

    #If the list is odd exctract the last number
    if (len(ls) % 2 != 0):
        last_value = ls.pop(len(ls) - 1)
        odd = True

    #As the list now must be even, I can treat them all the same
    #The approach is to keep adding until the list is empty
    while (ls != []):
        final_ls.append(ls[0] + ls[1])
        del ls[0], ls[0]
    
    #This is done because I considered that if the list is even, the last value must be the last one
    if(odd):
        final_ls.append(last_value)

    #Print list
    print_list(final_ls)

    return final_ls

def invert_list(ls:list):
    #Initializing empty list
    final_ls = []

    #Loop to invert list
    for _ in range(len(ls)):
        final_ls.append(ls[-1])
        del ls[-1]
    
    print_list(final_ls)

    return final_ls

#Actual Program-------------------------
option = int(input("""How do you want to fill the list?
1)  Partially random
2)  Totally random
3)  Manual \n"""))

#Loop to check if the option selected is valid
while(option < 1 or option > 3):
    option = int(input("Please, enter 1, 2 or 3! \n"))

#Option 1
if option == 1:
    #Input length of list
    length = int(input("Enter the number of elements\n"))

    #Input upper bound
    upper_bound = int(input("Enter the upper bound\n"))

    #Input lower bound
    lower_bound = int(input("Enter lower bound\n"))

    #Create list
    ls = partially_random(length, upper_bound, lower_bound)

elif option == 2:
    #Create random list
    ls = fully_random()

elif option == 3:
    #Create manual list
    ls = manual_filling()

option = ""

while option != "C":

    option = input("""Enter an option: 
    A)  Shrink the list
    B)  Invert the list
    C)  Quit\n""")

    accepted_options = ["A", "B", "C"]

    while not (option in accepted_options):
        option = input("Input a valid option: \n")

    if(option == "A"):
        ls = shrink_by_adding(ls)
    
    if(option == "B"):
        ls = invert_list(ls)

print("Thanks")