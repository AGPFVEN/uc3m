#Ask for input
from math import sqrt

inp = int(input("Input an integer: "))

for check_number in range(inp):
    if ( check_number != 0 and check_number != 1):
        controller = 0

        #Loop to check if a number is a perfect one
        for i in range(int(sqrt(check_number)) + 1):
            if(i != 0):
                if (((check_number % i) == 0) and i != 1):
                    controller += i + (check_number / i)

        if((controller + 1) == check_number):
            print("The number ", check_number, " is perfect")