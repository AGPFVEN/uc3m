import pyxel

class App:
    def __init__(self): #Variables
        
        #Init
        pyxel.init(160, 120)

        #Cube variables
        self.floor_cube = 110
        self.x = 0
        self.y = self.floor_cube
        self.cube_jump = 20
        self.contador = 0
        self.contador_aux = 0

        #Run
        pyxel.run(self.update, self.draw)

    def update(self):
        #Cube movement
        if pyxel.btn(pyxel.KEY_D):
            self.x = (self.x + 1)

        if pyxel.btn(pyxel.KEY_A):
            self.x = (self.x - 1)

        if pyxel.btnp(pyxel.KEY_W) and self.contador_aux == 0:
            self.contador_aux = 2 * self.cube_jump

        if self.contador_aux != 0:

            if(self.contador_aux > self.cube_jump):
                self.y -= 2
                self.contador_aux -= 1

            elif(self.contador_aux > 0):
                self.y += 2
                self.contador_aux -= 1
            

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 8, 8, 9)
        pyxel.text(0, 0, str(self.y), 7)

App()