import tkinter as tk
from tkinter import ttk
import math

class Workspace(ttk.Frame):
    def __init__(self, parent, scale_factor=50):
        super().__init__(parent, relief="groove")
        self.scale_factor = scale_factor
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.create_workspace_widgets()

    def create_workspace_widgets(self):
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.canvas.delete("all")
        self.draw_grid()

    def draw_grid(self):
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        for i in range(-50, 51):
            screen_x = center_x + i * self.scale_factor
            screen_y = center_y - i * self.scale_factor

            self.canvas.create_line(screen_x, 0, screen_x, self.canvas_height, fill="lightgray")
            if i % 1 == 0:
                self.canvas.create_text(screen_x + 5, center_y + 5, text=str(i), anchor="nw", font=("Arial", 8))

            self.canvas.create_line(0, screen_y, self.canvas_width, screen_y, fill="lightgray")
            if i % 1 == 0:
                self.canvas.create_text(center_x + 5, screen_y + 5, text=str(i), anchor="nw", font=("Arial", 8))

        self.canvas.create_line(0, center_y, self.canvas_width, center_y, fill="black", width=2)  # X-ось
        self.canvas.create_line(center_x, 0, center_x, self.canvas_height, fill="black", width=2)  # Y-ось

        self.canvas.create_text(self.canvas_width - 15, center_y - 15, text="X", font=("Arial", 12, "bold"))
        self.canvas.create_text(center_x + 10, 10, text="Y", font=("Arial", 12, "bold"))
        self.canvas.create_text(center_x + 5, center_y + 5, text="(0,0)", font=("Arial", 10, "bold"), fill="red")

    def draw_points(self, points, color="blue"):
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        # Вычисляем центр масс всех точек
        centroid_x = sum(x for x, y in points) / len(points)
        centroid_y = sum(y for x, y in points) / len(points)

        # Сортируем точки по углу относительно центра масс
        def polar_angle(point):
            x, y = point
            return math.atan2(y - centroid_y, x - centroid_x)

        points = sorted(points, key=polar_angle)

        # Преобразуем координаты точек для отображения на экране
        screen_points = []
        for x, y in points:
            screen_x = center_x + x * self.scale_factor
            screen_y = center_y - y * self.scale_factor
            screen_points.append((screen_x, screen_y))

            # Рисуем сами точки
            self.canvas.create_oval(
                screen_x - 2, screen_y - 2,
                screen_x + 2, screen_y + 2,
                fill=color, outline=color
            )

        # Соединяем точки в порядке их следования
        for i in range(len(screen_points) - 1):
            x1, y1 = screen_points[i]
            x2, y2 = screen_points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill=color)

        # Замыкаем контур, если больше двух точек
        if len(screen_points) > 2:
            x1, y1 = screen_points[-1]
            x2, y2 = screen_points[0]
            self.canvas.create_line(x1, y1, x2, y2, fill=color)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw_grid()
