#def quickSort(data:list):
    #print("hello")
    #print(data)
    ##Base Case
    #if len(data) < 1:
        #return 0
    
    #elif len(data) == 1:
        #return [data[0]]
    
    #else:
        #result = []

        #if len(data) == 2:
            #if data[0] < data[1]:
                #result.append(data[0])
                #result.append(data[1])
            #else:
                #result.append(data[1])
                #result.append(data[0])
    
        ##Real Divide and Conquer
        #if len(data) > 2:
            ##Aux Variables to iterate the array
            #i = 0
            #j = len(data) - 1

            ##Mid Variable
            #mid = len(data) // 2

            ##Pivot variable
            #pivot = data[mid]

            ##Loop the array and compare
            #while i < j:
                #if pivot < data[i]:
                    #value_storage = data.pop(i)
                    #data.append(value_storage)
                #else:
                    #i += 1
            
                #if pivot > data[j]:
                    #value_storage = data.pop(j)
                    #data.insert(0, value_storage)
                #else:
                    #j -= 1
                
            #print(pivot)

            #print(data[:mid])
            #print(data[mid:])
            
            #left = quickSort(data[:mid])
            #right = quickSort(data[mid:])
            
            #for k in left:
                #result.append(k)

            #for k in right:
                #result.append(k)

        #return result 

def quicksort(data):
    return _quicksort(data,0,len(data)-1)
def  _quicksort(data, left, right):
    i = left
    j = right
    m=(left + right) // 2
    p = data[m] # pivot element in the middle
    if i <= j: # if left index < right index
        while data[i] < p:
            i += 1
        while data[j] > p:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i] # swap
        i += 1
        j -= 1
    if left < j: # sort left list
        _quicksort(data, left, j)
    if i < right: # sort right list
        _quicksort(data, i, right)
    return data

ar = [4, 10, 2, 20, 1, 3, 5, -1, 9, 8, 0]
rew = quicksort(ar)
print(rew)