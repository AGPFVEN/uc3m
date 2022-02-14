from _typeshed import Self


class  Drone:
    def __init__(self, name:str):
        self.id = name
        self.current_power = 100
        self.available = True
        self.orders = ""

    @property
    def current_power(self):
        return self.__current_power
    
    @current_power.setter
    def current_power(self, current_power):
        if type(current_power) != int:
            raise TypeError("curret_power must be an integer")

        else:
            if(current_power < 0 or current_power > 100):
                raise ValueError("current_power must be betweeen 0 and 100")

class Warehouse:
    def __init__(self, name:str, drones:list = [], neighborhood:list = [], orders:str =""):
        self.name = name
        self.drones = drones
        self.neighborhood = neighborhood
        self.order = orders

    def createDrones(self, Num):
        #Loop to create a number of drones
        for i in range(Num):
            #Create the name of the drone
            drone_name = "drone" + str(i)

            #Create the drone
            new_drone = Drone(drone_name)

            #Add the new drone to the list of drones of the warehouse
            self.drones.append(new_drone)

class AreaMap:
    def __init__(self, name, list):
        self.name = name
        self.map = list