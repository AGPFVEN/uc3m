#Initialize my list
ls = []
my_str = ""
used_numbers = []

#Loop to do it two times
for i in range(2):
    ls.append([])

    #Ask for number of rows and columns
    rows = int(input(str("Specify the number of rows of the M%i matrix and press Enter: " % (i + 1))))
    columns = int(input(str("Specify the number of columns of the M%i matrix and press Enter: " % (i + 1))))

    #Loop for rows
    for k in range(rows):
        ls[i].append([])

        #Loop for columns
        for j in range(columns):
            
            #Ask for values
            ls[i][k].append(input(str("Introduce the term in the %i, %i position and press Enter: " % (j + 1, k + 1))))

    #Printing the matrix 
    print(str("The M%i matrix is: " % i))

    #Printing the final strings
    for k in range(rows):
        my_str = ""
        for j in range(columns):
            my_str += (str(ls[i][k][j]) + "  ")

        print(my_str)

#Checking for repeated values
#There's a problem
for k in range(len(ls[0])):
        
    for j in range(len(ls[0][k])):

        for p in range(len(ls[1])):
                
            for h in range(len(ls[1][p])):

                #I used -k, -j, -p, and -h because of the index out of bound error
                #So the list will be iterated from the last to the first and will repeat some values 
                if (ls[0][-k][-j] == ls[1][-p][-h]):
                    print("repetido", ls[0][-k][-j])

                    #This line is to prevent double repeats
                    del ls[0][-k][-j]