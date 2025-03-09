from model.other_model.point import Point
from model.other_model.triangle import Triangle

class DelaunayTriangulation:
    def __init__(self, points: list):
        self.points = points[:]
        self.triangles = []

    def triangulate(self):
        min_x = min(p.x for p in self.points)
        max_x = max(p.x for p in self.points)
        min_y = min(p.y for p in self.points)
        max_y = max(p.y for p in self.points)
        dx = max_x - min_x
        dy = max_y - min_y
        delta_max = max(dx, dy)
        midx = (min_x + max_x) / 2
        midy = (min_y + max_y) / 2

        p1 = Point(midx - 20 * delta_max, midy - delta_max)
        p2 = Point(midx, midy + 20 * delta_max)
        p3 = Point(midx + 20 * delta_max, midy - delta_max)
        super_triangle = Triangle(p1, p2, p3)
        self.triangles.append(super_triangle)

        for p in self.points:
            bad_triangles = []
            polygon = []

            for t in self.triangles:
                if t.contains_in_circumcircle(p):
                    bad_triangles.append(t)

            for t in bad_triangles:
                for edge in t.edges:
                    is_shared = False
                    for ot in bad_triangles:
                        if ot == t:
                            continue
                        if edge in ot.edges:
                            is_shared = True
                            break
                    if not is_shared:
                        polygon.append(edge)

            for t in bad_triangles:
                if t in self.triangles:
                    self.triangles.remove(t)

            for edge in polygon:
                new_triangle = Triangle(edge.p1, edge.p2, p)
                self.triangles.append(new_triangle)

        self.triangles = [t for t in self.triangles
                          if not (p1 in t.points or p2 in t.points or p3 in t.points)]
        return self.triangles