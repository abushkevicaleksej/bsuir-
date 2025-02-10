import tkinter as tk
from tkinter import *
from tkinter import ttk

from model.parametric_lines import ParametricCurve, ParametricCurveMode
from view.center_window import center_window
from model.line import Line, SecondOrderLine


class CompileCurveWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()
        self.title("Построение параметрической кривой.")
        self.geometry('500x500')
        self.menu = menu
        center_window(self, 500, 500)
        self.resizable(False, False)
        self.set_params_widgets()
        self.grab_set()

    def set_params_widgets(self):
        header = ttk.Label(self, text='Укажите параметры:')
        header.grid(row=0, columnspan=2, pady=10)

        # Поля для P1, P2, P3, P4
        ttk.Label(self, text='P1:').grid(row=1, column=0, padx=5, pady=5)
        self.p1_entry = ttk.Entry(self, width=5)
        self.p1_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text='P2:').grid(row=2, column=0, padx=5, pady=5)
        self.p2_entry = ttk.Entry(self, width=5)
        self.p2_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text='P3:').grid(row=3, column=0, padx=5, pady=5)
        self.p3_entry = ttk.Entry(self, width=5)
        self.p3_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text='P4:').grid(row=4, column=0, padx=5, pady=5)
        self.p4_entry = ttk.Entry(self, width=5)
        self.p4_entry.grid(row=4, column=1, padx=5, pady=5)

        # Поля для R1 и R2
        ttk.Label(self, text='R1:').grid(row=5, column=0, padx=5, pady=5)  # Изменено на 5
        self.r1_entry = ttk.Entry(self, width=5)
        self.r1_entry.grid(row=5, column=1, padx=5, pady=5)  # Изменено на 5

        ttk.Label(self, text='R2:').grid(row=6, column=0, padx=5, pady=5)  # Изменено на 6
        self.r2_entry = ttk.Entry(self, width=5)
        self.r2_entry.grid(row=6, column=1, padx=5, pady=5)  # Изменено на 6

        apply_button = ttk.Button(self, text='Применить', command=self.compile)
        apply_button.grid(row=7, columnspan=2, pady=30)

    def compile(self):
        try:
            p1 = list(map(int, self.p1_entry.get().split()))
            p2 = list(map(int, self.p2_entry.get().split()))
            p3 = list(map(int, self.p3_entry.get().split()))
            p4 = list(map(int, self.p4_entry.get().split()))
            r1 = list(map(int, self.r1_entry.get().split()))
            r2 = list(map(int, self.r2_entry.get().split()))
        except ValueError:
            print("Ошибка: Все параметры должны быть целыми числами.")
            return

        if self.menu.current_curve == ParametricCurveMode.erm.value:
            erm = ParametricCurve(ParametricCurveMode.erm, self.menu.workspace, self.menu.table, p1, p2, p3, p4, r1, r2)
            erm.draw()
        elif self.menu.current_curve == ParametricCurveMode.bez.value:
            bez = ParametricCurve(ParametricCurveMode.bez, self.menu.workspace, self.menu.table, p1, p2, p3, p4, r1, r2)
            bez.draw()
        elif self.menu.current_curve == ParametricCurveMode.b_spline.value:
            b_spline = ParametricCurve(ParametricCurveMode.b_spline, self.menu.workspace, self.menu.table, p1, p2, p3, p4, r1, r2)
            b_spline.draw()
        else:
            print("Ошибка: Неизвестный тип линии.")
        self.destroy()
