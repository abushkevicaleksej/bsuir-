import tkinter as tk
from tkinter import *
from tkinter import ttk
from model.mode import Mode
from view.select_mode_window import SelectModeWindow
from view.compile_window import CompileWindow

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(fill=X, expand=False)
        self.current_mode = Mode.none.value
        self.label = ttk.Label(self, text=f'Текущий режим: {self.current_mode}')
        self.create_widgets()

    def create_widgets(self):
        mode_button = ttk.Button(self, text='Выбрать режим', command=self.select_mode)
        grid_button = ttk.Button(self, text='Включить сетку')
        compile_button = ttk.Button(self, text = 'Построить', command=self.compile)
        clear_button = ttk.Button(self, text = 'Очистить')

        compile_button.pack(side = LEFT, padx = 10, pady = 20)
        clear_button.pack(side = LEFT, padx = 10, pady = 20)
        mode_button.pack(side = LEFT, padx = 10, pady = 20)
        grid_button.pack(side = LEFT, padx = 10, pady = 20)
        self.label.pack(side = LEFT, padx = 10, pady = 20)

    def select_mode(self):
        SelectModeWindow(self)

    def update_mode(self, new_mode):
        self.current_mode = new_mode
        self.label.config(text=f'Текущий режим: {self.current_mode}')

    def get_current_mode(self):
        print(f'current mode {self.current_mode}')
        return self.current_mode

    def compile(self):
        CompileWindow(self)
