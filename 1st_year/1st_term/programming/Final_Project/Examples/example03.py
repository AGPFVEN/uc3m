# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:31:32 2019

@author: Angel Garcia Olaya PLG-UC3M
@version: 1.0
This program shows how to move things in pyxel
"""

import pyxel

# We create a list with the coordinates that we will use inside the functions
# This is a way to change positions in update() and draw(), but an
# OO approach is recommended to work with pyxel
position = [10, 10]


def move(x, y):
    ''' This function checks if the arrows of the keyboard are pressed and
    updates the x and y accordingly.'''
    # See all the keys at:
    # https://github.com/kitao/pyxel/blob/master/pyxel/__init__.py
    # If the arrows are pressed it updates x or y accordingly
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 1
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1

    return x, y


# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw
def update():
    ''' This function is executed every frame. It invokes the move function
     which updates x and y of the circle'''
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        position[0], position[1] = move(position[0], position[1])


def draw():
    ''' This function draws geometrical figures on the screen every turn'''
    # We set the background color, anything on the screen is erased
    # See pyxel documentation for available colors (16)
    # 0 is black
    global x, y
    pyxel.cls(1)
    pyxel.circ(position[0], position[1], 10, 10)


################## main program ##################


# Creating constants so it is easier to modify values
# Maximum width and height are 256
WIDTH = 160
HEIGHT = 120
CAPTION = "This is an example of moving things in pyxel"

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)
