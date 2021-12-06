from mario import Mario
import time
import pyxel
from enemies import Enemy, Mushroom
from block import Ground
import copy


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
        self.progress = 0.00

        for i in range(0, 1000, 16):
            block = Ground(i, 236)
            block2 = Ground(i, 252)

            self.obstacles.append(block)
            self.obstacles.append(block2)

        block3 = Ground(10, 180)
        block4 = Ground(40, 140)
        block5 = Ground(80, 100)
        block7 = Ground(350, 220)

        self.obstacles.append(block7)

        self.obstacles.append(block3)

        self.obstacles.append(block4)

        self.obstacles.append(block5)

        obstacles_copy = copy.deepcopy(self.obstacles)

        obstacles_copy2 = copy.deepcopy(self.obstacles)
        enemy1 = Mushroom(220, 220, True, obstacles_copy2)

        self.enemies = []

        self.enemies.append(enemy1)

        enemies_copy = copy.deepcopy((self.enemies))

        self.mario = Mario(self.width / 2, 220, True, obstacles_copy, enemies_copy)

        self.velocity = 0

        self.big_x = 255




    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if pyxel.btn(pyxel.KEY_X):
                self.mario.move('right', self.width, 2, self.progress)
            else:
                self.mario.move('right', self.width, 1, self.progress)
        elif pyxel.btn(pyxel.KEY_LEFT):
            if pyxel.btn(pyxel.KEY_X):
                self.mario.move('left', self.width, 2, self.progress)
            else:
                self.mario.move('left', self.width, 1, self.progress)

        if pyxel.btn(pyxel.KEY_Z):  # and self.mario.y >= 200:
            self.mario.jump("up", self.height)

        if self.mario.jump_force != 10 and self.mario.in_the_ground():
            self.mario.jump_force = 13

        for block in self.obstacles:

            if self.big_x >= block.sprite[4]:
                self.progress = self.big_x - self.width

        for enemy in self.enemies:
            enemy.move(self.progress)

            if abs(enemy.x - (self.mario.x + self.progress)) < 2 and enemy.y - (self.mario.y + self.mario.sprite[4] < 2):

                self.mario.sprite[1] = 0
                self.mario.sprite[2] = 0


                big_x = self.width
                self.mario.lives -= 1
                self.mario.x = self.width/2
                self.mario.y = 220



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

        if self.mario.x > (self.width / 2):
            self.big_x += (self.mario.x - (self.width / 2))
            self.mario.x = self.width / 2

        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4])

        for block in self.obstacles:
            if self.big_x >= block.sprite[4]:
                self.progress = self.big_x - self.width

                pyxel.blt(block.sprite[5] - self.progress, block.sprite[6], block.sprite[0],
                          block.sprite[1], block.sprite[2], block.sprite[3],
                          block.sprite[4])

                if block.sprite[5] - self.progress < -16:
                    del self.obstacles[self.obstacles.index(block)]

        for enemy in self.enemies:
            if self.big_x >= enemy.sprite[4]:

                pyxel.blt(enemy.x - self.progress, enemy.y, enemy.sprite[0],
                          enemy.sprite[1], enemy.sprite[2], enemy.sprite[3],
                          enemy.sprite[4])
