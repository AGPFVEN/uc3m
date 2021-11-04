# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:39:31 2019

@author: Angel Garcia Olaya PLG-UC3M
@version: 1.0
Example of simple use of pyxel. It shows how to write text, how to change its
 color and how to move it
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
    ''' This function puts things on the screen every turn. Now only text '''
    # We set the background color, anything on the screen is erased
    # See pyxel documentation for available colors (16)
    # 0 is black
    pyxel.cls(0)
    # with .text(x:int,y:int,text:str,color:int) we draw a text in the screen
    pyxel.text(0, 0, "Hello, welcome to pyxel", 2)
    # we use pyxel.frame_count to do things every frame (here changing color)
    pyxel.text(0, 10, "Changing color every frame", pyxel.frame_count % 16)
    # this is done every frame... moving a text until it reaches the end
    # we can know the width and height of the screen using pyxel.width or
    # pyxel.height
    x = pyxel.frame_count % pyxel.width
    pyxel.text(x, 20, "Moving text", 3)


################## main program ##################


# Creating constants so it is easier to modify values
# Maximum width and height are 256
WIDTH = 256
HEIGHT = 256
CAPTION = "This is the first pyxel example"

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)

# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)
