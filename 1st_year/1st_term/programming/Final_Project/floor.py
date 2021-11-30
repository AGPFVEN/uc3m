from collisionManager import Collision_manager

class Floor_handler:
    def __init__(self, size_of_x, size_of_y, collision_manager:Collision_manager):
        #Array with all the invalid zones (all the floors)
        self.floor = []

        #Size of all the floors of x * y size
        self.size_X = size_of_x
        self.size_y = size_of_y

        #Sprite of the floor
        self.sprite = (0, 16, 16, 16, 16)

        #
        self.collision_manager = collision_manager

    #This function creates blocks (by programing them)
    #It is used for the floor because it`s faster to develop with a loop
    def create_floor(self, new_x, new_y):
        information = [new_x, new_y, "stones", self.size_X, self.size_y]
        self.floor.append(information)
        self.collision_manager.add_collider_x(information)

    #This function will create a list which contains the range of the floors
    #The approach is to check the upper corners so the player can't traspass them