import random

#Declaring the list
judges = []
maxi = 0
mini = 8

for i in range(5):

    #Assigning values to the judges
    judges.append(random.randrange(1, 9))
    print("Judge ", (i + 1), " gave the gymnast ", judges[i], " points")
    
    #Assing maximum and minimum
    if (maxi < judges[i]):
        maxi = judges[i]
    
    if(mini > judges[i]):
        mini = judges[i]

print("The lowest possible score is %i, and the highest possible score is %i" % (mini, maxi))