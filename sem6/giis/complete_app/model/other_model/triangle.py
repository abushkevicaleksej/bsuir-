from model.other_model.point import Point
from model.other_model.edge import Edge

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.points = [p1, p2, p3]
        self.edges = [Edge(p1, p2), Edge(p2, p3), Edge(p3, p1)]
        self.circumcenter, self.radius = self.circumcircle()

    def circumcircle(self):
        A = self.points[0]
        B = self.points[1]
        C = self.points[2]

        d = 2 * (A.x*(B.y - C.y) + B.x*(C.y - A.y) + C.x*(A.y - B.y))
        if d == 0:
            return (Point(0, 0), float('inf'))
        ux = ((A.x**2 + A.y**2)*(B.y - C.y) + (B.x**2 + B.y**2)*(C.y - A.y) + (C.x**2 + C.y**2)*(A.y - B.y)) / d
        uy = ((A.x**2 + A.y**2)*(C.x - B.x) + (B.x**2 + B.y**2)*(A.x - C.x) + (C.x**2 + C.y**2)*(B.x - A.x)) / d
        center = Point(ux, uy)
        radius = center.distance(A)
        return center, radius

    def contains_in_circumcircle(self, p: Point):
        return self.circumcenter.distance(p) < self.radius

    def __repr__(self):
        return f"Triangle({self.points[0]}, {self.points[1]}, {self.points[2]})"