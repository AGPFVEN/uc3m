#This program aims to calculate if a year is a leap year o not
#first we need to ask for the year
year = int(input("Enter the year you wanna calculate: "))

#Check if the year is divisible by 100
if (year % 100 == 0):

    #Check if year is divisible 400 if divisible by 100
    if (year % 400 == 0):
        if(year < 2021):
            print(year, " was a leap year")

        else:
            print(year, " will be a leap year")

else:
    if ( year % 4 == 0):
        if(year < 2021):
           print(year, " was a leap year")

        else:
            print(year, " will be a leap year")

    else:
        if(year < 2021):
           print(year, " was a not a not leap year")

        else:
            print(year, " will be a not leap year")       