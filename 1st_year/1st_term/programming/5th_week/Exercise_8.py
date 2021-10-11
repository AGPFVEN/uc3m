#21
import random

#Initializing all the variables
number_games = int(input("Input the number of games you want to play: "))
player_one = 0
player_two = 0
total_value = 0
value_one = 0
value_two = 0

#Run the game for a number of times
for i in range(number_games):

    #Restart values
    cont = True
    total_value = 0

    #Player 1
    while(cont):

        #These are the random values
        value_one = random.randrange(1, 10)
        value_two = random.randrange(1, 10)

        total_value += value_one + value_two

        #Output
        print("GAME ", i, " - PLAYER 1")
        print("The number of points obtained are ", value_one, ", ", value_two)
        print("The points accumulated are ", total_value)
        cont = input("Would you like to roll the dice again? (yes/no)\n")

        if(cont == "no"):
            player_one = total_value
            cont == False

    cont = True
    total_value = 0 

    #Player 2
    while(cont):

        #These are the random valuesº
        value_one = random.randrange(1, 11)
        value_two = random.randrange(1, 11)

        total_value += value_one + value_two

        print("GAME ", i, " - PLAYER 2")
        print("The number of points obtained are ", value_one, ", ", value_two)
        print("The points accumulated are ", total_value)
        cont = input("Would you like to roll the dice again? (yes/no)\n")

        if(cont == "no"):
            player_two = total_value
            cont == False

    #Results of the game
    if (abs(player_one - 21) < abs(player_two - 21)):
        print("**************PLAYER 1 WINS******************")
    if (abs(player_two - 21) < abs(player_one- 21)):
        print("**************PLAYER 2 WINS******************")
    if (abs(player_one - 21) == abs(player_two - 21)):
        print("**************TIE******************")