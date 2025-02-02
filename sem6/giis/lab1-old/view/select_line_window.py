import tkinter as tk
from tkinter import *
from tkinter import ttk
from view.center_window import center_window
from model.mode import Mode
from model.line import Line


class SelectLineWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()
        self.title("Выберите линию и задайте координаты.")
        self.geometry('250x300')
        center_window(self, 250, 300)
        self.menu = menu
        self.resizable(False, False)
        self.create_line_widgets()
        self.grab_set()

    def create_line_widgets(self):
        position = {"padx": 6, "pady": 6, "anchor": NW}
        line = StringVar()
        header = ttk.Label(self, text='Доступные линии:')

        circle_button = ttk.Radiobutton(self, text = Line.circle.value, value = Line.circle.value, variable=line)
        ell_button = ttk.Radiobutton(self, text = Line.ell.value, value = Line.ell.value, variable=line)
        hyp_button = ttk.Radiobutton(self, text=Line.hyp.value, value=Line.hyp.value, variable=line)
        par_button = ttk.Radiobutton(self, text=Line.par.value, value=Line.par.value, variable=line)

        apply_button = ttk.Button(self, text = 'Применить', command = lambda: self.apply_mode(line.get()))

        header.pack(side = TOP)
        apply_button.pack(side=BOTTOM, pady = 30)
        circle_button.pack(**position)
        ell_button.pack(**position)
        hyp_button.pack(**position)
        par_button.pack(**position)

    def apply_mode(self, selected_line):
        self.menu.update_line(selected_line)
        self.destroy()
