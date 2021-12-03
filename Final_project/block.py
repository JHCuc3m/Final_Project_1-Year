
class Ground:
    def __init__(self, x: int, y: int):
        """ This method creates the Ground object
        @param x the starting x of the Ground
        @param y the starting y of the Ground"""

        self.sprite = (2, 32, 0, 16, 16, x, y)  # img bank, x and y of the image bank, width, height, x, y and colkey
