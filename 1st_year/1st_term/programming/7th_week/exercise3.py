import random

#Declaring an empty list
ls = []

#Loop to random numbers not repeated
for i in range(3):
    ls.append([])

    for j in range(3): 
        ls[i].append(random.randrange(1, 101))

        #This approach to not repeat a number, has one mistake:
        #If a number is repeated and then replaced the new value could be another repeated value
        for l in range(i):
            for p in range(j):
                while(ls[i][j] == ls[l][p]):
                    ls[i][j] = (random.randrange(1, 101))

aux = 0
print(ls)
final_ls = []
pos = [0, 0]

for p in range(3):
    final_ls.append([])

    for k in range(3):

        for i in range(3):

            for j in range(3):

                if(ls[i][j] > aux):
                    aux = ls[i][j]
                    pos[0] = i
                    pos[1] = j

        final_ls[p].append(aux)
        ls[pos[0]][pos[1]] = 0
        pos = [0, 0]
        aux = 0

print(final_ls)