def findMax(data):
    #Easy base case
    if len(data) == 1:
        return data[0]
    
    #Real Divide and Conquer
    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:]
    max1 = findMax(left)
    max2 = findMax(right)
    return max(max1, max2)

print(findMax([5, 6, 4, 8, 9, 10, 1000, 4, 4, 4, 30, 7]))