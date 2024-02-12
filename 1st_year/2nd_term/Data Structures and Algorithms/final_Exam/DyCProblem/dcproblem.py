#Alfonso Pineda

import re


def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0:
        return None

    if len(a) == 1:
        if a[0] == x:
            return 1
    
    elif len(a) > 2:
        left = find_index(a[:(len(a)//2)], x, 0)
        right = find_index(a[(len(b)//2):], x, len(a)//2)
        print(left, right)

def find_index(a:list, x:int, ind:int):
    if len(a) > 2:
        left = find_index(a[:(len(a)//2)], x, ind)
        right = find_index(a[(len(b)//2):], x, ind + len(a)//2)
        #print(left,right)
    
    elif a != []:
        print(ind)
        if a[0] == x:
            return ind

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b[:(len(b)//2)], len(b[:(len(b)//2)]))
    print(b[(len(b)//2):], len(b[(len(b)//2):]))
    print(len(b))

    #print(find_first_last(b, -2))
    #for value in sorted(set(b)):
        #first, last = find_first_last(b, value)
        #print("x: ", value, ", first index:", first, ", last index: ", last)

    #value = 4   # does not exist
    #first, last = find_first_last(b, value)
    #print("x: ", value, ", first index:", first, ", last index: ", last)
