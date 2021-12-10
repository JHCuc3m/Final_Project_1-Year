class Ground:
    def __init__(self, x: int, y: int):
        """ This method creates the Ground object
        @param x the starting x of the Ground
        @param y the starting y of the Ground"""

        self.sprite = [2, 32, 0, 16, 16, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey


class Brick:
    def __init__(self, x: int, y: int):
        """ This method creates the Breakable bricks object
        @param x the starting x of the Breakable bricks
        @param y the starting y of the Breakable bricks"""

        self.sprite = [2, 0, 0, 16, 16, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey


class Question:
    def __init__(self, x: int, y: int):
        """ This method creates the question object
        @param x the starting x of the question
        @param y the starting y of the question"""

        self.sprite = [2, 0, 24, 16, 16, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey


class Tunnel:
    def __init__(self, x: int, y: int):
        """ This method creates the tunnel object
        @param x the starting x of the tunnel
        @param y the starting y of the tunnel"""

        self.sprite = [2, 32, 24, 24, 32, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey


class BigTunnel:
    def __init__(self, x: int, y: int):
        """ This method creates the tunnel object
        @param x the starting x of the tunnel
        @param y the starting y of the tunnel"""

        self.sprite = [2, 32, 24, 24, 40, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey



class BiggerTunnel:
    def __init__(self, x: int, y: int):
        """ This method creates the tunnel object
        @param x the starting x of the tunnel
        @param y the starting y of the tunnel"""

        self.sprite = [2, 32, 24, 24, 48, x, y]  # img bank, x and y of the image bank, width, height, x, y and colkey