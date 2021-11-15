import random

#The third number will be the parameter to state the type of the returne value
#If uniform is not valid then we can create a float with two variables 
#One an integer, and the second one also but it would be divided by some value
#Then we add both and we will get our float number
def generator_num(num1, num2, num3):
    if(num3 != 3):
        my_num = random.uniform(num1, num2)

        if(num3 == 1):
            return int(my_num)

        if(num3 == 2):
            return my_num

    else:
        my_num = random.uniform(num1, num2)
        my_num2 = random.uniform(num1, num2)
        
        return complex(my_num, my_num2)

start_interval = float(input("Input start of interval: "))
end_interval = float(input("Input end of interval: "))
choice_ = int(input("Result expressed in Integer(1), Float(2), Complex number (3): "))

while(choice_ not in [1, 2, 3]):
    choice_ = int(input("Invalid value entered, Result expressed in Integer(1), Float(2), Complex number (3): "))

print("Your number is: ",str(generator_num(start_interval, end_interval, choice_)))