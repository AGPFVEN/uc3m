coins = (200, 100, 50, 20, 10, 5, 2, 1, .5, .25)
inp = float(input("Enter a quantity of money: "))
n = 0

for divider in coins:
    while(inp > divider and inp > 0.001):
        n += 1
        inp -= divider

    print(divider, ": ", n)
    n = 0