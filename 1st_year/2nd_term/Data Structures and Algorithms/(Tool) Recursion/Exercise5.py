def russianMult(a, b):
    if a <= 1:
        return b

    if (a % 2 != 0):
        a -= 1
    return b + russianMult(a/2, b*2)

print(russianMult(7, 1000))