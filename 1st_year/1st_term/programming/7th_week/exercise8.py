#Aux variable
aux = False

#Asked dictionaries
months = {
    "January": 31,
    "February": [28, 29],
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

User = {
    "month": "",
    "day": 0,
    "year": 0,
    "leap": False
}
inp_year = input("Input a year: ")

#Input
inp_month = input("Input a month: ")

while (aux == False):
    for i in months.keys():
        if inp_month == i:
            aux = True

    if aux == False:
        inp_month = input("Input a valid month: ")

inp_day = input("Input a day: ")

while (inp_day > months[inp_month]):
        inp_day = input("Input a valid day: ")