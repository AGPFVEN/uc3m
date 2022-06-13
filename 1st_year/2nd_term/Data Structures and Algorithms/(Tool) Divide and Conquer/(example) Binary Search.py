def binarySearch(data, x):
    #Base case
    if len(data) == 0:
        return False
    
    #Real Divide and conquer 
    mid = len(data) // 2

    if x == data[mid]:
        return True
    
    if x < data[mid]:
        return binarySearch(data[0:mid], x)

    if x > data[mid]:
        return binarySearch(data[mid:], x)

print(binarySearch([1, 2, 3, 4, 6, 7, 20, 21, 25, 26, 30, 40, 100, 101, 102], 40))
