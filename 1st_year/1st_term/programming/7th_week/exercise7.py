import random

#Initialize all directories (students)
maria = {
    "name": "Maria"
}

peter= {
    "name": "Peter"
}

mike= {
    "name": "Mike"
}

#Number of marks
number_of_marks = 10

#List containing all students to iterate them
students = [maria, peter, mike]

#Loop
for i in range(len(students)):

    #Asked variables
    students[i]["weeklyExercises"] = []
    students[i]["weeklyTests"] = []
    total_exercises = 0
    total_tests = 0
    aux_exercises = 0
    aux_tests = 0

    #Loop to fill the first two lists, find its maximum, minimum and
    #the total of exercises and tests
    for j in range(number_of_marks):
        students[i]["weeklyExercises"].append(random.randrange(0, 11))
        total_exercises += students[i]["weeklyExercises"][j]
        students[i]["weeklyTests"].append(random.randrange(0, 11))
        total_tests += students[i]["weeklyTests"][j]

        if(students[i]["weeklyExercises"][j] > aux_exercises):
            aux_exercises = students[i]["weeklyExercises"][j]

        if(students[i]["weeklyTests"][j] > aux_tests):
            aux_tests= students[i]["weeklyTests"][j]

    #Exam
    students[i]["exam"] = random.randrange(0, 11)

    #Filling list with averages, minimum and maximum of each students
    students[i]["rates"] = []
    students[i]["rates"].append(total_exercises/number_of_marks)
    students[i]["rates"].append(total_tests/number_of_marks)
    students[i]["rates"].append(aux_exercises)
    students[i]["rates"].append(aux_tests)

    #Calculating mark of each student
    students[i]["mark"] = students[i]["rates"][0] * .01
    students[i]["mark"] += students[i]["rates"][1] * .3
    students[i]["mark"] += students[i]["exam"] * .6

    #Calculating letter grade
    if (students[i]["mark"] >= 9):
        students[i]["letterGrade"] = "A"
    elif (students[i]["mark"] >= 8):
        students[i]["letterGrade"] = "B"
    elif (students[i]["mark"] >= 7):
        students[i]["letterGrade"] = "C"
    elif (students[i]["mark"] >= 6):
        students[i]["letterGrade"] = "D"
    elif (students[i]["mark"] >= 5):
        students[i]["letterGrade"] = "E"
    else:
        students[i]["letterGrade"] = "F"

    #Printing each value of each student
    for j in students[i].values():
        print(j)

#Average mark of the class
average_mark = 0
for i in range(len(students)):
    average_mark += students[i]["mark"]

average_mark /= len(students)
print(average_mark)