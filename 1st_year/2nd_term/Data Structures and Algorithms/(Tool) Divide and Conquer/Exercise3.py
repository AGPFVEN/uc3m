def count(s:str, c:str):
    #Base cases
    if s == "":
        return 0
    
    else:
        result = 0
        i = 0
        j = len(s) -1

        while i < j:
            if s[i] == c:
                result += 1
            if s[j] == c:
                result += 1
            
            i += 1
            j -= 1
        
    return result

s = 'abcdecfccg'
c = 'c'
print(count(s,c))