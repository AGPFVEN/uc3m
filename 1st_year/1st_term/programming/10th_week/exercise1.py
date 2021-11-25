def function_combinator(ls1, ls2):
    #Declaring empty list to manipulate
    ls_final = []

    #Eliminate duplicated
    for i in ls2:
        if i in ls1:
            del ls2[ls2.index(i)]

    #Fill the list
    for i in ls1:
        ls_final.append(i)

    #If the second list is not empty use its values
    if(len(ls2) > 0):
        for i in ls2:
            ls_final.append(i)

    return(ls_final)

#Example of functionality
ls1 = [1, 2, 3, 4, 5, 6]
ls2 = [4, 5, 6, 7, 8, 9]

result = function_combinator(ls1, ls2)
print(result)