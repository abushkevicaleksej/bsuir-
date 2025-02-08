import tkinter as tk
from tkinter import *
from tkinter import ttk
from model.mode import Mode
from model.line import Line
from model.parametric_lines import ParametricCurveMode
from view.compile_circle_window import CompileCircleWindow
from view.compile_segment_window import CompileSegmentWindow
from view.compile_curve_window import CompileCurveWindow
from view.select_mode_window import SelectModeWindow
from view.select_line_window import SelectLineWindow
from view.select_curve_window import SelectCurveWindow


class Menu(ttk.Frame):
    def __init__(self, parent, workspace, table):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(fill=tk.X, expand=False)

        self.workspace = workspace
        self.table = table
        self.current_mode = Mode.none.value
        self.current_line = Line.none.value
        self.current_curve = ParametricCurveMode.none.value

        self.mode_label = ttk.Label(self, text=f'Текущий режим: {self.current_mode}')
        self.line_label = ttk.Label(self, text=f'Текущая линия второго порядка: {self.current_line}')
        self.curve_label = ttk.Label(self, text=f'Текущая параметрическая кривая: {self.current_curve}')

        self.create_widgets()

    def create_widgets(self):

        mode_button = ttk.Button(self, text='Выбрать режим', command=self.select_mode)
        line_button = ttk.Button(self, text='Линии второго порядка', command=self.select_line)
        curve_button = ttk.Button(self, text='Параметрические кривые', command=self.select_curve)
        compile_segment_button = ttk.Button(self, text='Построить отрезок', command=self.compile_segment)
        compile_circle_button = ttk.Button(self, text='Построить линию второго порядка', command=self.compile_line)
        compile_curve_button = ttk.Button(self, text='Построить параметрическую кривую', command=self.compile_curve)
        clear_button = ttk.Button(self, text = 'Очистить', command = self.clear_data)

        compile_segment_button.pack(side = LEFT, padx = 10, pady = 20)
        compile_circle_button.pack(side = LEFT, padx = 10, pady = 20)
        compile_curve_button.pack(side = LEFT, padx = 10, pady = 20)
        compile_circle_button.pack(side = LEFT, padx = 10, pady = 20)
        line_button.pack(side=LEFT, padx=10, pady=20)
        clear_button.pack(side = LEFT, padx = 10, pady = 20)
        curve_button.pack(side = LEFT, padx = 10, pady = 20)
        mode_button.pack(side = LEFT, padx = 10, pady = 20)
        self.mode_label.pack(side = LEFT, padx = 10, pady = 20)
        self.line_label.pack(side=LEFT, padx=10, pady=20)

    def select_mode(self):
        SelectModeWindow(self)

    def select_line(self):
        SelectLineWindow(self)

    def select_curve(self):
        SelectCurveWindow(self)

    def update_mode(self, new_mode):
        self.current_mode = new_mode
        self.mode_label.config(text=f'Текущий режим: {self.current_mode}')

    def update_line(self, new_line):
        self.current_line = new_line
        self.line_label.config(text=f'Текущая линия второго порядка: {self.current_line}')

    def update_curve(self, new_line):
        self.current_curve = new_line
        self.curve_label.config(text=f'Текущая параметрическая кривая: {self.current_curve}')

    def get_current_mode(self):
        print(f'current mode {self.current_mode}')
        return self.current_mode

    def get_current_line(self):
        print(f'current line {self.current_line}')
        return self.current_line

    def get_current_curve(self):
        print(f'current curve {self.current_curve}')
        return self.current_curve

    def compile_segment(self):
        CompileSegmentWindow(self)

    def compile_line(self):
        CompileCircleWindow(self)

    def compile_curve(self):
        CompileCurveWindow(self)

    def clear_data(self):
        self.table.clear_table()
        self.workspace.clear_canvas()

