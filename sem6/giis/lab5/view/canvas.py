import tkinter as tk
from model.polygon import Polygon
from model.builder import ConvexHullBuilder
from utils import line_intersection


class DrawCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.current_polygon = Polygon()
        self.draw_lines = []  # Список линий, каждая линия представлена парой точек ((x1, y1), (x2, y2))
        self.temp_line = None  # Временная линия при рисовании правой кнопкой мыши
        self.test_point = None  # Точка для проверки принадлежности
        self.hull_method = "graham"  # Метод по умолчанию
        self.bind("<Button-1>", self.on_left_click)
        self.bind("<Shift-Button-1>", self.on_shift_left_click)
        self.bind("<ButtonPress-3>", self.on_right_press)
        self.bind("<ButtonRelease-3>", self.on_right_release)

    def on_left_click(self, event):
        # Добавляем вершину многоугольника
        self.current_polygon.add_point((event.x, event.y))
        self.redraw()

    def on_shift_left_click(self, event):
        # Задаём точку для проверки принадлежности
        self.test_point = (event.x, event.y)
        self.redraw()

    def on_right_press(self, event):
        # Начало рисования произвольной линии
        self.temp_line = (event.x, event.y)

    def on_right_release(self, event):
        if self.temp_line:
            line = (self.temp_line, (event.x, event.y))
            self.draw_lines.append(line)
            self.temp_line = None
            self.redraw()

    def redraw(self):
        self.delete("all")
        points = self.current_polygon.points

        # Отрисовка многоугольника
        if points:
            # Рисуем линии между точками
            for i in range(1, len(points)):
                self.create_line(points[i-1][0], points[i-1][1],
                                 points[i][0], points[i][1],
                                 width=2, fill="black")
            if len(points) > 2:
                # Замыкаем многоугольник
                self.create_line(points[-1][0], points[-1][1],
                                 points[0][0], points[0][1],
                                 width=2, fill="black")
            # Выводим текст о выпуклости
            convex = self.current_polygon.is_convex()
            text = "Полигон выпуклый" if convex else "Полигон не выпуклый"
            self.create_text(10, 10, anchor="nw", text=text, fill="black", font=("Arial", 12))

            # Отрисовка внутренних нормалей
            normals = self.current_polygon.inner_normals()
            for i, normal in enumerate(normals):
                p1 = points[i]
                p2 = points[(i + 1) % len(points)]
                midx = (p1[0] + p2[0]) / 2
                midy = (p1[1] + p2[1]) / 2
                scale = 20
                endx = midx + normal[0] * scale
                endy = midy + normal[1] * scale
                self.create_line(midx, midy, endx, endy, fill="green", dash=(4, 2), width=2)

            # Построение и отрисовка выпуклой оболочки, если вершин 3 и больше
            if len(points) >= 3:
                if self.hull_method == "graham":
                    hull = ConvexHullBuilder.graham_scan(points)
                else:
                    hull = ConvexHullBuilder.jarvis_march(points)
                if hull:
                    for i in range(len(hull)):
                        p_start = hull[i]
                        p_end = hull[(i + 1) % len(hull)]
                        self.create_line(p_start[0], p_start[1],
                                         p_end[0], p_end[1],
                                         fill="red", width=2)

        # Отрисовка линий первого порядка и проверка пересечений с многоугольником
        for line in self.draw_lines:
            (x1, y1), (x2, y2) = line
            self.create_line(x1, y1, x2, y2, fill="blue", width=2)
            for edge in self.current_polygon.edges():
                inter, found = line_intersection(line[0], line[1], edge[0], edge[1])
                if found:
                    ix, iy = inter
                    self.create_oval(ix-3, iy-3, ix+3, iy+3, fill="magenta")

        # Отрисовка временной линии, если она есть
        if self.temp_line:
            self.create_line(self.temp_line[0], self.temp_line[1],
                             self.winfo_pointerx() - self.winfo_rootx(),
                             self.winfo_pointery() - self.winfo_rooty(),
                             fill="blue", width=2)

        # Отрисовка тестовой точки и проверка принадлежности многоугольнику
        if self.test_point:
            x, y = self.test_point
            self.create_oval(x-3, y-3, x+3, y+3, fill="dark cyan")
            inside = self.current_polygon.contains_point(self.test_point)
            txt = "Внутри" if inside else "Снаружи"
            self.create_text(x + 10, y, text=txt, anchor="w", fill="black", font=("Arial", 12))