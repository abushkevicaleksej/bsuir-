import tkinter as tk
from tkinter import *
from tkinter import ttk
from view.center_window import center_window
from model.line import Line, SecondOrderLine


class CompileCircleWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()
        self.title("Построение линии второго порядка.")
        self.geometry('270x270')
        self.menu = menu
        center_window(self, 270, 270)
        self.resizable(False, False)
        self.set_coords_widgets()
        self.grab_set()

    def set_coords_widgets(self):
        header = ttk.Label(self, text='Укажите параметры:')
        header.grid(row=0, columnspan=2, pady=10)

        ttk.Label(self, text='x:').grid(row=1, column=0, padx=5, pady=5)
        self.x_entry = ttk.Entry(self, width=5)
        self.x_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text='y:').grid(row=2, column=0, padx=5, pady=5)
        self.y_entry = ttk.Entry(self, width=5)
        self.y_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text='a:').grid(row=3, column=0, padx=5, pady=5)
        self.a_entry = ttk.Entry(self, width=5)
        self.a_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text='b:').grid(row=4, column=0, padx=5, pady=5)
        self.b_entry = ttk.Entry(self, width=5)
        self.b_entry.grid(row=4, column=1, padx=5, pady=5)

        apply_button = ttk.Button(self, text='Применить', command=self.compile)
        apply_button.grid(row=5, columnspan=2, pady=30)

    def compile(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
        except ValueError:
            print("Ошибка: Все параметры должны быть целыми числами.")
            return

        if self.menu.current_line == Line.circle.value:
            circle = SecondOrderLine(Line.circle, self.menu.workspace, self.menu.table, x, y, a, b)
            circle.draw()
        elif self.menu.current_line == Line.ell.value:
            ellipse = SecondOrderLine(Line.ell, self.menu.workspace, self.menu.table, x, y, a, b)
            ellipse.draw()
        elif self.menu.current_line == Line.par.value:
            parabola = SecondOrderLine(Line.par, self.menu.workspace, self.menu.table, x, y, a, b)
            parabola.draw()
        elif self.menu.current_line == Line.hyp.value:
            hyperbola = SecondOrderLine(Line.hyp, self.menu.workspace, self.menu.table, x, y, a, b)
            hyperbola.draw()
        else:
            print("Ошибка: Неизвестный тип линии.")

        self.destroy()
