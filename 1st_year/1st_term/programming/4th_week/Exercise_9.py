n_one = int(input("Enter your x-coordinate"))
n_two = int(input("Enter your y-coordinate"))

if (n_one == 0 or n_two == 0):
    print("The values are not valid")

if (n_one > 0 and n_two > 0):
    print("1st")

if (n_one < 0 and n_two > 0):
    print("2nd")

if (n_one < 0 and n_two < 0):
    print("3rd")

if (n_one < 0 and n_two < 0):
    print("4th")