import random

#Initializing list
list_1 = []

#Assingning random values
for i in range(20):
    list_1.append(random.randrange(0, 100))

#Assign one list to anotherone
list_2 = list_1

#Print both lists
print(list_1)
print(list_2)

#Equal to another value
list_1[0] = 101

#Printing both lists
print(list_1)
print(list_2)

#Yes, the corresponding element of the second list changed too
#Because of the memory management

list_3 = []
for i in range(20):
    list_3.append(random.randrange(0, 100))

list_4 = []
for i in list_3:
    list_4.append(i)

print(list_3)
print(list_4)

list_3[0] = 101

print(list_3)
print(list_4)

#The difference is that the value of the second does not change