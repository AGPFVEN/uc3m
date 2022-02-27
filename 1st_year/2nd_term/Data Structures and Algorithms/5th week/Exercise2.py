def palindrome_check(st):
    if len(st) > 1:
        if st[0] == st[-1]:
            return palindrome_check(st[1:-1])
        else:
            return False
        
    else:
        return True

print(palindrome_check("racecar"))