import random

print("Stock:   size0  size1  size2  size3  size4  size5  size6  size7  size8  size9")

#Declaring my variables
wood = []
wood_num = 10
size_string = "           "

#Loop to create the wood
for i in range(wood_num):
    wood.append(random.randrange(1, 11))
    size_string += (str(wood[i]) + "      ")

print(size_string)

#Input of customers
customer_num = int(input("input a number of clients: "))

#Assure that the number is positive
while(customer_num < 1):
    customer_num = int(input("Invalid number of clients, try again:"))

#Create customers
customer = []
print("Original orders:")

#Fill customers
for j in range(customer_num):
    customer.append([])
    customer_str = str("Customer " + str(j) + ": ")

    for i in range(wood_num): 
        customer[j].append(random.randrange(0, 5))
        customer_str += str(customer[j][i]) + "      "

    print(customer_str)

#Operations
print("Pending orders")
for i in range(customer_num):
    for j in range(wood_num):
        if(wood[j] >= customer[i][j]):
            wood[j] -= customer[i][j]
            customer[i][j] = 0
        else:
            customer[i][j] -= wood[j]
            wood[j] = 0

    #Decide whether to print or not
    if wood.count(0) != wood_num:
        customer_str = str("Customer " + str(i) + ": ")

        for j in range(wood_num):
            customer_str += str(customer[i][j]) + "      "

        print(customer_str)