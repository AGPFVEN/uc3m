def my_exercise(year, month):

    #Asked dictionaries
    months = {
        "January": 31,
        "February": 28,
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
    inp_year = year

    #Input
    inp_month = month
    
    if(inp_year % 400 == 0 or (inp_year % 100 != 0 and inp_year % 4 == 0 )):
        months["February"] = 29

    my_months = list(months.keys())
    print(months[my_months[inp_month -1]])

my_year = int(input("Input a year: "))
my_month = int(input("Input a month:"))

my_exercise(my_year, my_month)