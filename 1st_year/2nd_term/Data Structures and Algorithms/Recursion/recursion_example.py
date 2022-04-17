def rec(a):
    if a > 3:
        return a

    print("hello " + str(a))
    rec(a + 1)
    print("bye" + str(a))

print(rec(1))