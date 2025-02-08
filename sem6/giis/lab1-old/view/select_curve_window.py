import tkinter as tk
from tkinter import *
from tkinter import ttk
from view.center_window import center_window
from model.parametric_lines import ParametricCurveMode


class SelectCurveWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()
        self.title("Выберите кривую и задайте координаты.")
        self.geometry('250x300')
        center_window(self, 250, 300)
        self.menu = menu
        self.resizable(False, False)
        self.create_curve_widgets()
        self.grab_set()

    def create_curve_widgets(self):
        position = {"padx": 6, "pady": 6, "anchor": NW}
        curve = StringVar()
        header = ttk.Label(self, text='Доступные кривые:')

        erm_button = ttk.Radiobutton(self, text = ParametricCurveMode.erm.value, value = ParametricCurveMode.erm.value, variable=curve)
        bez_button = ttk.Radiobutton(self, text = ParametricCurveMode.bez.value, value = ParametricCurveMode.bez.value, variable=curve)
        b_button = ttk.Radiobutton(self, text=ParametricCurveMode.b_spline.value, value=ParametricCurveMode.b_spline.value, variable=curve)
        apply_button = ttk.Button(self, text = 'Применить', command = lambda: self.apply_curve(curve.get()))

        header.pack(side = TOP)
        apply_button.pack(side=BOTTOM, pady = 30)
        erm_button.pack(**position)
        bez_button.pack(**position)
        b_button.pack(**position)

    def apply_curve(self, selected_curve):
        self.menu.update_curve(selected_curve)
        self.destroy()
