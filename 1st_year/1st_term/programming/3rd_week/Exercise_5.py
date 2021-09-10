#This exercise is about demonstrating the precission of python

#Declaring two floats
first_float = 12345678901234567.0
second_float = 12345678901234568.0

#Print the substraction between two floats
print(str(str(first_float) + " - " + str(second_float)) + " = " + str(first_float - second_float))

#Declaring two ints
first_int = 12345678901234567
second_int = 12345678901234568

#Print the substraction between two ints
print(str(str(first_int) + " - " + str(second_int)) + " = " + str(first_int - second_int))

#This happens because in pyhton integers doesn't have a limit, meanwhile floats have

print(0.3 - .2)
#The result is .09999999999 because of a precision issue of python