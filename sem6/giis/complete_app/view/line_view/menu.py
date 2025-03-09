import tkinter as tk
from tkinter import *
from tkinter import ttk
from model.line_model.mode import Mode
from model.line_model.line import Line
from model.line_model.parametric_lines import ParametricCurveMode
from view.line_view.compile_circle_window import CompileCircleWindow
from view.line_view.compile_segment_window import CompileSegmentWindow
from view.line_view.compile_curve_window import CompileCurveWindow
from view.line_view.select_mode_window import SelectModeWindow
from view.line_view.select_line_window import SelectLineWindow
from view.line_view.select_curve_window import SelectCurveWindow


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
        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Первый ряд кнопок
        mode_button = ttk.Button(frame, text='Выбрать режим', command=self.select_mode)
        line_button = ttk.Button(frame, text='Линии второго порядка', command=self.select_line)
        curve_button = ttk.Button(frame, text='Параметрические кривые', command=self.select_curve)
        clear_button = ttk.Button(frame, text='Очистить', command=self.clear_data)

        mode_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        line_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        curve_button.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        clear_button.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        # Второй ряд кнопок
        compile_segment_button = ttk.Button(frame, text='Построить отрезок', command=self.compile_segment)
        compile_circle_button = ttk.Button(frame, text='Построить линию второго порядка', command=self.compile_line)
        compile_curve_button = ttk.Button(frame, text='Построить параметрическую кривую', command=self.compile_curve)

        compile_segment_button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        compile_circle_button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        compile_curve_button.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        # Метки внизу
        label_frame = ttk.Frame(self)
        label_frame.pack(pady=10, fill=X)

        self.mode_label.pack(side=LEFT, padx=10)
        self.line_label.pack(side=LEFT, padx=10)
        self.curve_label.pack(side=LEFT, padx=10)

        # Равномерное распределение колонок
        for i in range(4):
            frame.columnconfigure(i, weight=1)

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

