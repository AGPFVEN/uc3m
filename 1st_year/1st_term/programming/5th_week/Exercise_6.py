#Ask for the first student, it will all the parameters because is the first one
student = float(input("Put the mark of your student:"))
highest = student
lowest = student
average = student
n = 0
total_student = 0

#This will be a loop because I don't know how many students they are
while (student > 0):
    if (lowest > student):
        lowest = student
    print("The lowest student has a: ", lowest)

    if (highest < student):
        highest = student
    print("The highest student has a: ", highest)

    n += 1
    total_student += student
    average = total_student / n
    print("Your total student scores are: ", total_student, ", your number of students is: ", n, ", and the average is: ", average)

    student = float(input("What's your next student: "))