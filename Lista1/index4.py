import pyxel

class App:
    def __init__(self):
        pyxel.init(180,180, title="Questão 4")
        self.x = 0
        pyxel.run(self.update, self.draw)   

    def update(self):
        pass
    

    def draw(self):
        pyxel.cls(0)
        pyxel.line(pyxel.mouse_x, pyxel.mouse_y,0,0,5,)

App()        

