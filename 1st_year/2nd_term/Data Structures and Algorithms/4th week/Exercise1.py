import random
import time
import matplotlib.pyplot as plt

def randomList(n = 25, a = 0, b = 0):
    result = []

    for i in range(n):
        result.append(random.randrange(a, b))

    return result

def sumList(l):
    start = time.time()

    result = 0

    for i in l:
        result += i

    end = time.time()

    return result, end - start

def contains(l, x):
    for i in l:
        if (i == x):
            return True

    return False

values = [[], []]
for i in range(8):
    num = 10 ** i
    print("The list was of length: " + str(num))
    result = sumList(randomList(num, 0, 100))
    print("The time spent has been of: " + str(result[1]))
    values[0].append(num)
    values[1].append(result[1])

print(values)
fig, ax = plt.subplots()
ax.plot(values[0], values[1])
ax.set_xscale = "log"
ax.set_yscale = "log"
plt.show()