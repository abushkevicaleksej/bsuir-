import tkinter as tk
from tkinter import *
from tkinter import ttk
from utils import center_window
from model.line_model.mode import Mode


class SelectModeWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()
        self.title("Выберите режим и задайте координаты.")
        self.geometry('250x200')
        center_window(self, 250, 200)
        self.menu = menu
        self.resizable(False, False)
        self.create_mode_widgets()
        self.grab_set()

    def create_mode_widgets(self):
        position = {"padx": 6, "pady": 6, "anchor": NW}
        mode = StringVar()
        header = ttk.Label(self, text='Доступные режимы:')

        cda_button = ttk.Radiobutton(self, text = Mode.cda.value, value = Mode.cda.value, variable=mode)
        brez_button = ttk.Radiobutton(self, text=Mode.brez.value, value=Mode.brez.value, variable=mode)
        wu_button = ttk.Radiobutton(self, text=Mode.wu.value, value=Mode.wu.value, variable=mode)

        apply_button = ttk.Button(self, text = 'Применить', command = lambda: self.apply_mode(mode.get()))

        header.pack(side = TOP)
        apply_button.pack(side=BOTTOM, pady = 30)
        cda_button.pack(**position)
        brez_button.pack(**position)
        wu_button.pack(**position)

    def apply_mode(self, selected_mode):
        self.menu.update_mode(selected_mode)
        self.destroy()
