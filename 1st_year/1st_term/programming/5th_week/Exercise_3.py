#This program tells the perfects numbers till the input number
#Ask for input
from math import sqrt

inp = int(input("Input an integer: "))

#Check all the chars of the string if they are numbers or not
for check_number in range(inp):

    #check if the element is 0 or 1 because it would cause an error 
    #(divide by 0 and 1 will cause an error in the sum) 
    if ( check_number != 0 and check_number != 1):
        controller = 0

        #Loop to check if a number is a perfect one
        for i in range(int(sqrt(check_number)) + 1):
            if(i != 0):
                if (((check_number % i) == 0) and i != 1):
                    controller += i + (check_number / i)

        #This is the proof of a number to be perfect
        if((controller + 1) == check_number):
            print("The number ", check_number, " is perfect")