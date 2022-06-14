#Divide and conquer which search the longest str

def longestr_(data:list):
    if len(data) > 1:
        mid = len(data) // 2
        left = longestr_(data[:mid])
        right = longestr_(data[mid:])

        if len(left) > len(right):
            return left
        else:
            return right

    if len(data) == 1:
        return data[0]
    
data = ['john', 'adam', 'alexander', 'robert', 'gerard']
print(longestr_(data))