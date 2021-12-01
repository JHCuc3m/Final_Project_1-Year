import time


class Enemy:
    def __init__(self, x: int, y: int, dir: bool):
        """ This method creates the Enemy object
        @param x the starting x of the Enemy
        @param y the starting y of the Enemy
        @param dir a boolean to store the initial direction of the enemy.
                True is facing right, False is facing left"""

        self.direction = dir

        self.sprite = (0, 0, 16, 16, x, y, 16)  # img bank, x and y of the image bank, width, height, x, y and colkey

        self.alive = True

    def move(self, direction: str):
        """ This is an example of a method that moves the enemy, it receives the
                direction"""
        if direction.lower() == 'left':
            self.x -= 1


