import tkinter as tk
from view.canvas import DrawCanvas
from model.polygon import Polygon
from tkinter import messagebox
from utils import center_window

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Графический редактор: Построение полигонов")
        self.geometry("1280x720")
        center_window(self, 1280, 720)
        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.use_jarvis = tk.BooleanVar(value=False)
        self.use_graham = tk.BooleanVar(value=True)

        self.chk_jarvis = tk.Checkbutton(
            toolbar, text="Использовать метод Джарвиса",
            variable=self.use_jarvis, command=self.update_method_from_jarvis)
        self.chk_jarvis.pack(side=tk.LEFT, padx=2, pady=2)

        self.chk_graham = tk.Checkbutton(
            toolbar, text="Использовать метод Грэхема",
            variable=self.use_graham, command=self.update_method_from_graham)
        self.chk_graham.pack(side=tk.LEFT, padx=2, pady=2)

        btn_clear = tk.Button(toolbar, text="Очистить", command=self.clear_canvas)
        btn_clear.pack(side=tk.LEFT, padx=2, pady=2)

        btn_help = tk.Button(toolbar, text="Справка", command=self.show_help)
        btn_help.pack(side=tk.LEFT, padx=2, pady=2)

        self.canvas = DrawCanvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

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

    def show_help(self):
        help_text = (
            "Левая кнопка мыши: добавить вершину многоугольника.\n"
            "Shift + левая кнопка: задать точку для проверки принадлежности.\n"
            "Правая кнопка мыши: рисовать линии первого порядка.\n\n"
            "Выберите метод построения выпуклой оболочки:\n"
            "• 'Использовать метод Джарвиса' – оболочка по алгоритму Джарвиса.\n"
            "• 'Использовать метод Грэхема' – оболочка по алгоритму Грэхема.\n"
            "Внутренние нормали от сторон рисуются зелёной пунктирной линией,\n"
            "а точки пересечения линий с многоугольником – фиолетовыми кругами."
        )
        messagebox.showinfo("Справка", help_text)