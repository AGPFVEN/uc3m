#Return the smallest even number of a list using divide and conquer
def smallest_even_number(data:list):
    if len(data) == 0:
        return None
    elif len(data) == 1:
        if data[0] % 2 == 0:
            return data[0]
        else:
            return None
    else:
        mid = len(data) // 2
        left = smallest_even_number(data[:mid])
        right = smallest_even_number(data[mid:])

        if left == None:
            return right
        
        if right == None:
            return left
        
        if left < right:
            return left
        else:
            return right

print(smallest_even_number([1, 3, 4, 5, 7, 9, 2, -2, 5, 3, 10, 8]))