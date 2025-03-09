import math

class Polygon:
    def __init__(self):
        self.points = []  # Список точек в формате (x, y)

    def add_point(self, point):
        self.points.append(point)

    def is_convex(self):
        n = len(self.points)
        if n < 3:
            return False
        sign = 0
        for i in range(n):
            p0 = self.points[i]
            p1 = self.points[(i + 1) % n]
            p2 = self.points[(i + 2) % n]
            dx1 = p1[0] - p0[0]
            dy1 = p1[1] - p0[1]
            dx2 = p2[0] - p1[0]
            dy2 = p2[1] - p1[1]
            cross = dx1 * dy2 - dy1 * dx2
            current_sign = math.copysign(1, cross) if cross != 0 else 0
            if current_sign != 0:
                if sign == 0:
                    sign = current_sign
                elif sign != current_sign:
                    return False
        return True

    def inner_normals(self):
        normals = []
        n = len(self.points)
        if n < 2:
            return normals
        # Находим центр многоугольника для определения направления нормали
        cx = sum(p[0] for p in self.points) / n
        cy = sum(p[1] for p in self.points) / n
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            # Вектор стороны
            vx = p2[0] - p1[0]
            vy = p2[1] - p1[1]
            # Возможные нормали: (-vy, vx) и (vy, -vx)
            normal1 = (-vy, vx)
            normal2 = (vy, -vx)
            # Находим середину отрезка
            midx = (p1[0] + p2[0]) / 2
            midy = (p1[1] + p2[1]) / 2
            dot1 = (cx - midx) * normal1[0] + (cy - midy) * normal1[1]
            dot2 = (cx - midx) * normal2[0] + (cy - midy) * normal2[1]
            normal = normal1 if dot1 > dot2 else normal2
            # Нормализация вектора
            length = math.hypot(normal[0], normal[1])
            if length != 0:
                normal = (normal[0] / length, normal[1] / length)
            normals.append(normal)
        return normals

    def contains_point(self, point):
        """Проверка принадлежности точки многоугольнику методом луча"""
        cnt = 0
        n = len(self.points)
        if n < 3:
            return False
        x, y = point
        for i in range(n):
            a = self.points[i]
            b = self.points[(i + 1) % n]
            if ((a[1] > y) != (b[1] > y)):
                t = (y - a[1]) / (b[1] - a[1])
                if x < a[0] + t * (b[0] - a[0]):
                    cnt += 1
        return cnt % 2 == 1

    def edges(self):
        """Возвращает список сторон (пар точек) многоугольника"""
        return [(self.points[i], self.points[(i + 1) % len(self.points)]) for i in range(len(self.points))]
