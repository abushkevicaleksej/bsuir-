import tkinter as tk
from tkinter import *
from tkinter import ttk
from view.center_window import center_window
from model.mode import Mode

class CompileSegmentWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()
        self.title("Построение отрезка.")
        self.geometry('270x270')
        self.menu = menu
        center_window(self, 270, 270)
        self.resizable(False, False)
        self.set_coords_widgets()
        self.grab_set()

    def set_coords_widgets(self):
        header = ttk.Label(self, text='Укажите координаты начала и конца отрезка:')
        header.grid(row=0, columnspan=2, pady=10)

        ttk.Label(self, text='x1:').grid(row=1, column=0, padx=5, pady=5)
        x_1 = ttk.Entry(self, width=5)
        x_1.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text='y1:').grid(row=2, column=0, padx=5, pady=5)
        y_1 = ttk.Entry(self, width=5)
        y_1.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text='x2:').grid(row=3, column=0, padx=5, pady=5)
        x_2 = ttk.Entry(self, width=5)
        x_2.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text='y2:').grid(row=4, column=0, padx=5, pady=5)
        y_2 = ttk.Entry(self, width=5)
        y_2.grid(row=4, column=1, padx=5, pady=5)
        apply_button = ttk.Button(self, text='Применить', command=lambda: self.compile({
            'x1': x_1.get(),
            'y1': y_1.get(),
            'x2': x_2.get(),
            'y2': y_2.get()
        }))
        apply_button.grid(row=5, columnspan=2, pady=30)

    def compile(self, coords):
        if self.menu.current_mode == "ЦДА":
            print("раз")

        if self.menu.current_mode == "Метод Брезенхема":
            print("два")
        if self.menu.current_mode == "Метод Ву":
            print("три")
        self.destroy()