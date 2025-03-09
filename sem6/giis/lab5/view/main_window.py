import tkinter as tk
from view.canvas import DrawCanvas
from model.polygon import Polygon
from model.fill_algorythm import FillAlgorithms
from tkinter import messagebox, scrolledtext
from utils import center_window

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Графический редактор: Построение полигонов")
        self.geometry("1280x720")
        center_window(self, 1280, 720)
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(container, bd=2, relief=tk.SUNKEN)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas = DrawCanvas(self.left_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(container, width=300)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        ctrl_frame = tk.Frame(self.right_frame, bd=2, relief=tk.RIDGE, padx=5, pady=5)
        ctrl_frame.pack(fill=tk.X, padx=5, pady=5)
        self.use_jarvis = tk.BooleanVar(value=False)
        self.use_graham = tk.BooleanVar(value=True)
        self.chk_jarvis = tk.Checkbutton(ctrl_frame, text="Использовать метод Джарвиса",
                                         variable=self.use_jarvis, command=self.update_method_from_jarvis)
        self.chk_jarvis.pack(anchor="w", pady=2)
        self.chk_graham = tk.Checkbutton(ctrl_frame, text="Использовать метод Грэхема",
                                         variable=self.use_graham, command=self.update_method_from_graham)
        self.chk_graham.pack(anchor="w", pady=2)
        btn_clear = tk.Button(ctrl_frame, text="Очистить", command=self.clear_canvas)
        btn_clear.pack(fill=tk.X, pady=2)
        btn_help = tk.Button(ctrl_frame, text="Справка", command=self.show_help)
        btn_help.pack(fill=tk.X, pady=2)
        algo_frame = tk.Frame(ctrl_frame, bd=1, relief=tk.GROOVE, padx=5, pady=5)
        algo_frame.pack(fill=tk.X, pady=5)
        tk.Label(algo_frame, text="Алгоритм заполнения:").pack(anchor="w")
        self.algo_choice = tk.StringVar(value="ordered")
        tk.Radiobutton(algo_frame, text="Растровая развертка (упорядоченный список ребер)",
                       variable=self.algo_choice, value="ordered").pack(anchor="w")
        tk.Radiobutton(algo_frame, text="Растровая развертка (активный список ребер)",
                       variable=self.algo_choice, value="active").pack(anchor="w")
        tk.Radiobutton(algo_frame, text="Простой алгоритм заполнения с затравкой",
                       variable=self.algo_choice, value="seed_simple").pack(anchor="w")
        tk.Radiobutton(algo_frame, text="Построчный алгоритм заполнения с затравкой",
                       variable=self.algo_choice, value="seed_scanline").pack(anchor="w")
        btn_fill = tk.Button(ctrl_frame, text="Запустить заливку", command=self.run_fill_algorithm)
        btn_fill.pack(fill=tk.X, pady=2)

        self.debug_text = scrolledtext.ScrolledText(self.right_frame, width=40, height=20)
        self.debug_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def update_method_from_jarvis(self):
        if self.use_jarvis.get():
            self.use_graham.set(False)
            self.canvas.hull_method = "jarvis"
        else:
            self.use_graham.set(True)
            self.canvas.hull_method = "graham"
        self.canvas.redraw()

    def update_method_from_graham(self):
        if self.use_graham.get():
            self.use_jarvis.set(False)
            self.canvas.hull_method = "graham"
        else:
            self.use_jarvis.set(True)
            self.canvas.hull_method = "jarvis"
        self.canvas.redraw()

    def clear_canvas(self):
        self.canvas.current_polygon = Polygon()
        self.canvas.draw_lines = []
        self.canvas.test_point = None
        self.canvas.redraw()
        self.debug_text.delete("1.0", tk.END)

    def show_help(self):
        help_text = (
            "Левая кнопка мыши: добавить вершину многоугольника.\n"
            "Shift + левая кнопка: задать точку для проверки принадлежности.\n"
            "Правая кнопка мыши: рисовать линии.\n\n"
            "Панель управления (правая часть):\n"
            "  - Выбор метода построения выпуклой оболочки (Checkbutton).\n"
            "  - Выбор алгоритма заполнения (RadioButton).\n"
            "  - Кнопки: Очистить, Справка, Запустить заливку.\n\n"
            "Отладочная информация выводится ниже."
        )
        messagebox.showinfo("Справка", help_text)

    def run_fill_algorithm(self):
        self.debug_text.delete("1.0", tk.END)
        choice = self.algo_choice.get()
        steps = []
        if choice == "ordered":
            steps = FillAlgorithms.fill_ordered_edge_list(self.canvas.current_polygon, self.canvas)
        elif choice == "active":
            steps = FillAlgorithms.fill_active_edge_table(self.canvas.current_polygon, self.canvas)
        elif choice == "seed_simple":
            steps = FillAlgorithms.simple_seed_fill(self.canvas.current_polygon, self.canvas)
        elif choice == "seed_scanline":
            steps = FillAlgorithms.scanline_seed_fill(self.canvas.current_polygon, self.canvas)
        for step in steps:
            self.debug_text.insert(tk.END, step + "\n")
        self.canvas.redraw()