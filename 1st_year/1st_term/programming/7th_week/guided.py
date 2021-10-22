import random
lan = []

sol = 10000
sol_aux = sol
i = 1
rows = 0

while (sol_aux != 0):
   sol_aux -= (i * 1000)
   rows += 1
   i += 1

print(rows)

for i in range(4):
    lan.append([])

    for j in range(1000 * (i + 1)):
        lan[i].append(random.randrange(10, 100))

    print(len(lan[i]))

