import math
import time
from Card import Card


class Algorithm:
    def __init__(self):
        self.origin = []  # initial vector set for which we want to find the solution
        self.solution = []
        self.time = None

    def create_y_list(self):
        y_full = []
        for card in self.origin:  # O(n)
            left = card.rotate(90).normalize()
            left.L.append(card)
            y_full.append(left)

            right = card.rotate(-90).normalize()
            right.R.append(card)
            y_full.append(right)

        y_full = sorted(y_full)  # timsort - worst case O(nlogn), best  O(n)

        y = list()  # normalized and rotated elements of initial set without redundant elements
        previous = y_full[0]
        for card in y_full[1:]:  # remove redundant elements O(n)
            if card != previous:
                y.append(previous)
                previous = card
            else:  # keep all information about L and R sets but within a single vector
                """ L will contain all vectors from the initial set
                that after rotation by 90 degrees and normalization will give the same vector as 'previous'
                """
                previous.L += card.L
                previous.R += card.R  # same as L but the rotation is by -90 degrees
        y.append(previous)

        return y

    def run(self, data):
        start_time = time.time()
        self.origin = data
        y = self.create_y_list()

        # v is set of possible best solutions, longest vec from v will be the best solution
        v = [sum(y[0].L + y[1].R, start=Card(0, 0))]
        v_k = v[-1]  # the furthest point that can be reached by summing vectors from the initial set

        for y in y[1:]:  # point 5 of algorithm description O(n)
            v.append(v[-1] + sum(y.L, start=Card(0, 0)) - sum(y.R, start=Card(0, 0)))
            if v[-1].length() > v_k.length():
                v_k = v[-1]

        # find vectors from origin that sums up to v_k O(n)
        self.solution = [card for card in self.origin if card * v_k > 0]

        self.time = time.time() - start_time

    def return_results(self):
        final_vec = sum(self.solution, start=Card(0, 0))
        return final_vec.x, final_vec.y,  final_vec.length(), self.time

    def reset(self):
        self.origin = 0
        self.solution = 0
