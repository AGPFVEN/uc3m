import pyxel

#I will put the ones that I have, not all the possible needed because is a nonsense because of time and functionality

class Mario:
    #This class stores all the information needed for Mario
    def __init__(self, x:int, y:int, dir:str):
        #This method creates the Mario object
        #param x the starting x of Mario
        #param y the starting y of Mario
        #param dir a string to store the initial direction of Mario.

        self.x = x
        self.y = y

        #Here we are assuming Mario will be always placed at the first
        #bank at first position and it will have fixed size
        self.sprite = (1, 112, 0, 16, 16)
        self.direction = dir

        #We also assume that Mario will always start with 3 lives
        self.lives = 3

    def move(self, direction: str, size: int, prohibited_zones: list):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size and ([self.x + 1, self.y] not in prohibited_zones):
            self.x += 1

        elif direction.lower() == 'left' and self.x > 0 and ([self.x -1, self.y] not in prohibited_zones):
            # I am assuming that if it is not right it will be left
            self.x -= 1

        #Approach: connect the first top left to top right and you cannot pass that line

class Floor_handler:
    def __init__(self, size_of_x, size_of_y):
        #Array with all the invalid zones (all the floors)
        self.floor = []
        self.floor_collider = []

        #Size of all the floors of x * y size
        self.size_X = size_of_x
        self.size_y = size_of_y

        #Sprite of the floor
        self.sprite = (1, 17, 0, 15, 16)

    def create_floor(self, new_x, new_y):
        self.floor.append([new_x, new_y])
        self.floor_collider.append([new_x, new_y])
        self.floor_collider.append([new_x + 16, new_y + 16])
        self.floor_collider.append([new_x + 16, new_y])

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h

        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(100, 200, True)
        self.floor_handler = Floor_handler(16, 16)

        #Create all the floor in the window
        for i in range(int(self.width / 16)):
            self.floor_handler.create_floor(i * 16, 216)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.move('right', self.width, self.floor_handler.floor_collider)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.move('left', self.width, self.floor_handler.floor_collider)

        self.mario.fall(self.height, self.floor_handler.floor_collider)

    def draw(self):
        pyxel.cls(0)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4])

        for i in self.floor_handler.floor:
            pyxel.blt(
                #Position of each block
                i[0], i[1],

                #Image bank
                self.floor_handler.sprite[0],

                #Starting point
                self.floor_handler.sprite[1], self.floor_handler.sprite[2],

                #Size of the image in the bank
                self.floor_handler.sprite[3], self.floor_handler.sprite[4]
            )

        pyxel.text(0, 0, str(str(self.mario.x) + " " + str(self.mario.y)), 7)