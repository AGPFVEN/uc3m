#Rock, Paper, scissors
import random

#Declaring number of games
n = 0 

while (n < 4):
    n += 1

    #User
    inp = ""
    while (inp != "rock" and inp != "paper" and inp != "scissors"):
        inp = input("ROCK, PAPER or SCISSORS? ").lower()

    #Program
    program = random.choice(["ROCK", "PAPER", "SCISSORS"]).lower()
    print("Program chooses ", program)

    #Possible cases
    if(inp == program):
        print("*****TIE*****")

    if(( inp == "rock" and program == "scissors") or (inp == "paper" and program == "rock") or (inp == "scissors" and program == "paper")):
        print("*****PLAYER WINS*****")

    if(( program == "rock" and inp== "scissors") or (program == "paper" and inp == "rock") or (program == "scissors" and inp == "paper")):
        print("*****PROGRAM WINS*****")