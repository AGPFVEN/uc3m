import random

def creator_numbers():
    #Create an empty list to manipulate it
    list_even_values = []

    for _ in range(10):
        
        #I will use a variable to define the last number of the interval becasue is not specified
        last_num = 20
        aux = random.randrange(0, (last_num + 1))

        #Loop untill the condition is satisfied
        while ((aux % 2) !=  1):
            aux = random.randrange(0, last_num + 1)

        #Add valid value
        list_even_values.append(aux)

    return list_even_values
    
def requirements(list_nums):
    maximum = 0
    minimum = list_nums[0]

    #My appproach is to sum all the elements and then divede between the len of the list
    average = 0

    for i in list_nums:

        #Check maximum
        if(i > maximum):
            maximum = i

        #Check minimum
        if(i < minimum):
            minimum = i

        #sum
        average += i

    average /= len(list_nums)

    return average, maximum, minimum

requirements_var = requirements(creator_numbers())
print("Average: " + str(requirements_var[0]), "Maximum: " + str(requirements_var[1]), "Minimum: " + str(requirements_var[2]), sep="\n")