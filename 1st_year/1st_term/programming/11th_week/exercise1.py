class Student:
    def __init__(self, name: str, surname: str, programming_m: float, algebra_m: float, calculus_m: float, physics_m: float, humanities_m: float):
        
        #Declaring my variables
        self.name = name
        self.surname = surname
        self.marks = [int(programming_m), int(algebra_m), int(calculus_m), int(physics_m), int(humanities_m)]

        #Check that the marks are valid
        for i in range(len(self.marks)):
            if (self.marks[i] < 0 or self.marks[i] > 10):
                self.marks[i] = 0

#Needed inputs
name_input = input("Input the name of your student: ")
surname_input = input("Input the surname of your student: ")
programming_m_input = input("Input the programming`s mark of your student: ")
algebra_m_input = input("Input the algebra`s mark of your student: ")
calculus_m_input = input("Input the calculus`s mark of your student: ")
physics_m_input = input("Input the physics`s mark of your student: ")
humanities_m_input = input("Input the humanities mark of your student: ")

my_student = Student(name_input, surname_input, programming_m_input, algebra_m_input, calculus_m_input, physics_m_input, humanities_m_input)
print(my_student.marks)