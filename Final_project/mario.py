class Mario:
    """ This class stores all the information needed for Mario"""

    def __init__(self, x: int, y: int, dir: bool, obstacles: list, enemies:list):
        """ This method creates the Mario object
        @param x the starting x of Mario
        @param y the starting y of Mario
        @param dir a boolean to store the initial direction of Mario.
                True is facing right, False is facing left"""
        self.x = x
        self.y = y
        self.direction = dir

        self.sprite = [0, 48, 16, 16, 16]  # img bank, x and y of the image bank, width, height and colkey
        # We also assume that Mario will always have three lives in the beginning
        self.lives = 3

        self.jump_force = 13
        self.obstacles = obstacles
        self.previous_progress = 0.00
        self.enemies = enemies

    def in_the_ground(self):
        for obstacle in self.obstacles:
            if abs(self.y + self.sprite[4] - obstacle.sprite[6]) < 4 \
                 and (round(self.x + self.sprite[3]) > obstacle.sprite[5]) \
                      and (round(self.x) < (obstacle.sprite[5] + obstacle.sprite[3])
                 ):
                return True
        return False

    def in_the_enemy(self, dangerous_enemies = []):
        if dangerous_enemies == []:
            dangerous_enemies = self.enemies
        for enemy in dangerous_enemies:
            if abs(self.y + self.sprite[4] - enemy.y) < 4 \
                    and (round(self.x + self.sprite[3]) > enemy.x - self.previous_progress) \
                    and (round(self.x) < (enemy.x + enemy.sprite[3]) - self.previous_progress):
                return True
        return False

    def at_the_ceiling(self):
        for obstacle in self.obstacles:
            if (((abs(self.y - (obstacle.sprite[6] + obstacle.sprite[4])) < 5) \
                 and (round(self.x + self.sprite[2]) > obstacle.sprite[5]) \
                 and (round(self.x) < obstacle.sprite[5] + obstacle.sprite[3]))):
                return True

        return False

    def move(self, direction: str, size: int, speed: int, progress:int):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size and self.lives > 0:
            self.sprite[1] = 48
            go = True
            for obstacle in self.obstacles:

                obstacle.sprite[5] -= (progress - self.previous_progress)

                if not (abs(round(self.x + self.sprite[3]) - obstacle.sprite[5]) > 1 \
                        or (round(self.y) + self.sprite[4] < obstacle.sprite[6] + 3 \
                            or round(self.y) > obstacle.sprite[6] + obstacle.sprite[4])):
                    go = False
            if go:
                self.x += speed

            self.previous_progress = progress

        elif direction.lower() == 'left' and self.x > 0 and self.lives > 0:
            self.sprite[1] = 32
            go = True
            for obstacle in self.obstacles:

                if not (abs(round(self.x) -(obstacle.sprite[5] + obstacle.sprite[3])) > 1 \
                        or (round(self.y) + self.sprite[4] < obstacle.sprite[6] + 3 \
                            or round(self.y) > obstacle.sprite[6] + obstacle.sprite[4])):
                    go = False
            if go:
                self.x -= speed

    def jump(self, direction: str):
        """ This is an example of a method that makes Mario jump, it receives the
                direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the upper border
        if not self.at_the_ceiling() and self.lives > 0:
            if direction.lower() == 'up' and self.y > 0:
                self.y = self.y - self.jump_force
                if self.jump_force > 0:
                    self.jump_force -= 1
