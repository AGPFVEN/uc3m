#Ask for a "number" and declaring a controller variable to check if the input is not a number
inp = input("Enter a number: ")
controller = True

#Loop to check is the input is not a number
for number in inp:
    if(number.isdigit() == False):
        controller = False

#loop to try again
while(controller != True):
    inp = input("You entered a wrong input, input a real number: ")
    controller = True
    for number in inp:
        if(number.isdigit() == False and number != "."):
            controller = False

#Result of the program
print("The square of ", inp, " is ", float(inp) ** 2)