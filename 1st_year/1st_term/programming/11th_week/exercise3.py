import random
from pprint import pprint

class Dice:
    def __init__(self, name: str, n: int):
        #Name field
        self.name = name

        #Rolls field
        self.rolls = []
        for _ in range(n):
            self.rolls.append(random.randrange(1, 7))

    def calculate_normal_score(self):
        #Initialize the return value and axiliar list
        result = 0
        aux_list = []
        for i in self.rolls:
            aux_list.append(i)
        
        lenght = len(aux_list)
        aux_result = 1
        aux_counter = lenght - 1
        aux_value = aux_list[0]

        #----------Check how many times a number repeats itself------------
        #More complex than it should be???? my objective was to reduce the amount of redundant operations and try to reduce the amount of calculations+
        #This algorithm is thought to calculate the greater number of times a number repeats in a list
        #My approach is to pick the first number and then loop the list from the end to the first integer
        #In order to search matches
        #The greater the algorithm the more optimized the time is compared with other solutions
        while (lenght != 1):
            
            #Reached the first term
            if(aux_counter <= 0 and lenght != 1):

                #Greater match
                if(aux_result > result):
                    result = aux_result

                #Reset auxiliar values
                aux_result = 1
                del aux_list[0]
                lenght -= 1
                aux_counter = lenght - 1
                aux_value = aux_list[0]
            else:
                #Got a match
                if(aux_value == aux_list[aux_counter] and lenght != 1):
                    aux_result += 1
                    del aux_list[aux_counter]
                    lenght -= 1
                
                #Go one back
                aux_counter -= 1

        return result
 
    def calculate_total_score(self):
        result = 0

        #Calculate the sum of the numbers in self.rolls
        for i in self.rolls:
            result += i

        return result

#Actual program--------------
#I aimed to create the program in order to facilitate the creation of the same game but with more player
players = [Dice(input("Input username of player 1"), 10)]
players.append(Dice(input("Input username of player 2"), 10))

#I assigned the result to the first player because i need something to compare with
result = players[0]

#This loop could be a simple if, but i used it to facilitate the making of the same game but with more players
for i in players:
    if i.calculate_normal_score() > result.calculate_normal_score():
        result = i
    elif(i.calculate_normal_score() == result.calculate_normal_score()):
        if(i.calculate_total_score() > result.calculate_total_score()):
            result = i

    #I print all the results in order to facilitate the evaluation of the program
    pprint((vars(i), i.calculate_normal_score(), i.calculate_total_score()))

#Final answer
print("The winner is",result.name)