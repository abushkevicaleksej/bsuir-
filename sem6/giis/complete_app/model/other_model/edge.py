from model.other_model.point import Point

class Edge:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return (self.p1 == other.p1 and self.p2 == other.p2) or \
               (self.p1 == other.p2 and self.p2 == other.p1)