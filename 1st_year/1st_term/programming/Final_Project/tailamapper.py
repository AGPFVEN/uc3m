import pyxel

pyxel.init(255, 255)
pyxel.load("assets/resources.pyxres")

pyxel.image(0).set(33, 0, ["a"])
print(pyxel.tilemap(0).get(0, 14))
pyxel.save("assets/resources.pyxres")