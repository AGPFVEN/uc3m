class Floor_handler:
    def __init__(self, size_of_x, size_of_y):
        #Array with all the invalid zones (all the floors)
        self.floor = []
        self.floor_not_fall = []

        #Size of all the floors of x * y size
        self.size_X = size_of_x
        self.size_y = size_of_y

        #Sprite of the floor
        self.sprite = (0, 16, 16, 16, 16)

    #This function creates blocks (by programing them)
    #It is used for the floor because it`s faster to develop with a loop
    def create_floor(self, new_x, new_y):
        self.floor.append([new_x, new_y])

    #This function will create a list which contains the range of the floors
    #The approach is to check the upper corners so the player can't traspass them
    def create_floor_not_fall(self):
        beggining_x = self.floor[0][0]
        final_x = beggining_x + 16
        floor_counter = 0

        self.floor_not_fall.append([beggining_x, final_x, self.floor[0][1], "stones"])

        for i in range(1, len(self.floor)):
            #print(self.floor[i])
            if (final_x == self.floor[i][0]):
                final_x = self.floor[i][0] + self.sprite[3]
                self.floor_not_fall[floor_counter][1] = final_x
            
            elif(i < len(self.floor) + 1):
                if (self.floor[i][0] + self.sprite[3] == self.floor[i + 1][0]):
                    beggining_x = self.floor[i][0]
                    final_x = beggining_x + self.sprite[3]

                    floor_counter += 1
                    self.floor_not_fall.append([beggining_x, final_x, self.floor[i][1], "stones"])

                print(self.floor_not_fall)