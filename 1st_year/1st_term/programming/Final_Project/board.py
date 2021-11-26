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

        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(0, 100, True)
        self.floor_handler = Floor_handler(16, 16)

        #Create all the floor in the window
        #self.floor_handler.create_floor(0, 216)
        #for i in range(int((int(self.width / 16)) / 2)):
            #self.floor_handler.create_floor(100 + (i * 16), 216)

        #self.floor_handler.create_floor_not_fall()


        #print(self.floor_handler.floor)
        #print(self.floor_handler.floor_not_fall)
        counter = 0

        for i in range(self.width + 1):
            for j in range(self.height + 1):
                if(pyxel.tilemap(0).get(i, j) == 1):
                    print(i, j)
                    counter += 1

        print(counter)


    def update(self):
        self.mario.collisions(self.width, self.floor_handler.floor_not_fall)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.accelerate('right', self.width, self.floor_handler.floor_not_fall)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.accelerate('left', self.width, self.floor_handler.floor_not_fall)
        
        self.mario.move()

    def draw(self):
        pyxel.cls(12)

        pyxel.bltm(0, 0, 0, 0, 0, 32, 16)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], 12)

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