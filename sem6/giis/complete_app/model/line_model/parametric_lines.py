import enum
from view.line_view.workspace import Workspace
from view.line_view.table import Table
import numpy as np

class ParametricCurveMode(enum.Enum):
    none = "Не выбрано"
    erm = "кривая Эрмита"
    bez = "кривая Безье"
    b_spline = "В-сплайн"

class ParametricCurve:
    def __init__(self, curve: ParametricCurveMode, workspace: Workspace, table: Table,
                 p1: list[int, int], p2: list[int, int], p3: list[int, int], p4: list[int, int], r1: list[int, int], r2: list[int, int]):
        self.curve = curve
        self.workspace = workspace
        self.table = table
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.r1 = r1
        self.r2 = r2

    def draw(self):
        if self.curve == ParametricCurveMode.erm:
            points = self._erm_curve()
        elif self.curve == ParametricCurveMode.bez:
            points = self._bez_curve()
        elif self.curve == ParametricCurveMode.b_spline:
            points = self._b_curve()
        else:
            raise ValueError(f"Unsupported parametric curve mode: {self.curve}")

        self.table.update_table(points)
        self.workspace.draw_points(points)

    def _erm_curve(self):
        points = []
        for i in range(0, 11):
            t = i / 10.0

            mtx = [
                [self.p1[0], self.p1[1]],
                [self.p2[0], self.p2[1]],
                [self.r1[0], self.r1[1]],
                [self.r2[0], self.r2[1]]
            ]

            default_mtx = [
                [2, -2, 1, 1],
                [-3, 3, -2, -1],
                [0, 0, 1, 0],
                [1, 0, 0, 0]
            ]
            temp_mtx = multiply_matrices(default_mtx, mtx)
            t_mtx = multiply_matrices([[t ** 3, t ** 2, t, 1]], temp_mtx)
            points.append((t_mtx[0][0], t_mtx[0][1]))
            print(f'ERMITH: {points}')
        return points

    def _bez_curve(self):
        points = []
        for i in range(0, 11):
            t = i / 10.0

            mtx = [
                [self.p1[0], self.p1[1]],
                [self.p2[0], self.p2[1]],
                [self.p3[0], self.p3[1]],
                [self.p4[0], self.p4[1]]
            ]

            default_mtx = [
                [-1, 3, -3, 1],
                [3, -6, 3, 0],
                [-3, 3, 0, 0],
                [1, 0, 0, 0]
            ]
            temp_mtx = multiply_matrices(default_mtx, mtx)
            t_mtx = multiply_matrices([[t ** 3, t ** 2, t, 1]], temp_mtx)
            points.append((t_mtx[0][0], t_mtx[0][1]))
            print(f'BEZ: {points}')
        return points

    def _b_curve(self):
        control_points = [self.p1, self.p2, self.p3, self.p4]
        n = len(control_points) - 1
        k = 3

        knot_vector = self._generate_uniform_knot_vector(n, k)

        points = []

        # Вычисляем точки на кривой
        for i in range(101):
            t = i / 100.0
            x, y = 0, 0

            for j in range(n + 1):
                N = self._basis_function(j, k, t, knot_vector)
                x += N * control_points[j][0]
                y += N * control_points[j][1]

            points.append((x, y))

        return points

    def _basis_function(self, i, k, t, knot_vector):
        if k == 0:
            return 1.0 if knot_vector[i] <= t < knot_vector[i + 1] else 0.0
        else:
            left = 0.0
            right = 0.0

            if knot_vector[i + k] - knot_vector[i] != 0:
                left = ((t - knot_vector[i]) / (knot_vector[i + k] - knot_vector[i])) * self._basis_function(i, k - 1,
                                                                                                             t,
                                                                                                             knot_vector)

            if i + k + 1 < len(knot_vector) and knot_vector[i + k + 1] - knot_vector[i + 1] != 0:
                right = ((knot_vector[i + k + 1] - t) / (
                            knot_vector[i + k + 1] - knot_vector[i + 1])) * self._basis_function(i + 1, k - 1, t,
                                                                                                 knot_vector)

            return left + right

    def _generate_uniform_knot_vector(self, n, k):
        m = n + k + 2
        return [0] * k + list(range(m - 2 * k)) + [m - 2 * k - 1] * k


def multiply_matrices(mtx1, mtx2):
    rows_mtx1 = len(mtx1)
    cols_mtx1 = len(mtx1[0])
    rows_mtx2 = len(mtx2)
    cols_mtx2 = len(mtx2[0])

    if cols_mtx1 != rows_mtx2:
        raise ValueError("Невозможно умножить матрицы: количество столбцов первой матрицы "
                         "должно совпадать с количеством строк второй матрицы.")

    result = [[0 for _ in range(cols_mtx2)] for _ in range(rows_mtx1)]

    for i in range(rows_mtx1):
        for j in range(cols_mtx2):
            result[i][j] = sum(mtx1[i][k] * mtx2[k][j] for k in range(cols_mtx1))

    return result