import random

maria = {
    "name": "Maria",
    "weeklyExercises": [],
    "weeklyTests": []
}

peter= {
    "name": "Peter",
    "weeklyExercises": [],
    "weeklyTests": []
}

mike= {
    "name": "Mike",
    "weeklyExercises": [],
    "weeklyTests": []
}

for i in range(10):
    maria["weeklyExercises"].append(random.randrange(0, 10))
    maria["weeklyTests"].append(random.randrange(0, 10))

    peter["weeklyExercises"].append(random.randrange(0, 10))
    peter["weeklyTests"].append(random.randrange(0, 10))

    mike["weeklyExercises"].append(random.randrange(0, 10))
    mike["weeklyTests"].append(random.randrange(0, 10))

print(maria)
print(peter)
print(mike)
