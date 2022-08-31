import pyxel

class App:
    def __init__(self):
        pyxel.init(180,180, title="Questão 2")
        pyxel.run(self.update, self.draw)   

    def update(self):
        pass
    

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y,20,20,7)

App()        