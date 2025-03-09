from view.workspace import Workspace
import tkinter as tk
from tkinter import ttk
from model.point import Point
from model.shape import Shape
import numpy as np

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = ttk.Frame(self, relief="groove", borderwidth=1)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        self.workspace = Workspace(self)
        self.menu_bar = tk.Menu(parent)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.focus_set()
        parent.bind("<Key>", self.key_handler)
        parent.bind("<KeyPress-a>", self.move_shape_x_plus)
        parent.bind("<KeyPress-z>", self.move_shape_x_minus)
        parent.bind("<KeyPress-s>", self.move_shape_y_plus)
        parent.bind("<KeyPress-x>", self.move_shape_y_minus)
        parent.bind("<KeyPress-d>", self.move_shape_z_plus)
        parent.bind("<KeyPress-c>", self.move_shape_z_minus)

        parent.bind("<KeyPress-q>", self.rotate_selected_shape_x)
        parent.bind("<KeyPress-w>", self.rotate_selected_shape_y)
        parent.bind("<KeyPress-e>", self.rotate_selected_shape_z)

        parent.bind("<KeyPress-r>", self.scale_selected_shape_plus_ten_percent)
        parent.bind("<KeyPress-f>", self.scale_selected_shape_minus_ten_percent)
        parent.config(menu=self.menu_bar)
        self.create_menu_widgets()

    def scale_selected_shape_plus_ten_percent(self, select = None):
        if self.workspace.selected_shape is not None:
            self.workspace.selected_shape.scale(1.1)
            self.workspace.update_plot()

    def scale_selected_shape_minus_ten_percent(self, select = None):
        if self.workspace.selected_shape is not None:
            self.workspace.selected_shape.scale(0.9)
            self.workspace.update_plot()

    def rotate_selected_shape_x(self, select = None):
        if self.workspace.selected_shape is not None:
            self.workspace.selected_shape.rotate(np.pi / 4, 'x')
            self.workspace.update_plot()

    def rotate_selected_shape_y(self, select = None):
        if self.workspace.selected_shape is not None:
            self.workspace.selected_shape.rotate(np.pi / 4, 'y')
            self.workspace.update_plot()

    def rotate_selected_shape_z(self, select = None):
        if self.workspace.selected_shape is not None:
            self.workspace.selected_shape.rotate(np.pi / 4, 'z')
            self.workspace.update_plot()

    def move_shape_x_plus(self, select = None):
        print('aaaa')
        if self.workspace.selected_shape is not None:
            for point in self.workspace.selected_shape.points:
                point.x += 1
            self.workspace.update_plot()

    def move_shape_x_minus(self, select = None):
        if self.workspace.selected_shape is not None:
            for point in self.workspace.selected_shape.points:
                point.x -= 1
            self.workspace.update_plot()

    def move_shape_y_plus(self, select = None):
        if self.workspace.selected_shape is not None:
            for point in self.workspace.selected_shape.points:
                point.y += 1
            self.workspace.update_plot()

    def move_shape_y_minus(self, select = None):
        if self.workspace.selected_shape is not None:
            for point in self.workspace.selected_shape.points:
                point.y -= 1
            self.workspace.update_plot()

    def move_shape_z_plus(self, select = None):
        if self.workspace.selected_shape is not None:
            for point in self.workspace.selected_shape.points:
                point.z += 1
            self.workspace.update_plot()

    def move_shape_z_minus(self, select = None):
        if self.workspace.selected_shape is not None:
            for point in self.workspace.selected_shape.points:
                point.z -= 1
            self.workspace.update_plot()

    def key_handler(self, event):
        print(event.char, event.keysym, event.keycode)

    def save_file(self):
        if self.workspace.shapes:
            with open("shapes.txt", "w") as file:
                for shape in self.workspace.shapes:
                    points_str = " ".join(f"{point.x},{point.y},{point.z}" for point in shape.points)
                    file.write(f"{len(shape.points)} {points_str}\n")

    def clear_all(self):
        self.workspace.points = []
        self.workspace.selection_points = []
        self.workspace.selected_shape = None
        self.workspace.shapes = []
        self.workspace.update_plot()
        self.update_shapes_listbox()

    def update_shapes_listbox(self):
        self.shapes_listbox.delete(0, tk.END)
        for shape in self.workspace.shapes:
            self.shapes_listbox.insert(tk.END, f"Shape {self.workspace.shapes.index(shape) + 1}")

    def open_file(self):
        self.clear_all()
        try:
            with open("points.txt", "r") as file:
                for line in file:
                    num_points, *points_str = line.strip().split(" ")
                    num_points = int(num_points)
                    points = [Point(*map(float, point.split(","))) for point in points_str]
                    self.workspace.shapes.append(Shape(points))
            self.workspace.update_plot()
            self.update_shapes_listbox()
        except FileNotFoundError:
            print("Error: File not found")

    def create_shape(self):
        shape = Shape(self.workspace.points)
        self.workspace.shapes.append(shape)
        self.workspace.update_plot()
        self.update_shapes_listbox()
        self.workspace.points = []

    def select_shape(self, event):
        selected_index = self.shapes_listbox.curselection()
        if selected_index:
            self.selected_shape = self.workspace.shapes[selected_index[0]]
            self.workspace.selected_shape = self.selected_shape
        self.update_shapes_listbox()
        self.workspace.update_plot(select = self.selected_shape)

    def add_point(self):
        x = float(self.x_entry.get())
        y = float(self.y_entry.get())
        z = float(self.z_entry.get())
        self.workspace.add_point(x, y, z)

    def create_menu_widgets(self):
        self.preview_point = Point(x=0, y=0, z=0)

        self.point_frame = tk.Frame(self)
        self.point_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        self.x_label = tk.Label(self.point_frame, text="X:")
        self.x_label.pack(padx=5, pady=5)
        self.x_entry = tk.Entry(self.point_frame, width=10)
        self.x_entry.pack(padx=5, pady=5)

        self.y_label = tk.Label(self.point_frame, text="Y:")
        self.y_label.pack(padx=5, pady=5)
        self.y_entry = tk.Entry(self.point_frame, width=10)
        self.y_entry.pack(padx=5, pady=5)

        self.z_label = tk.Label(self.point_frame, text="Z:")
        self.z_label.pack(padx=5, pady=5)
        self.z_entry = tk.Entry(self.point_frame, width=10)
        self.z_entry.pack(padx=5, pady=5)

        self.add_button = tk.Button(self.point_frame, text="Add Point", command=self.add_point)
        self.add_button.pack(padx=5, pady=5)

        self.create_shape_button = tk.Button(self.point_frame, text="Create Shape", command=self.create_shape)
        self.create_shape_button.pack(padx=5, pady=5)

        self.clear_button = tk.Button(self.point_frame, text="Clear", command=self.clear_all)
        self.clear_button.pack(padx=5, pady=5)

        self.shapes_listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.shapes_listbox.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.shapes_listbox.bind("<<ListboxSelect>>", self.select_shape)