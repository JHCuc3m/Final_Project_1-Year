from mario import Mario
import time
import pyxel


class Board:
    """ This class contains all the information needed to represent the
    board"""

    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width / 2, 200, True)
        self.velocity = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if pyxel.btn(pyxel.KEY_X):
                self.mario.run('right', self.width)
            else:
                self.mario.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            if pyxel.btn(pyxel.KEY_X):
                self.mario.run('left', self.width)
            else:
                self.mario.move('left', self.width)

        if pyxel.btn(pyxel.KEY_Z): #and self.mario.y >= 200:
            self.mario.jump("up", self.height)

        if self.mario.jump_force != 10 and self.mario.y >= 200:
            self.mario.jump_force = 15

    def draw(self):
        pyxel.cls(0)

        #the gravity, when it is not in the ground, Mario starts falling

        if self.mario.y >= 200: #and self.velocity != 0:
            self.velocity = 0
        else:
            self.velocity += 0.2

            self.mario.y += self.velocity
            time.sleep(0.001)

        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size

        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4])
