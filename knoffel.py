import numpy as np


class dice:

    def __init__(self):
        self.eyes = 1

    def __lt__(self, other):
        return True if self.eyes < other.eyes else False

    def __str___(self):
        return str(self.eyes) + " "

    def roll_dice(self):
        self.eyes = np.random.randint(1, 6)


if __name__ == "__main__":
    d = dice()
    d.roll_dice()
