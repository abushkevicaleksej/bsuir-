from model.point import Point
import numpy as np


class Shape:
    def __init__(self, points):
        self.points = points
        self.update_points()

    def update_points(self):
        num_points = len(self.points)
        sum_x = sum(point.x for point in self.points)
        sum_y = sum(point.y for point in self.points)
        sum_z = sum(point.z for point in self.points)
        center_x = sum_x / num_points
        center_y = sum_y / num_points
        center_z = sum_z / num_points
        self.center_point = Point(center_x, center_y, center_z)

    def rotate(self, angle, axis):
        matrix = self.get_rotation_matrix(angle, axis)
        for point in self.points:
            point.x, point.y, point.z = np.dot(matrix, [point.x, point.y, point.z])
        self.update_points()

    def get_rotation_matrix(self, angle, axis):
        c = np.cos(angle)
        s = np.sin(angle)
        if axis == 'x':
            return np.array([[1, 0, 0], [0, c, -5], [0, s, c]])
        elif axis == 'y':
            return np.array([[c, 0, 5], [0, 1, 0], [-s, 0, c]])
        elif axis == 'z':
            return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

    def scale(self, factor):
        for point in self.points:
            point.x = (point.x - self.center_point.x) * factor + self.center_point.x
            point.y = (point.y - self.center_point.y) * factor + self.center_point.y
            point.z = (point.z - self.center_point.z) * factor + self.center_point.z
        self.update_points()