import random

stannis = []
lannister = []

for _ in range(10000):
    stannis.append(random.randrange(10, 51))

for _ in range(3200):
    lannister.append(random.randrange(35, 76))

while not (lannister == [] or stannis == []):
    if(len(lannister) < len(stannis)):
        while (len(lannister) < len(stannis)):
            print(i)
            if(lannister[i] > stannis[i]):
                lannister[i] -= stannis[i]/3
                del(stannis[i])
        
            if(lannister[i] < stannis[i]):
                stannis[i] -= lannister[i]/3
                del(lannister[i])

        print("Lannister: ", len(lannister))
        print("Stannis: ", len(stannis))
    
    if(len(lannister) > len(stannis)):
        while(len(lannister) > len(stannis)):
            if(lannister[i] > stannis[i]):
                lannister[i] -= stannis[i]/3
                del(stannis[i])
        
            if(lannister[i] < stannis[i]):
                stannis[i] -= lannister[i]/3
                del(lannister[i])

        print("Lannister: ", len(lannister))
        print("Stannis: ", len(stannis))