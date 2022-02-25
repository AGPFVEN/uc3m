def checksorted(l):
    if len(l) <= 1:
        return True
      
    if (l[0] <= l[1]):
        return checksorted(l[1:])
    else:
        return False

l = [1, 2, 3, 4, 7, 6, 7, 8, 9]
print(checksorted(l))