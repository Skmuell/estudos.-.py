import pyxel

class App:
    def __init__(self):
        pyxel.init(180,180, title="Questão 6")
        self.x = 0
        pyxel.run(self.update, self.draw)   
        pyxel.mouse(True)

    def update(self):
        pass
    

    def draw(self):
        pyxel.mouse(True)
        pyxel.cls(0)
        pyxel.rectb(0,0,180,180,7)
        pyxel.rect(1,1,60,60,0)
        pyxel.rect(59,1,60,60,7)
        pyxel.rect(119,1,60,60,0)
        pyxel.rect(1,59,60,60,7)
        pyxel.rect(1,119,60,60,0)
        pyxel.rect(59,59,60,60,0)
        pyxel.rect(59,119,60,60,7)
        pyxel.rect(119,119,60,60,0)
        pyxel.rect(119,59,60,60,7)
        
        
        
App()        