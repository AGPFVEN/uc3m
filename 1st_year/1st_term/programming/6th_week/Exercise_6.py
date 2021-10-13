inp = ""
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "Dicember")

#Loop to print month by a given number
while(inp != 0):
    inp = int(input("Input a number of a month: "))

    if(inp != 0):
        print(months[inp -1], " is ", inp)