import random

#Generate random pin and account balanace, I print the pin because of testing purposes
pin = str(random.randrange(1000, 10000))
print(pin)
balanece = int(random.randrange(50, 5001))

#Request for the first time the pin
inp = input("Enter your pin: ")

#this will happen if the pin is incorrect
if (inp != pin):
    for i in range(2):
        inp = input("Your pin is incorrect, try again: ")

        if(inp == pin):
            break

#This will happen if you are out of tries and still have the wrong pin
if (inp != pin):
    print("You tried too many times")

#The code of the operations will be executed if you input the correct pin
else:
    operation_inp = input("""
Welcome
----------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation: """)

    #If the input is 3 the program of operations won't be continued
    while (operation_inp != "3"):

        #The first operation will be deposit
        if (operation_inp == "1"):
            deposit = float(input("Input the deposit you want to introduce: "))
            
            #I check that the number is not negative, because it should be in cash withdrawal
            while (deposit < 0):
                deposit = float(input("Input a positive number: "))

            #Actual deposit
            balanece += deposit
            print("Your balance is: ", balanece, "€")

            #Next operation
            operation_inp = input("""
Which operation you want to perform now
----------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation: """)

        if (operation_inp == "2"):
            withdrawal = float(input("Input the deposit you want to introduce: "))
            
            #I check that the number is not negative, because it should be in deposit, or the quantity is too high
            while (withdrawal < 0 or withdrawal >= balanece):
                withdrawal = float(input("Invalid withdrawal, try again: "))

            #Actual deposit
            balanece -= withdrawal
            print("Your balance is: ", balanece, "€")

            #Next operation
            operation_inp = input("""
Which operation you want to perform now
----------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation: """)