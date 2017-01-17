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

    def __init__(self):
        """Initialize object with a dictionary of figure-names, associated
        with default values of -1 and the rules(functions) for the scoring of the figures."""

        def ns(n):
            """Private helper function to compute scores of first 6 figures. Just
            returns a function that sums the number provided as argument
            in a list
            """
            return lambda seq: sum(filter(lambda y: y == n, seq))

        self.figures = {"1s": ns(1),
                        "2s": ns(2),
                        "3s": ns(3),
                        "4s": ns(4),
                        "5s": ns(5),
                        "6s": ns(6),
                        "3Tuple": lambda x: sum(x),
                        "4Tuple": lambda x: sum(x),
                        "FullHouse": lambda x: 25,
                        "SmallStraight": lambda x: 30,
                        "LargeStraight": lambda x: 40,
                        "Knoffel": lambda x: 50,
                        "Chance": lambda x: sum(x)}
        # Dictionary with rules to decide whether a toss is valid with
        # respect to the categorys.  It has the same keys as the
        # figures dictionary, but the values are functions, which
        # check whether the toss matches the proposed category. The
        # first 6 figures always return True, because the score is
        # just the sum over eyes count matching n. It would not make sense for
        # the player to choose these figures if his toss does not contain n,
        # but he/she is free to do so.
        self.rules = {"1s": lambda x: True, "2s": True, "3s": True,
                      "4s": True, "5s": True, "6s": True,
                      "3Tuple": lambda seq: 3 in
                      [seq.count(i) for i in set(seq)],
                      "4Tuple": lambda seq: 4 in
                      [seq.count(i) for i in set(seq)],
                      "FullHouse":
                      lambda seq: {2, 3} == set(
                          [seq.count(i) for i in set(seq)]),
                      "SmallStraight": lambda seq: set(range(1, 6)) == set(seq),
                      "LargeStraight": lambda seq: set(range(1, 7)) == set(seq),
                      "Knoffel": True}

        # Initialize dictionary to hold the actual scores for each figure.
        # For this, the keys of the figures dict are just copied again, but
        # associated with -1.
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
        if self.is_valid_category(category):
            return self.rules[category](toss)
        else:
            print("Invalid category")
            return False

    def get_score_for_curr_toss(self, category, toss):
        return False

    def __setitem__(self, category, toss):
        if is_valid_category(category):
            self.card[category] = toss

    def get_final_score(self):
        return sum(self.card.values())


d = dice()
d.roll_dice()
c = ScoreCard()
