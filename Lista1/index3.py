import pyxel

class App:
    def __init__(self):
        pyxel.init(180,180, title="Questão 3")
        self.x = 0
        pyxel.run(self.update, self.draw)   

    def update(self):
        pass
    

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(pyxel.mouse_x - 10, pyxel.mouse_y - 10,21,21,5)
        pyxel.circb(pyxel.mouse_x, pyxel.mouse_y,9,7)

App()        