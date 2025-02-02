import tkinter as tk
from tkinter import *
from tkinter import ttk
from model.mode import Mode
from model.line import Line
from view.compile_circle_window import CompileCircleWindow
from view.compile_segment_window import CompileSegmentWindow
from view.select_mode_window import SelectModeWindow
from view.select_line_window import SelectLineWindow


class Menu(ttk.Frame):
    def __init__(self, parent, workspace, table):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(fill=tk.X, expand=False)

        self.workspace = workspace  # Store workspace reference
        self.table = table
        self.current_mode = Mode.none.value
        self.current_line = Line.none.value

        self.mode_label = ttk.Label(self, text=f'Текущий режим: {self.current_mode}')
        self.line_label = ttk.Label(self, text=f'Текущая линия второго порядка: {self.current_line}')

        self.create_widgets()

    def create_widgets(self):
        compile_segment_button = ttk.Button(self, text='Построить отрезок', command=self.compile_segment)
        mode_button = ttk.Button(self, text='Выбрать режим', command=self.select_mode)
        line_button = ttk.Button(self, text='Линии второго порядка', command=self.select_line)
        compile_circle_button = ttk.Button(self, text='Построить линию второго порядка', command=self.compile_line)
        clear_button = ttk.Button(self, text = 'Очистить')

        compile_segment_button.pack(side = LEFT, padx = 10, pady = 20)
        compile_circle_button.pack(side = LEFT, padx = 10, pady = 20)
        line_button.pack(side=LEFT, padx=10, pady=20)
        clear_button.pack(side = LEFT, padx = 10, pady = 20)
        mode_button.pack(side = LEFT, padx = 10, pady = 20)
        self.mode_label.pack(side = LEFT, padx = 10, pady = 20)
        self.line_label.pack(side=LEFT, padx=10, pady=20)

    def select_mode(self):
        SelectModeWindow(self)

    def select_line(self):
        SelectLineWindow(self)

    def update_mode(self, new_mode):
        self.current_mode = new_mode
        self.mode_label.config(text=f'Текущий режим: {self.current_mode}')

    def update_line(self, new_line):
        self.current_line = new_line
        self.line_label.config(text=f'Текущая линия второго порядка: {self.current_line}')

    def get_current_mode(self):
        print(f'current mode {self.current_mode}')
        return self.current_mode

    def get_current_line(self):
        print(f'current line {self.current_line}')
        return self.current_line

    def compile_segment(self):
        CompileSegmentWindow(self)

    def compile_line(self):
        CompileCircleWindow(self)
