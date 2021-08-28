#Input a positive number
p_num = float(input("Input a positive number "))
two_hundred = 0
one_hundred = 0
fifty = 0
twenty = 0
ten = 0
five = 0
two = 0
one = 0
point_five = 0
point_two = 0
point_one = 0
point_zero_five = 0
point_zero_two = 0
point_zero_one = 0

if (p_num % 200 == 0):
    two_hundred = int(p_num / 200)
    p_num -= two_hundred * 200
    print("200€: ", two_hundred)

if (p_num % 100 == 0):
    one_hundred= int(p_num / 100)
    p_num -= one_hundred * 100
    print("100€: ", one_hundred)

if (p_num % 50 == 0):
    fifty = int(p_num / 50)
    p_num -= fifty * 50
    print("50€: ", fifty)

if (p_num % 20 == 0):
    twenty = int(p_num / 20)
    p_num -= twenty * 20
    print("20€: ", twenty)

if (p_num % 10 == 0):
    ten = int(p_num / 10)
    p_num -= ten * 10
    print("10€: ", ten)

if (p_num % 5 == 0):
    five = int(p_num / 5)
    p_num -= five * 5
    print("5€: ", five)

if (p_num % 2 == 0):
    two = int(p_num / 2)
    p_num -= two * 2
    print("2€: ", two)

if (p_num % 1 == 0):
    one = int(p_num / 200)
    p_num -= one * 1
    print("1€: ", one)

if (p_num % .5 == 0):
    point_five = int(p_num / 200)
    p_num -= point_five * 200
    print(".5€: ", point_five)

if (p_num % .2 == 0):
    point_two= int(p_num / .2)
    p_num -= point_two* .2
    print(".2€: ", point_two)

if (p_num % .1 == 0):
    point_one = int(p_num / .1)
    p_num -= point_one * .1
    print(".1€: ", point_one)

if (p_num % .05 == 0):
    point_zero_five = int(p_num / .05)
    p_num -= point_zero_five * .05
    print("0.05€: ", point_zero_five)

if (p_num % .02 == 0):
    point_zero_two = int(p_num / .02)
    p_num -= point_zero_two * .02
    print(".02€: ", point_zero_two)

if (p_num % .01 == 0):
    point_zero_one = int(p_num / .01)
    p_num -= point_zero_one * .01
    print(".02€: ", point_zero_one)

#888,88