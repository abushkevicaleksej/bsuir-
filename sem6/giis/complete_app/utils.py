import math

def line_intersection(p1, p2, p3, p4):
    """Находит точку пересечения отрезков p1-p2 и p3-p4, если оно существует.
       p1, p2, p3, p4 – кортежи (x, y). Возвращает (точка, True) или (None, False)"""
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1
    if abs(determinant) < 1e-10:
        return None, False

    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    intersection = (x, y)

    def on_segment(p, q, r):
        return (min(p[0], r[0]) - 1e-10 <= q[0] <= max(p[0], r[0]) + 1e-10 and
                min(p[1], r[1]) - 1e-10 <= q[1] <= max(p[1], r[1]) + 1e-10)

    if on_segment(p1, intersection, p2) and on_segment(p3, intersection, p4):
        return intersection, True
    return None, False

def center_window(window, w, h):
    ws, hs = window.winfo_screenwidth(), window.winfo_screenheight()  # dimensions of screen
    x, y = (ws / 2) - (w / 2), (hs / 2) - (h / 2)  # calculate center

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def circumcircle(triangle):
    # triangle: [(x1,y1), (x2,y2), (x3,y3)]
    (x1, y1), (x2, y2), (x3, y3) = triangle
    d = 2 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    if d == 0:
        return None  # точки коллинеарны
    ux = ((x1**2+y1**2)*(y2-y3) + (x2**2+y2**2)*(y3-y1) + (x3**2+y3**2)*(y1-y2)) / d
    uy = ((x1**2+y1**2)*(x3-x2) + (x2**2+y2**2)*(x1-x3) + (x3**2+y3**2)*(x2-x1)) / d
    center = (ux, uy)
    radius = distance(center, (x1, y1))
    return center, radius