from floor import Floor_handler
from mario import Mario
import pyxel

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h

        self.floor_handler = Floor_handler(16, 16)

        #Create all the floor in the window
        self.floor_handler.create_floor(0, self.height - self.floor_handler.sprite[4])
        for i in range(int((int(self.width / 16)) / 2)):
            self.floor_handler.create_floor(32 + (i * self.floor_handler.sprite[3]), self.height - self.floor_handler.sprite[4])

        self.floor_handler.create_floor_not_fall()

        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width / 2, self.height / 2, True, self.floor_handler.floor_not_fall)
        #self.mario = Mario(0,0, True)

        print(self.floor_handler.floor)
        print(self.floor_handler.floor_not_fall)

    def update(self):
        #Here will be th colliders summed in just one list----------REVIEW HOW TO COPY ARRAYS SAFELY
        #NEED TO PUT THE COLLIDERS IN A VARIABLE AND THEN USE IT IN THE INIT OF MARIO ??????
        self.mario.collisions(self.floor_handler.floor_not_fall)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.accelerate('right', self.width, self.floor_handler.floor_not_fall)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.accelerate('left', self.width, self.floor_handler.floor_not_fall)
        
        self.mario.move()

    def draw(self):
        pyxel.cls(12)

        pyxel.bltm(0, 0, 1, 0, 0, 32, 16) #Change the third number to 0 (now is 1)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], 12)

        #Drawing each block of floor
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