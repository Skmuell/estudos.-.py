import pyxel

class App:
    def __init__(self):
        pyxel.init(180,180, title="Questão 5")
        self.x = 0
        pyxel.run(self.update, self.draw)   

    def update(self):
        pass
    

    def draw(self):
        pyxel.cls(0)
        pyxel.line(pyxel.mouse_x, pyxel.mouse_y,0,0,5,)
        pyxel.line(pyxel.mouse_x, pyxel.mouse_y,180,180,5,)
        pyxel.line(pyxel.mouse_x, pyxel.mouse_y,180,0,5,)
        pyxel.line(pyxel.mouse_x, pyxel.mouse_y,0,180,5,)

App()        