def sumdigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumdigits(int(n / 10))

print(sumdigits(2356))