from mario import Mario
import time
import pyxel
from enemies import Enemy


class Board:
    """ This class contains all the information needed to represent the
    board"""

    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right

        self.enemy1 = Enemy(50, 200, False)
        self.obstacle_positions = [self.enemy1.sprite[2:6]]

        self.mario = Mario(self.width / 2, 200, True, self.obstacle_positions)

        self.velocity = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if pyxel.btn(pyxel.KEY_X):
                self.mario.move('right', self.width, 2)
            else:
                self.mario.move('right', self.width, 1)
        elif pyxel.btn(pyxel.KEY_LEFT):
            if pyxel.btn(pyxel.KEY_X):
                self.mario.move('left', self.width, 2)
            else:
                self.mario.move('left', self.width, 1)

        if pyxel.btn(pyxel.KEY_Z):  # and self.mario.y >= 200:
            self.mario.jump("up", self.height)

        if self.mario.jump_force != 10 and self.mario.in_the_ground():
            self.mario.jump_force = 13

    def draw(self):
        pyxel.cls(12)

        # the gravity, when it is not in the ground, Mario starts falling

        if self.mario.in_the_ground():
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

        pyxel.blt(self.enemy1.sprite[4], self.enemy1.sprite[5], self.enemy1.sprite[0],
                  self.enemy1.sprite[1], self.enemy1.sprite[2], self.enemy1.sprite[3],
                  self.enemy1.sprite[6])
