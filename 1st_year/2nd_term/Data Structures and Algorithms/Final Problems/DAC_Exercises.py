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

def getIndexes(data,x):
    if data==None or len(data)==0:
        return []
    return _getIndexes(data,x,0,len(data)-1)

def _getIndexes(data,x,left,right):
    print(left, right)

    if left>right:
        return []
    
    if left==right:
      
       if data [left] == x:
           return [left]
       else:
           return []
       
    mid = (left + right) // 2

    index1= _getIndexes(data,x,left,mid)
      
    index2= _getIndexes(data,x,mid+1,right)
   
    return index1 + index2


def kk(ls:list):
    return kk_(ls, 0, len(ls) - 1)
def kk_(ls:list, first, second):
    res = []
    mid = (second + first) // 2 
    print(first, mid, second, res)

    if first == second:
        return [first]
 
    if first < second:
        #left
        for i in (kk_(ls, first, mid)):
            res.append(i)

        #right
        for j in (kk_(ls, mid + 1, second)):
            res.append(j)

    return res


def multiples_sum(ls:list, x:int):
    if len(ls) < 1:
        return 0

    elif len(ls) == 1:
        if ls[0] % x == 0:
            return ls[0]

        return 0

    else:
        mid = ((len(ls)) // 2)

        left = multiples_sum(ls[:mid], x)
        right = multiples_sum(ls[mid:], x)

        return left + right
            

l = [1,2,3,4,2,3,4,7,8,9,2,2,4,2]
#print(l[(len(l) - 1)// 2])
res = multiples_sum(l, 2)
#print(len(res))
print(res)
#print(len(l))