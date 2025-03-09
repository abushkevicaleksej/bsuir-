import tkinter as tk
from tkinter import ttk
import math


class Workspace(ttk.Frame):
    def __init__(self, parent, scale_factor=100):
        super().__init__(parent, relief="groove")
        self.scale_factor = scale_factor
        self.points = []
        self.on_point_moved = None
        self.selected_point = None
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.create_workspace_widgets()

    def set_callback(self, callback):
        self.on_point_moved = callback

    def create_workspace_widgets(self):
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.on_resize)

        self.canvas.bind("<ButtonPress-1>", self.on_point_press)
        self.canvas.bind("<B1-Motion>", self.on_point_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_point_release)

    def on_resize(self, event):
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_points(self.points)

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
        if not points:
            return
        self.points = points
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        centroid_x = sum(x for x, y in self.points) / len(self.points)
        centroid_y = sum(y for x, y in self.points) / len(self.points)

        def polar_angle(point):
            x, y = point
            return math.atan2(y - centroid_y, x - centroid_x)

        self.points = sorted(self.points, key=polar_angle)
        screen_points = []
        for x, y in self.points:
            screen_x = center_x + x * self.scale_factor
            screen_y = center_y - y * self.scale_factor
            screen_points.append((screen_x, screen_y))

            self.canvas.create_oval(
                screen_x - 5, screen_y - 5,
                screen_x + 5, screen_y + 5,
                fill=color, outline="black", tags="point"
            )

        for i in range(len(screen_points) - 1):
            x1, y1 = screen_points[i]
            x2, y2 = screen_points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill=color)

        if len(screen_points) > 2:
            x1, y1 = screen_points[-1]
            x2, y2 = screen_points[0]
            self.canvas.create_line(x1, y1, x2, y2, fill=color)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw_grid()

    def on_point_press(self, event):
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        print(self.points)
        for i, (x, y) in enumerate(self.points):
            screen_x = center_x + x * self.scale_factor
            screen_y = center_y - y * self.scale_factor
            if (event.x - screen_x) ** 2 + (event.y - screen_y) ** 2 <= 5 ** 2:
                print(f"Попал в точку {i}: ({x}, {y})")
                self.selected_point = i
                return
        print("Клик мимо точек")

    def on_point_move(self, event):
        print("мувчик")

        if self.selected_point is not None:
            print(f"Перемещение точки {self.selected_point}")
            center_x = self.canvas_width // 2
            center_y = self.canvas_height // 2

            new_x = (event.x - center_x) / self.scale_factor
            new_y = (center_y - event.y) / self.scale_factor
            self.points[self.selected_point] = (new_x, new_y)

            self.clear_canvas()
            self.draw_points(self.points)

        if self.on_point_moved is not None:
            self.on_point_moved(self.points)

    def on_point_release(self, event):
        print("Отпускание точки")

        self.selected_point = None