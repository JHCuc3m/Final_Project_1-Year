from mario import Mario
import time
import pyxel
from enemies import Enemy
from block import Ground


class Board:
    """ This class contains all the information needed to represent the
    board"""

    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.obstacles = []
        for i in range(0, 1000, 16):
            block = Ground(i, 236)
            block2 = Ground(i, 252)

            self.obstacles.append(block)
            self.obstacles.append(block2)
        block3 = Ground(10, 180)
        block4 = Ground(40, 140)
        block5 = Ground(80, 100)
        block6 = Ground(300, 220)

        self.obstacles.append(block3)

        self.obstacles.append(block4)

        self.obstacles.append(block5)
        self.obstacles.append(block6)

        self.mario = Mario(self.width / 2, 220, True, self.obstacles)

        self.velocity = 0

        self.big_x = 255

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

        if self.mario.x > self.width / 2:
            self.big_x += (self.mario.x - self.width/2)
            self.mario.x = self.width/2


        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4])

        for block in self.obstacles:
            if self.big_x >= block.sprite[4]:
                progress = self.big_x - 255
                pyxel.blt(block.sprite[4]- progress, block.sprite[5], block.sprite[0],
                          block.sprite[1], block.sprite[2], block.sprite[3],
                          block.sprite[6])
