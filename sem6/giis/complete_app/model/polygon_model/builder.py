import math

class ConvexHullBuilder:
    @staticmethod
    def graham_scan(points):
        if len(points) < 3:
            return points[:]
        points_sorted = sorted(points, key=lambda p: (p[1], p[0]))
        base = points_sorted[0]

        def polar_angle(p):
            return math.atan2(p[1] - base[1], p[0] - base[0])

        sorted_points = sorted(points_sorted[1:], key=polar_angle)
        hull = [base, sorted_points[0]]
        for p in sorted_points[1:]:
            while len(hull) >= 2:
                p1 = hull[-2]
                p2 = hull[-1]
                cross = (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])
                if cross <= 0:
                    hull.pop()
                else:
                    break
            hull.append(p)
        return hull

    @staticmethod
    def jarvis_march(points):
        n = len(points)
        if n < 3:
            return points[:]
        leftmost = min(points, key=lambda p: p[0])
        hull = []
        p = leftmost
        while True:
            hull.append(p)
            q = points[0]
            for r in points:
                if r == p:
                    continue
                cross = ((q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]))
                if q == p or cross < 0:
                    q = r
            p = q
            if p == leftmost:
                break
        return hull
