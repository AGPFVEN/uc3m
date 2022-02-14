import random

class Snowflake:
    def __init__(self, x:int, y:int, temperature:float):
        self.x = x
        self.y = y
        self.temperature = temperature
        self.__melted = False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x:float):
        if x < 0:
            raise ValueError("The x coordinate cannot be negative")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y:float):
        if y < 0:
            raise ValueError("The y coordinate cannot be negative")

    @property
    def melted(self):
        if self.temperature > 2:
            return True
        else:
            return False

class Street:
    def __init__(self, direction:str, starting_x:int, starting_y:int, length:int, temperature:int, snoflakes:list = []):
        self.direction = direction
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.length = length
        self.temperature = temperature
        self.snowflakes = snoflakes

        if()

    def __str__(self):
        #Start with empty string
        result = "Street "

        #Check for vertical or horizontal
        if self.direction == "horizontal":
            result += "H-" + str(self.starting_x)
            final_x = self.starting_x + self.length
            final_y = self.starting_y
        elif self.direction == "vertical":
            result += "V-" + str(self.starting_y)
            final_x = self.starting_x
            final_y = self.starting_y + self.length

        #Continue coordinates of string
        result += ", goes from (" + str(self.starting_x) + "," + str(self.starting_y) + ") to (" + str(final_x) + "," + str(final_y) + ")"
        result += ". Temperature: " + str(self.temperature)

        return result

class Snowplow:
    def __init__(self, x, y, fuel):
        self.x = x
        self.y = y
        self.fuel = fuel

class City:
    def __init__(self, height, width, streets:tuple = (), snowplow:tuple = ()):
        self.height = height
        self.width = width
        self.streets = streets
        self.snowplow = snowplow

    def create_streets(self):
        result = []

        #Doing rectangular matrix
        for i in range(20):
            #Appending the horizontal street
            result.append(Street("horiontal", 0, 1, random.randrange(5, self.width + 1), random.randrange(-5, 5)))

            #Appending the vertical street
            result.append(Street("vertical", i, 0, random.randrange(5, self.height + 1), random.randrange(-5, 5)))
        
        return tuple(result)

    def create_snowplows(self):
        result = []

        #Loop through streets to create a snowplow in each one of them
        for i in self.streets:
            result.append(Snowplow(i.x, i.y, random.randrange(1, 21)))

    def snow(self, number:int):
        for i in range(number):
            #Select random street
            selected_street = self.streets[random.randrange(0, len(self.streets))]

            #Create the snowflake
            Snowflake()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height:int):
        if height > 5:
            self.__height = height
        else:
            raise ValueError("Height must be bigger than 5")
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width:int):
        if width > 5:
            self.__width = width
        else:
            raise ValueError("Width must be bigger than 5")