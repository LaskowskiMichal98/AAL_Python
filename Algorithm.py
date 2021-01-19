import math
import time
from Card import Card


class Algorithm:
    def __init__(self):
        self.origin = []
        self.Y = []
        self.V = []
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

        y_full = sorted(y_full)  # timsort - worst case O(nlogn)

        previous = y_full[0]
        for card in y_full[1:]:  # remove redundant elements O(n)
            if card != previous:
                self.Y.append(previous)
                previous = card
            else:
                previous.L += card.L
                previous.R += card.R
        self.Y.append(previous)

    def run(self, data):
        start_time = time.time()
        self.origin = data
        self.create_y_list()

        self.V.append(sum(self.Y[0].L + self.Y[1].R, start=Card(0, 0)))

        v_k = self.V[-1]

        for y in self.Y[1:]:  # 5. O(n)
            self.V.append(self.V[-1] + sum(y.L, start=Card(0, 0)) - sum(y.R, start=Card(0, 0)))
            if self.V[-1].length() > v_k.length():
                v_k = self.V[-1]

        for card in self.origin:  # find vecs from origin that sums up to v_k O(n)
            if card * v_k > 0:
                self.solution.append(card)
        self.time = time.time() - start_time

    def return_results(self):
        final_x = 0
        final_y = 0

        for i in range(len(self.solution)):
            final_x += self.solution[i].x
            final_y += self.solution[i].y

        final_trip = math.sqrt(math.pow(final_x, 2) + math.pow(final_y, 2))
        return final_x, final_y, final_trip, self.time

    def reset(self):
        self.origin = 0
        self.Y = 0
        self.V = 0
        self.solution = 0
