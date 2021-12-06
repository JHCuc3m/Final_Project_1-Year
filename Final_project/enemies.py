import time


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

        self.direction = dir

        self.sprite = [1, 0, 0, 16, 16, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey

        self.alive = True

        self.previous_progress = 0

        self.obstacles = obstacles

    def move(self, progress: int):
        """ This is an example of a method that moves the enemy, it receives the
                direction"""
        # self.sprite[1] = 48

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
            self.x -= 1

        self.previous_progress = progress


class Mushroom(Enemy):
    def __init__(self, x: int, y: int, dir: bool, obstacles: list):
        super().__init__(x, y, dir, obstacles)
