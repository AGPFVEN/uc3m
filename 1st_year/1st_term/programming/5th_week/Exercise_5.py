import random

#Generate random pin and account balanace
pin = str(random.randrange(1000, 10000))
print(pin)
balanece = int(random.randrange(50, 5001))

#Request for the first time the pin
inp = input("Enter your pin: ")
if (inp == pin):
    print("Your balance is: ", balanece)
    exit()

else:
    for i in range(2):
        inp = input("Your pin is incorrect, try again: ")

        if(inp == pin):
            print("Your balance is ", balanece)
            exit()

print("You failed too many times")