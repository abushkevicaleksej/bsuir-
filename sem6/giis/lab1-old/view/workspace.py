import tkinter as tk
from tkinter import ttk


class Workspace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        self.create_workspace_widgets()

    def create_workspace_widgets(self):
        self.canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.draw_grid()

    def draw_grid(self):
        step = 50
        width = 500
        height = 500

        for x in range(0, width, step):
            self.canvas.create_line(x, 0, x, height, fill="lightgray")
            self.canvas.create_text(x + 5, 10, text=str(x), anchor="nw", font=("Arial", 8))

        for y in range(0, height, step):
            self.canvas.create_line(0, y, width, y, fill="lightgray")
            self.canvas.create_text(5, y + 5, text=str(y), anchor="nw", font=("Arial", 8))

        self.canvas.create_line(0, height // 2, width, height // 2, fill="black", width=2)
        self.canvas.create_line(width // 2, 0, width // 2, height, fill="black", width=2)

        self.canvas.create_text(width - 10, height // 2 - 10, text="X", font=("Arial", 12, "bold"))
        self.canvas.create_text(width // 2 + 10, 10, text="Y", font=("Arial", 12, "bold"))

        self.canvas.create_text(width // 2 + 5, height // 2 + 5, text="(0,0)", font=("Arial", 10, "bold"), fill="red")
