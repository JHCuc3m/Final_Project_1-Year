from mario import Mario
import time
import pyxel
from enemies import Mushroom, Turtle
from block import Ground, Brick, Question, Tunnel, BigTunnel, BiggerTunnel
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
            if i != 816:
                block = Ground(i, 236)
                block2 = Ground(i, 252)

            self.obstacles.append(block)
            self.obstacles.append(block2)

        """block3 = Ground(10, 180)
        block4 = Ground(40, 140)
        block5 = Ground(80, 100)
        block7 = Ground(350, 220)"""

        """block3 = Ground(10, 180)
        block4 = Ground(40, 140)
        block5 = Ground(80, 100)
        block7 = Ground(350, 220)"""
        block7 = Question(104, 170)
        block8 = Brick(152, 170)
        block9 = Question(168, 170)
        block10 = Brick(184, 170)
        block11 = Question(200, 170)
        block12 = Brick(216, 170)
        block13 = Tunnel(296, 204)
        block14 = Question(184, 110)
        block15 = BigTunnel(424, 196)
        block16 = BiggerTunnel(552, 188)
        block17 = BiggerTunnel(648, 188)
        block18 = Brick(776, 170)
        self.obstacles.append(block18)

        """self.obstacles.append(block7)

        self.obstacles.append(block3)

        self.obstacles.append(block4)

        self.obstacles.append(block5)"""

        self.obstacles.append(Ground(500, 220))
        self.obstacles.append(block7)
        self.obstacles.append(block8)
        self.obstacles.append(block9)
        self.obstacles.append(block10)
        self.obstacles.append(block10)
        self.obstacles.append(block10)
        self.obstacles.append(block11)
        self.obstacles.append(block12)
        self.obstacles.append(block13)
        self.obstacles.append(block14)
        self.obstacles.append(block15)
        self.obstacles.append(block16)
        self.obstacles.append(block17)
        block19 = Question(952, 170)
        self.obstacles.append(block19)
        block20 = Brick(968, 170)
        self.obstacles.append(block20)
        block21 = Brick(984, 110)
        self.obstacles.append(block21)
        block22 = Brick(1000, 110)
        self.obstacles.append(block22)
        block23 = Brick(1016, 110)
        self.obstacles.append(block23)
        block24 = Brick(1032, 110)
        self.obstacles.append(block24)
        block25 = Brick(1048, 110)
        self.obstacles.append(block25)
        block26 = Brick(1064, 110)
        self.obstacles.append(block26)
        block27 = Brick(1080, 110)
        self.obstacles.append(block27)
        block28 = Brick(1096, 110)
        self.obstacles.append(block28)
        block29 = Brick(1112, 110)
        self.obstacles.append(block29)
        block30 = Brick(1208, 110)
        self.obstacles.append(block30)
        block31 = Brick(1176, 110)
        self.obstacles.append(block31)
        block32 = Brick(1192, 110)
        self.obstacles.append(block32)
        block33 = Question(1224, 110)
        self.obstacles.append(block33)
        block34 = Brick(1224, 170)
        self.obstacles.append(block34)
        block35 = Brick(1284 + 60, 170)
        self.obstacles.append(block35)
        block36 = Brick(1300 + 60, 170)
        self.obstacles.append(block36)
        block37 = Question(1348 + 120, 170)
        self.obstacles.append(block37)
        block38 = Question(1380 + 180 - 16, 170)
        self.obstacles.append(block38)
        block39 = Question(1380 + 180 - 16, 110)
        self.obstacles.append(block39)
        block40 = Question(1620, 170)
        self.obstacles.append(block40)
        block41 = Brick(1728, 170)
        self.obstacles.append(block41)
        block42 = Brick(1804, 110)
        self.obstacles.append(block42)
        block43 = Brick(1820, 110)
        self.obstacles.append(block43)
        block44 = Brick(1836, 110)
        self.obstacles.append(block44)
        block45 = Brick(1944, 110)
        self.obstacles.append(block45)
        block46 = Question(1960, 110)
        self.obstacles.append(block46)
        block47 = Question(1976, 110)
        self.obstacles.append(block47)
        block48 = Brick(1992, 110)
        self.obstacles.append(block48)
        block49 = Brick(1960, 170)
        self.obstacles.append(block49)
        block50 = Brick(1976, 170)
        self.obstacles.append(block50)


        obstacles_copy = copy.deepcopy(self.obstacles)

        obstacles_copy2 = copy.deepcopy(self.obstacles)
        enemy1 = Mushroom(220, 200, True, obstacles_copy2)
        enemy2 = Mushroom(100, 100, True, obstacles_copy2)

        self.enemies = []

        self.enemies.append(enemy1)
        self.enemies.append(enemy2)
        self.enemies.append(Turtle(400, 220, False, obstacles_copy2))

        self.mario = Mario(self.width / 2, 220, True, obstacles_copy, self.enemies)

        self.velocities = [0] * (len(self.enemies) + 1)

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
            self.mario.jump("up")

        if self.mario.jump_force != 13 and (self.mario.in_the_ground() or self.mario.in_the_enemy()):
            self.mario.jump_force = 13

        for block in self.obstacles:

            if self.big_x >= block.sprite[4]:
                self.progress = self.big_x - self.width

        self.enemy_kill_mario()

        # move the map if neccesary

        self.move_map()

        if self.mario.y > 255:
            self.restart()

    def enemy_kill_mario(self):
        for enemy in self.enemies:
            enemy.move(self.progress)

            if enemy.alive:
                if self.mario.in_the_enemy([enemy]):
                    enemy.alive = False
            else:
                if type(enemy) == Turtle:
                    if not self.mario.in_the_enemy([enemy]):
                        enemy.second_time = True
                    enemy.revive()
                    if self.mario.in_the_enemy([enemy]) and enemy.second_time:
                        enemy.shot = True

                    if enemy.shot:
                        enemy.move(self.progress, 1)  # turtle is shot by Mario
                        enemy.move(self.progress, 1)
                        enemy.move(self.progress, 1)
                        enemy.move(self.progress, 1)
                        enemy.move(self.progress, 1)

                    #the turtle kills the mushroom when being shot
                    for mushroom in self.enemies:
                        if type(mushroom) == Mushroom:
                            if (round(enemy.x + enemy.sprite[3]) - mushroom.x) >= 0 and (
                                    round(enemy.x) - (mushroom.x + mushroom.sprite[3])) <= 0 \
                                    and round(enemy.y) + enemy.sprite[4] > mushroom.y \
                                    and round(enemy.y) < mushroom.y + mushroom.sprite[4]:
                                mushroom.alive = False
                                #mushroom.sprite[3] = 0
                                #mushroom.sprite[4] = 0

                    if enemy.alive and enemy.shot: #the turtle disappear after 5 seconds being shot
                        pass
                        enemy.sprite[3] = 0
                        enemy.sprite[4] = 0

                elif type(enemy) == Mushroom: #the mushroom disappear when killed
                    pass
                    enemy.sprite[3] = 0
                    enemy.sprite[4] = 0

            """
            (round(self.mario.x + self.mario.sprite[3]) - enemy.x + self.progress) >= 0 and (
                    round(self.mario.x) - (enemy.x + enemy.sprite[3]) + self.progress) <= 0 \
                    and 2 > round(self.mario.y) + self.mario.sprite[4] - enemy.y > 0:"""

            if enemy.alive:
                if (round(self.mario.x + self.mario.sprite[3]) - enemy.x + self.progress) >= 0 and (
                        round(self.mario.x) - (enemy.x + enemy.sprite[3]) + self.progress) <= 0 \
                        and round(self.mario.y) + self.mario.sprite[4] > enemy.y \
                        and round(self.mario.y) < enemy.y + enemy.sprite[4]:
                    self.restart()
            elif type(enemy) == Turtle and enemy.third_time:
                if ((round(self.mario.x + self.mario.sprite[3]) - enemy.x + self.progress) >= 0 and (
                        round(self.mario.x) - (enemy.x + enemy.sprite[3]) + self.progress) <= 0 \
                        and round(self.mario.y) + self.mario.sprite[4] > enemy.y \
                        and round(self.mario.y) < enemy.y + enemy.sprite[4]) or self.mario.in_the_enemy():
                    self.restart()

            if  type(enemy) == Turtle and enemy.shot and not self.mario.in_the_enemy():
                enemy.third_time = True


    def restart(self):
        self.big_x = self.width
        self.mario.lives -= 1
        self.mario.x = self.width / 2
        self.mario.y = 210
        self.mario.obstacles = copy.deepcopy(self.obstacles)
        self.mario.previous_progress = 0


    def draw(self):
        pyxel.cls(12)

        # the gravity, when it is not in the ground, Mario starts falling

        self.gravity_mario()
        # We draw things taking the values the objects
        # Parameters are x, y, image bank, the starting x and y and the size

        self.print_mario()
        self.print_obstacles()
        self.print_enemies_with_gravity()

    def gravity_mario(self):
        if self.mario.in_the_ground() or self.mario.in_the_enemy():
            self.velocities[0] = 0
        else:
            self.velocities[0] += 0.2
            self.mario.y += self.velocities[0]
            time.sleep(0.001)

    def move_map(self):
        if self.mario.x > (self.width / 2):
            self.big_x += (self.mario.x - (self.width / 2))
            self.mario.x = self.width / 2

    def print_mario(self):
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4])

    def print_obstacles(self):
        for block in self.obstacles:
            if self.big_x >= block.sprite[4]:
                self.progress = self.big_x - self.width

                pyxel.blt(block.sprite[5] - self.progress, block.sprite[6], block.sprite[0],
                          block.sprite[1], block.sprite[2], block.sprite[3],
                          block.sprite[4])

    def print_enemies_with_gravity(self):
        if len(self.enemies) != 0 and self.mario.lives == self.enemies[0].mario_previous_lives:
            for enemy in self.enemies:

                if enemy.in_the_ground():
                    self.velocities[self.enemies.index(enemy) + 1] = 0
                else:
                    self.velocities[self.enemies.index(enemy) + 1] += 0.2

                    enemy.y += self.velocities[self.enemies.index(enemy) + 1]

                    time.sleep(0.001)

                if self.big_x >= enemy.sprite[4]:
                    pyxel.blt(enemy.x - self.progress, enemy.y, enemy.sprite[0],
                              enemy.sprite[1], enemy.sprite[2], enemy.sprite[3],
                              enemy.sprite[4])

        else:
            for enemy in self.enemies:
                enemy.x = enemy.sprite[5]
                enemy.y = enemy.sprite[6]
                enemy.mario_previous_lives = self.mario.lives
                enemy.dir = enemy.sprite[7]
                enemy.alive = True
                enemy.sprite[3] = 16 #for now all enemies size are 16 *16, but it depends. If the size were not 16*16, we would have to use parameter to store this info
                enemy.sprite[4] = 16
                if type(enemy) == Turtle:
                    enemy.shot = False
                    enemy.second_time = False
                    enemy.third_time = False