salary = int(input("Input base salary "))

if(salary >= 1000):
    print("Final salary of the worker is:\n", salary)

elif(salary < 1000):
    seniority = int(input("Input your seniority (years working): "))
    
    if(seniority >= 10):
        print("Final salary of the worker is:\n", salary * 1.2)

    elif(seniority < 10):
        print("Final salary of the worker is:\n", salary * 1.05)