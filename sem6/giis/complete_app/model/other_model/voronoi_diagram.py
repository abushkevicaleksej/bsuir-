from model.other_model.point import Point
import math


class VoronoiDiagram:
    def __init__(self, triangles: list):
        self.triangles = triangles
        self.edges = []

    def compute(self):
        edge_dict = {}
        for t in self.triangles:
            for edge in t.edges:
                key = tuple(sorted([(edge.p1.x, edge.p1.y), (edge.p2.x, edge.p2.y)]))
                if key not in edge_dict:
                    edge_dict[key] = []
                edge_dict[key].append(t)

        for edge_key, tris in edge_dict.items():
            if len(tris) == 2:
                c1 = tris[0].circumcenter
                c2 = tris[1].circumcenter
                self.edges.append((c1, c2))
            else:
                t = tris[0]
                c = t.circumcenter
                (x1, y1), (x2, y2) = edge_key
                dx = x2 - x1
                dy = y2 - y1
                norm = math.hypot(dx, dy)
                if norm == 0:
                    continue
                dx, dy = -dy / norm, dx / norm
                far_point = Point(c.x + dx * 1000, c.y + dy * 1000)
                self.edges.append((c, far_point))
        return self.edges
