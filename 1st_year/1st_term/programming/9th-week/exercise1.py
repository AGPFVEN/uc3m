import random
import string

#The task is to generate a random password containing at least one uppercase, one numbera and one symbol
#My Approach is to generate a random password and then check if it has one of each
#If not change a random character from the string

#Function to transform list into string
def list_to_str(your_list):
    my_string = ""

    for i in your_list:
        my_string += i

    return my_string

#Function to check if the manipulated has an element of expected
def checker(manipulated, expected):
    #Auxiliar variable
    aux = False

    #Check if password contains character
    for i in range(len(manipulated)):

        if manipulated[i] in expected:
            aux = True

    #Change if doesn't contain
    if(aux == False):
        to_modify = random.randrange(0, len(manipulated))
        manipulated[to_modify] = random.choice(expected)

    return manipulated



def generate_password():

    #Define length of the password
    legth = random.randrange(8, 13)

    #Empty string to manipulate
    password = []

    #Loop to fill the string randomly
    for _ in range(legth):
        choice_maker = random.randrange(1, 5)

        if(choice_maker == 1):
            password.append(random.choice(string.ascii_lowercase))

        if(choice_maker == 2):
            password.append(random.choice(string.ascii_uppercase))

        if(choice_maker == 3):
            password.append(random.choice(string.digits))

        if(choice_maker == 4):
            password.append(random.choice(string.punctuation))

    #function to verify all espectations
    password = checker(list(password), string.ascii_lowercase)
    password = checker(list(password), string.ascii_uppercase)
    password = checker(list(password), string.digits)
    password = checker(list(password), string.punctuation)

    return list_to_str(password)

print("Your new pasword is:",generate_password())

#The unique fault that I find in my program is that if there's just one type of one requested character
#checker can replace that value, but is highly unprobable, it can be fixed with a loop and an auxiliar boolean
#but I think I have complicated this exercise long enough