#This program calculates the price of a ticket depending of the age of the customer
#Input the age of user
age = int(input("Enter your age"))

#Price of ticket
n_price = 9

#Calculate ticket
if (age < 5):
    n_price *= .6

if (age > 60):
    n_price *= .55

if (age < 26):
    n_price *= .2

print("This is the price od your ticket ", n_price)