import math


class Card:
    def __init__(self, x, y):
        self.x = round(x, 3)
        self.y = round(y, 3)

        self.R = []
        self.L = []

    def alpha(self):
        return round(math.atan(self.y / self.x)*180/math.pi, 3)  # angle between OX and vector in degrees

    def rotate(self, angle):
        angle_rad = angle/180*math.pi
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Card(new_x, new_y)

    def normalize(self):
        return Card(self.x/self.length(), self.y/self.length())

    def length(self):
        return round(math.sqrt(self.x**2 + self.y**2), 3)

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

    def __eq__(self, other):
        return self.alpha() == other.alpha()

    def __lt__(self, other):
        return self.alpha() < other.alpha()

    def __add__(self, other):
        return Card(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y