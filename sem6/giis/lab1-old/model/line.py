import enum
from view.workspace import Workspace
from view.table import Table

class Line(enum.Enum):
    none = "Не выбрано"
    circle = "окружность"
    ell = "эллипс"
    hyp = "гипербола"
    par = "парабола"

class SecondOrderLine:
    def __init__(self, line_type: Line, workspace: Workspace, table: Table, x: int, y: int, a: int, b: int):
        self.line_type = line_type
        self.workspace = workspace
        self.table = table
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def draw(self):
        if self.line_type == Line.circle:
            points = self._bresenham_circle()
        elif self.line_type == Line.ell:
            points = self._bresenham_ellipse()
        elif self.line_type == Line.hyp:
            points = self._bresenham_hyperbola()
        elif self.line_type == Line.par:
            points = self._bresenham_parabola()
        else:
            raise ValueError(f"Unsupported line type: {self.line_type}")

        self.table.update_table(points)
        self.workspace.draw_points(points)

    def _bresenham_circle(self):
        """Bresenham's algorithm for drawing a circle with radius self.b."""
        r = self.y
        x, y = 0, r
        d = 3 - 2 * r
        points = []

        while x <= y:
            points += [(x, y), (-x, y), (x, -y), (-x, -y),
                       (y, x), (-y, x), (y, -x), (-y, -x)]
            if d < 0:
                d += 4 * x + 6
            else:
                d += 4 * (x - y) + 10
                y -= 1
            x += 1
        return points

    def _bresenham_ellipse(self):
        """Bresenham's algorithm for drawing an ellipse centered at (0,0)."""
        a, b = self.a, self.b
        x, y = 0, b
        d = b ** 2 - a ** 2 * b + (a ** 2) // 4
        points = []

        while b ** 2 * x <= a ** 2 * y:
            points += [(x, y), (-x, y), (x, -y), (-x, -y)]  # Centered at (0,0)
            if d < 0:
                d += 2 * b ** 2 * x + 3 * b ** 2
            else:
                d += 2 * b ** 2 * x - 2 * a ** 2 * y + 2 * a ** 2 + 3 * b ** 2
                y -= 1
            x += 1

        d = b ** 2 * (x + 0.5) ** 2 + a ** 2 * (y - 1) ** 2 - a ** 2 * b ** 2
        while y >= 0:
            points += [(x, y), (-x, y), (x, -y), (-x, -y)]  # Centered at (0,0)
            if d > 0:
                d += -2 * a ** 2 * y + 3 * a ** 2
            else:
                d += 2 * b ** 2 * x - 2 * a ** 2 * y + 2 * b ** 2 + 3 * a ** 2
                x += 1
            y -= 1
        return points

    def _bresenham_hyperbola(self):
        """Bresenham’s algorithm for drawing a hyperbola centered at (0,0)."""
        a, b = self.a, self.b
        x, y = a, 0
        d = a ** 2 - 2 * a * b ** 2 + b ** 2
        points = []

        while x * b ** 2 >= y * a ** 2:
            points += [(x, y), (-x, y), (x, -y), (-x, -y)]  # Centered at (0,0)
            if d < 0:
                d += 2 * a ** 2 * y + 3 * a ** 2
            else:
                d += -2 * b ** 2 * x + 2 * a ** 2 * y + 3 * a ** 2
                x += 1
            y += 1
        return points

    def _bresenham_parabola(self):
        """Bresenham’s algorithm for drawing a parabola (y^2 = 4ax), centered at (0,0)."""
        x, y = 0, 0
        d = 1 - self.a
        points = []

        while x <= self.a:
            points += [(x, y), (x, -y)]
            if d < 0:
                d += 2 * y + 3
            else:
                d += 2 * (y - x) + 5
                x += 1
            y += 1
        return points
