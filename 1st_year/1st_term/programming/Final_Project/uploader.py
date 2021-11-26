import pyxel
import os

pyxel.init(255, 255)
my_files = os.listdir("assets")
my_files.remove("assets.png")
my_files.remove("assets.pyxres")
print(my_files)

for i in range(len(my_files)):
    pyxel.image(0).load(16*int(i), 16, str(r"assets/" + my_files[i]))

pyxel.image(0).load(16, 32, str(r"assets/nubes.png"))

pyxel.save("assets/assets.pyxres")