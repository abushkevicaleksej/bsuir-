import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"