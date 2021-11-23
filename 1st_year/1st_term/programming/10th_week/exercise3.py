def multiple_ls_analizer(ls1, ls2, element):
    #Empty string to manipulate
    result = []

    #Checks if an element is in the same position in two lists
    for i in range(min(len(ls1), len(ls2))):
        if(ls1 == element and ls2 == element):
            result.append(i)

    return tuple(result)

    

def ls_analizer(ls, element):

    #Empty string to manipulate
    result= []

    #Loop to search element
    for i in range(len(ls)):
        if (ls[i] == element):
            result.append(i)

    return tuple(result)
