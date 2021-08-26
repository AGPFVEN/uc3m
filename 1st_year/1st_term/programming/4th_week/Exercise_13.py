#This is a simulated calculator
#Inputs
first_number = int(input("Input a number: "))
operator = input("an operator (+, -, *, /, //, **): ")
second_number = int(input("Input another numbe: "))

#Conditionals depending of the operator
if (operator == "+"):
    print(first_number + second_number)
elif (operator == "-"):
    print(first_number - second_number)
elif (operator == "*"):
    print(first_number * second_number)
elif (operator == "/"):
    print(first_number / second_number)
elif (operator == "//"):
    print(first_number // second_number)
elif (operator == "**"):
    print(first_number ** second_number)