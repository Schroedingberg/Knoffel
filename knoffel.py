import numpy as np
import re


class dice:

    def __init__(self):
        self.eyes = 1

    def __lt__(self, other):
        return True if self.eyes < other.eyes else False

    def __str___(self):
        return str(self.eyes) + " "

    def roll_dice(self):
        self.eyes = np.random.randint(1, 6)


class ScoreCard:
    # Functions returning functions that compute a score for a figure
    ns = lambda x: sum(filter(lambda y: y == x, x))
    ntuple = lambda x: sum(x)
    fullhouse = lambda x: 25
    smallstraight = lambda x: 30
    largestraight = lambda x: 40
    knoffel = lambda x: 50
    chance = lambda x: sum(x)

    def __init__(self):
        """Initialize object with a dictionary of figure-names, associated with default values of -1"""
        self.figures = {"1s": (ns(1), "1{0,5}"),
                        "2s": (ns(2), "2{0,5}"),
                        "3s": (ns(3) "3{0,5}"),
                        "4s": (ns(4) "4{0,5}"),
                        "5s": (ns(5) "5{0,5}"),
                        "6s": (ns(6) "6{0,5}"),
                        "3Tuple": (ntuple "*"),
                        "4Tuple": (ntuple "*"),
                        "FullHouse": (fullhouse "*"),
                        "SmallStraight": (smallstraight "*"),
                        "LargeStraight": (largestraight "*"),
                        "Knoffel": (knoffel "*"),
                        "Chance": (chance "*")}

        self.card = dict.fromkeys(self.figures.keys(), -1)

    def __str__(self):
        print("Figure | Score")
        for k, v in self.card:
            print("{0} | {1}".format(k, v))

    def is_valid_category(self, category):
        if category in self.card.keys():
            if self.card[category] == -1:
                return True
            elif category not "Chance":
                print("Figure already played")
                return False
        else:
            print("Invalid category")
            return False

    def is_valid_toss(self, category, toss):
        return False

    def get_score_for_curr_toss(self, category, toss):
        return False

    def __setitem__(self, category, toss):
        if is_valid_category(category):
            self.card[category] = toss

    def get_final_score(self):
        return sum(self.card.values())

if __name__ == "__main__":
    d = dice()
    d.roll_dice()
