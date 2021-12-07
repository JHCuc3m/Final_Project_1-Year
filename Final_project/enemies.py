import time
import copy

class Enemy:
    def __init__(self, x: int, y: int, dir: bool, obstacles: list):
        """ This method creates the Enemy object
        @param x the starting x of the Enemy
        @param y the starting y of the Enemy
        @param dir a boolean to store the initial direction of the enemy.
                True is facing right, False is facing left"""

        self.x = x
        self.y = y
        self.dir = dir
        self.mario_previous_lives = 3

        self.sprite = [1, 0, 0, 16, 16, copy.copy(x), copy.copy(y), copy.copy(dir)]  # img bank, x and y of the image bank, width, height, x, y and dir

        self.alive = True

        self.previous_progress = 0

        self.obstacles = obstacles

    def move(self, progress: int):
        """ This is an example of a method that moves the enemy, it receives the
                direction"""
        # self.sprite[1] = 48
        if self.alive:
            for obstacle in self.obstacles:
                # obstacle.sprite[5] -= (progress - self.previous_progress)
                if (abs(round(self.x + self.sprite[3]) - obstacle.sprite[5]) < 1 \
                        and (round(self.y) + self.sprite[4] > obstacle.sprite[6] + 3 \
                             and round(self.y) < obstacle.sprite[6] + obstacle.sprite[4])):
                    self.dir = False
                elif (abs(round(self.x) - (obstacle.sprite[5] + obstacle.sprite[3])) < 1 \
                      and (round(self.y) + self.sprite[4] > obstacle.sprite[6] + 3 \
                           and round(self.y) < obstacle.sprite[6] + obstacle.sprite[4])):
                    self.dir = True

            if self.dir:
                self.x += 0.5
            else:
                self.x -= 0.5

        self.previous_progress = progress

    def in_the_ground(self):
        for obstacle in self.obstacles:
            if abs(self.y + self.sprite[4] - obstacle.sprite[6]) < 4 \
                 and (round(self.x + self.sprite[3]) > obstacle.sprite[5]) \
                      and (round(self.x) < (obstacle.sprite[5] + obstacle.sprite[3])
                 ):
                return True
        return False

class Mushroom(Enemy):
    def __init__(self, x: int, y: int, dir: bool, obstacles: list):
        super().__init__(x, y, dir, obstacles)
