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
    # Helper function to return function for computation of first 6 figures
    ns = lambda x: sum(filter(lambda y: y == x, x))

    def __init__(self):
        """Initialize object with a dictionary of figure-names, associated
        with default values of -1 and the rules for the scoring of the figures."""
        self.figures = {"1s":
                        ns(1),
                        "2s":
                        ns(2),
                        "3s":
                        ns(3),
                        "4s":
                        ns(4),
                        "5s":
                        ns(5),
                        "6s":
                        ns(6),
                        "3Tuple":
                        lambda x: sum(x),
                        "4Tuple":
                        lambda x: sum(x),
                        "FullHouse":
                        lambda x: 25,
                        "SmallStraight":
                        lambda x: 30,
                        "LargeStraight":
                        lambda x: 40,
                        "Knoffel":
                        lambda x: 50,
                        "Chance":
                        lambda x: sum(x)}

        self.card = dict.fromkeys(self.figures.keys(), -1)

    def __str__(self):
        print("Figure | Score")
        for k, v in self.card:
            print("{0} | {1}".format(k, v))

    def is_valid_category(self, category):
        if category in self.card.keys():
            if self.card[category] == -1:
                return True
            elif category != "Chance":
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
