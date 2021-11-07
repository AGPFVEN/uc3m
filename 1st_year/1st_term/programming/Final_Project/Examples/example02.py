# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:05:18 2019

@author: Angel Garcia Olaya PLG-UC3M
@version: 1.1
Showing how to draw figures in pyxel
"""
import pyxel

# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw


def update():
    ''' This function is executed every frame. Now it only checks if the
    Escape key or Q are pressed to finish the program'''
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    ''' This function draws geometrical figures on the screen every turn'''
    # We set the background color, anything on the screen is erased
    # See pyxel documentation for available colors (16)
    # 0 is black
    pyxel.cls(1)
    # To draw a line: .line(x1: int, y1: int, x2: int, y2: int, color: int)
    pyxel.line(0, 0, 20, 20, 3)
    # For a rectangle: .rect(x: int, y: int, w: int, h: int, col: int)
    pyxel.rect(20, 20, 10, 30, 4)
    # For the 'frame' of a rectangle
    pyxel.rectb(30, 50, 20, 10, 5)
    # For a circle: circ(x: int, y: int, r: int, col: int)
    pyxel.circ(50, 80, 10, 6)
    # For a circle 'frame'
    pyxel.circb(100, 30, 15, 7)
    # For a single pixel: pset(x: int, y: int, col: int)
    pyxel.pset(120, 100, 8)


################## main program ##################

# Creating constants so it is easier to modify values
# Maximum width and height are 256
WIDTH = 160
HEIGHT = 120
CAPTION = "This is an example of drawing figures in pyxel"

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)

# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)
