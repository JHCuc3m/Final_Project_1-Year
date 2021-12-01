class Mario:
    """ This class stores all the information needed for Mario"""

    def __init__(self, x: int, y: int, dir: bool, obstacle_positions: list):
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
        self.obstacle_positions = obstacle_positions

    def in_the_ground(self):
        if round(self.y == self.obstacle_positions[0][3]) or self.y > 200:
            return True
        else:
            return False

    def move(self, direction: str, size: int):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            self.sprite[1] = 48
            if round(self.x + self.sprite[2]) != self.obstacle_positions[0][2] \
                    or (round(self.y) < self.obstacle_positions[0][3] \
                        or round(self.y) > self.obstacle_positions[0][3] + self.obstacle_positions[0][1]):
                self.x += 1

        elif direction.lower() == 'left' and self.x > 0:
            self.sprite[1] = 32
            if round(self.x) != self.obstacle_positions[0][2] + self.obstacle_positions[0][0] \
                    or (round(self.y) < self.obstacle_positions[0][3] \
                        or round(self.y) > self.obstacle_positions[0][3] + self.obstacle_positions[0][1]):
                self.x -= 1

    def run(self, direction: str, size: int):
        """ This is an example of a method that runs Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            if round(self.x + self.sprite[2]) != self.obstacle_positions[0][2] \
                    or (round(self.y) < self.obstacle_positions[0][3] \
                        or round(self.y) > self.obstacle_positions[0][3] + self.obstacle_positions[0][1]):
                self.x = self.x + 2
        elif direction.lower() == 'left' and self.x > 0:
            if round(self.x) != self.obstacle_positions[0][2] + self.obstacle_positions[0][0] \
                    or (round(self.y) < self.obstacle_positions[0][3] \
                        or round(self.y) > self.obstacle_positions[0][3] + self.obstacle_positions[0][1]):
                self.x -= 2

    def jump(self, direction: str, size: int):
        """ This is an example of a method that makes Mario jump, it receives the
                direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the upper border
        mario_y_size = self.sprite[4]
        if direction.lower() == 'up' and self.y > 0 and self.in_the_ground():
            self.y = self.y - self.jump_force
            if self.jump_force > 0:
                self.jump_force -= 1
