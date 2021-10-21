import random

#Declaring a new and fresh list and a variable that represents the number
#of rows that we want
ls = []
rows_num = 4

#Inner loop for the construction of rows
for k in range(rows_num):
    ls.append([])
    result = 0
    my_str = ""

    #Loop for the construction of columns
    #My approach is to create a column with our random values
    for i in range(rows_num):
        ls[k].append(random.randrange(1, 11))
        result += ls[k][i]
        my_str += (str(ls[k][i]) + " + ")


    #And then we add our sum of random values
    ls[k].append(result)

    #And do the last change to our string
    final_str = my_str[:-2] + "= " + str(result)

    print(final_str)