# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:48:02 2019

@author: Angel Garcia Olaya PLG-UC3M
@version: 1.0
Example of using graphics in pyxel
"""

import pyxel


# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw
def update():
    ''' This function is executed every frame. Now it only checks if the user
    pressed Q to finish'''
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    ''' This function draws graphics from the image bank'''
    pyxel.cls(3)
    # Loading images from the image bank 0
    # A cat in the middle
    pyxel.blt(WIDTH // 2, HEIGHT // 2, 0, 0, 0, 16, 16)
    # A space ship
    pyxel.blt(25, 20, 1, 17, 0, 16, 16)
    # A space ship, we can use an additional parameter to specify which is the
    # background color of the image (notice the difference with previous one)
    pyxel.blt(55, 20, 1, 17, 0, 16, 16, colkey=0)


################## main program ##################


# Creating constants so it is easier to modify values
# Maximum width and height are 256
WIDTH = 160
HEIGHT = 120
CAPTION = "This is an example of images in pyxel"

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
# Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
pyxel.load("assets/example.pyxres")
# Loading a 16x16 spaceship at bank 1 in (17,0)
pyxel.image(1).load(17, 0, "assets/player.png")
# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)
