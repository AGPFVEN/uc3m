#Define functionn to check if a number is bigger than 0 in order to not repeat code
def check_if_lower_zero(number):
    if number < 0:
        number = 1

    return number

class RightTriangle:
    #In the init I declared the parameters as properties and applying the rules given by the exercise
    def __init__(self, base: float, height: float):
        self.base = check_if_lower_zero(float(base))
        self.height = check_if_lower_zero(float(height))

    #Function to calculate area
    def area_calculator(self):
        return (self.base * self.height) / 2

    #Function to calculate perimeter
    def perimeter_calculator(self):
        return (self.base + self.height + (self.base ** 2 + self.height ** 2) ** (1/2))

#----Actual program-----
#Inputs
inp_base = input("Input the base of your triangle: ")
inp_height = input("Input the height of your triangle: ")

#Initialize object
my_triangle = RightTriangle(inp_base, inp_height)

#Ask for area or perimeter
decision = input("Do you want the base or the perimeter of your triangle? (area/perimeter): ")

#Print what the user wants
if (decision == "area"):
    print(my_triangle.area_calculator())

if (decision == "perimeter"):
    print(my_triangle.perimeter_calculator())