def mergeSort(data):
    #Base Case
    if len(data) == 0:
        return False

    #Real Divide and Conquer
    if len(data) > 1:
        mid = len(data) // 2
        part1 = mergeSort(data[0:mid])
        part2 = mergeSort(data[mid:]) 
        return merge(part1, part2)
    else:
        return data


def merge(a, b):
    newList = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            newList.append(a[i])
            i += 1
        else:
            newList.append(b[j])
            j+= 1
        
    while i < len(a):
        newList.append(a[i])
        i += 1

    while j < len(b):
        newList.append(b[j])
        j += 1
        
    print(newList)
    
    return newList

print(mergeSort([5, 4, 2, 56, 9, 12, 6, 234, 6, 8, 90, 4, 0, -4, -80, 2, 7, 99, 99, -100]))