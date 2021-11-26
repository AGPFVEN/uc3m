from board import Board
import pyxel

#Declaring the width and height of the frame
frame_width = 255
frame_height = 130

# The first thing to do is to create the screen
pyxel.init(frame_width, frame_height, caption="This is my final project")

# Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
pyxel.load("assets/resources.pyxres")

#Then we initialize "the game itself"
board = Board(frame_width, frame_height)

# To start the game we invoke the run method with the update and draw functions
pyxel.run(board.update, board.draw)


#Mario acelera al saltar ?python -c "import pyxel; print(site.getsitepackages())"
