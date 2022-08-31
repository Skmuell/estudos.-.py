import pyxel

class App:
    def __init__(self):
        pyxel.init(180, 180,title="Questão 7")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % (pyxel.width -10)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 80, 10, 10, 7)

App()