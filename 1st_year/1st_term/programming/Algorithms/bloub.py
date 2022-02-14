import random
ls = []

for i in range(10000):
    ls.append(random.randrange(0, 10000))

for _ in range(len(ls)):
    for i in range(len(ls)):
        if i != len(ls) -1 and ls[i] > ls[i + 1]:
            aux = ls[i]
            ls[i] = ls[i + 1]
            ls[i + 1] = aux
        
print(ls)

#It returns the array with a lot of time