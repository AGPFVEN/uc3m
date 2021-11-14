def convert_to_int(target):
    if(target == "USD"):
        target = 0
    if(target == "EUR"):
        target = 1
    if(target == "GBP"):
        target = 2
    if(target == "JPY"):
        target = 3
    
    return(target)



def currecy_converter(amount, origin, end):
    #USD, EUR, GBP, JPY
    exchange_rate = (1, .86, .74, 112.87)

    #Convert target into number
    origin = convert_to_int(origin)
    end = convert_to_int(end)

    return amount / exchange_rate[origin] * exchange_rate[end]

money = float(input("Input the amount of money you want to convert: "))
original = input("input origin (USD, EUR, GBP, JPY): ")
final_ = input("Input your target (same as before): ")

print(currecy_converter(money, original, final_))