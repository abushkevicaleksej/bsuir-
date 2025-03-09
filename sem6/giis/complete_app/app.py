import tkinter as tk
from tkinter import ttk
from view.line_view.app import LineAppWindow
from view.fig_view.menu import FigureAppWindow
from view.other_view.main_window import OtherAppWindow
from view.polygon_view.main_window import PolygonAppWindow
from utils import center_window

class CompleteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GIIS Complete App")
        self.geometry('1280x720')
        self.resizable(False, False)
        center_window(self, 1280, 720)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        line_frame = tk.Frame(self.notebook)
        fig_frame = tk.Frame(self.notebook)
        polygons_frame = tk.Frame(self.notebook)
        other_frame = tk.Frame(self.notebook)

        self.line_entry = LineAppWindow(line_frame)
        self.fig_entry = FigureAppWindow(fig_frame)
        self.polygons_entry = PolygonAppWindow(polygons_frame)
        self.other_entry = OtherAppWindow(other_frame)

        self.notebook.add(line_frame, text="Линии первого, второго порядка. Кривые")
        self.notebook.add(fig_frame, text="Функционал для работы с 3D")
        self.notebook.add(polygons_frame, text="Полигоны")
        self.notebook.add(other_frame, text="Триангуляция Делоне и диаграмма Вороного.")

        self.mainloop()