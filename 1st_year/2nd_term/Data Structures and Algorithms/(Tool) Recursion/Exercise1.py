def detect_min(l):
    if len(l) > 1:
        if (l[0] < l[1]):
            del l[1]
        else:
            del l[0]
        
        result = detect_min(l)

        return result
    
    else:
        return l

l = [1, 2, 4, 7, 6, 5, 20, 0]
print(str(detect_min(l)))