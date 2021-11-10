class Floor_handler:
    def __init__(self, size_of_x, size_of_y):
        #Array with all the invalid zones (all the floors)
        self.floor = []
        self.floor_not_fall = []

        #Size of all the floors of x * y size
        self.size_X = size_of_x
        self.size_y = size_of_y

        #Sprite of the floor
        self.sprite = (1, 48, 0, 15, 16)

    #This function creates blocks (by programing them)
    #It is used for the floor because it`s faster to develop with a loop
    def create_floor(self, new_x, new_y):
        self.floor.append([new_x, new_y])

    #This function will create a list which contains the range of the floors
    #The approach is to check the upper corners so the player can't traspass them
    def create_floor_not_fall(self):
        beggining = self.floor[0][0]
        final = beggining + 16
        floor_counter = 0

        self.floor_not_fall.append([beggining, final])

        for i in range(len(self.floor)):
            #print(self.floor[i])
            if (final == self.floor[i][0]):
                #print("in", self.floor[i])
                self.floor_not_fall[floor_counter][1] = self.floor[i][0] + 16
                final = self.floor[i][0] + 16
            
            elif (self.floor[i][0] + 16 == self.floor[i + 1][0]):
                beggining = self.floor[i][0]
                final = beggining + 16

                floor_counter += 1
                self.floor_not_fall.append([beggining, final])

            print(self.floor_not_fall)
        return self.floor_not_fall