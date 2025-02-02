import tkinter as tk
from tkinter import ttk

class Workspace(ttk.Frame):
    def __init__(self, parent, scale_factor=10):
        super().__init__(parent, relief="groove")
        self.scale_factor = scale_factor  # Количество пикселей на одну единицу координат
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.create_workspace_widgets()

    def create_workspace_widgets(self):
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        """Обновляет размеры и перерисовывает сетку."""
        self.canvas.delete("all")
        self.draw_grid()

    def draw_grid(self):
        """Рисует координатную сетку 100x100 с центром в (0,0)."""
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        # Отображение сетки от -50 до 50
        for i in range(-50, 51):
            screen_x = center_x + i * self.scale_factor
            screen_y = center_y - i * self.scale_factor

            # Вертикальные линии
            self.canvas.create_line(screen_x, 0, screen_x, self.canvas_height, fill="lightgray")
            if i % 5 == 0:  # Подписи через 10 единиц
                self.canvas.create_text(screen_x + 5, center_y + 5, text=str(i), anchor="nw", font=("Arial", 8))

            # Горизонтальные линии
            self.canvas.create_line(0, screen_y, self.canvas_width, screen_y, fill="lightgray")
            if i % 5 == 0:
                self.canvas.create_text(center_x + 5, screen_y + 5, text=str(i), anchor="nw", font=("Arial", 8))

        # Оси
        self.canvas.create_line(0, center_y, self.canvas_width, center_y, fill="black", width=2)  # X-ось
        self.canvas.create_line(center_x, 0, center_x, self.canvas_height, fill="black", width=2)  # Y-ось

        # Подписи осей
        self.canvas.create_text(self.canvas_width - 15, center_y - 15, text="X", font=("Arial", 12, "bold"))
        self.canvas.create_text(center_x + 10, 10, text="Y", font=("Arial", 12, "bold"))
        self.canvas.create_text(center_x + 5, center_y + 5, text="(0,0)", font=("Arial", 10, "bold"), fill="red")

    def draw_points(self, points, color="blue"):
        """Рисует точки в координатной плоскости."""
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        for x, y in points:
            screen_x = center_x + x * self.scale_factor
            screen_y = center_y - y * self.scale_factor  # Инверсия Y
            self.canvas.create_oval(screen_x - 1, screen_y - 1, screen_x + 1, screen_y + 1, fill=color, outline=color)
