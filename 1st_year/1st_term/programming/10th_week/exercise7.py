def fibonacci_sequence(x):
    #Empty list to manipulate
    result = [0, 1]

    while (len(result) -1 != x):
        result.append(result[-1] + result[-2])

    return result

print(fibonacci_sequence(7))