import random
import time

#Variables of the exercise
list_1 = []
start = time.time()

for i in range(100000):
    list_1.append(random.randrange(1, 100))

end = time.time()

print("append: ", end - start)

list_1.clear

start = time.time()

for i in range(100000):
    list_1 += [(random.randrange(1, 100))]

end = time.time()

print("+=: ", end - start)

list_2 =[]

start = time.time()

for i in range(100000):
    var = [random.randrange(1, 100)]
    list_2 = list_2 + var

end = time.time()

print("+: ", end - start)

list_1.clear

#append:  0.05451345443725586
#+=:  0.05701327323913574
#+:  6.393956422805786
#As we can see append is the fastest