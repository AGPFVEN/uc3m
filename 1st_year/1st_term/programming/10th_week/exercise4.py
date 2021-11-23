def range_tuple(start, end, step = 1):
    #Empty list to manipulate
    result = []

    if (type(start) == int and type(end) == int and type(step) == int):
        #The aux variable will act as the distance between values
        aux = abs((start - end))

        #Loop to fill the list
        while (start != end):
            result.append(start)
            start += step

            #As the distance will always be decreasing until it reaches 0
            #If it increases some parameter must be wrong
            if(aux < abs(start - end)):
                return tuple([])
            else:
                aux -= abs(step)

        return tuple(result)

    else:
        return("Invalid parameters")

#Examples
print(range_tuple(2, 20, 2), "\n", range_tuple(1, 10, -1), "\n", range_tuple("ex", 10, 2))