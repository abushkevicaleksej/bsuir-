import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np
from model.point import Point
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Workspace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.points = []
        self.shapes = []
        self.preview_point = Point(0, 0, 0)
        self.selected_shape = None
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.create_workspace_widget()

    def create_workspace_widget(self):
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.axis('on')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

    def draw_shape(self, x_values, y_values, z_values):
        num_steps = 20
        if len(x_values) >= 3:
            lines = []
            for i in range(len(x_values)):
                for j in range(i + 1, len(x_values)):
                    lines.append([i, j])

            interpolated_lines = []
            for line in lines:
                x_interp = np.linspace(x_values[line[0]], x_values[line[1]], num_steps)
                y_interp = np.linspace(y_values[line[0]], y_values[line[1]], num_steps)
                z_interp = np.linspace(z_values[line[0]], z_values[line[1]], num_steps)
                interpolated_lines.append(list(zip(x_interp, y_interp, z_interp)))

            for line in interpolated_lines:
                x, y, z = zip(*line)
                self.ax.plot(x, y, z, color='black', linewidth=1)
        else:
            self.ax.plot(x_values, y_values, z_values)

    def add_point(self, x, y, z):
        point = Point(x, y, z)
        self.points.append(point)
        self.update_plot()

    def update_plot(self, select= None):
        self.ax.clear()

        for shape in self.shapes:
            points = shape.points
            x_values = [point.x for point in points]
            y_values = [point.y for point in points]
            z_values = [point.z for point in points]
            self.draw_shape(x_values, y_values, z_values)

        if self.points:
            marked_x = [point.x for point in self.points]
            marked_y = [point.y for point in self.points]
            marked_z = [point.z for point in self.points]
            self.ax.scatter(marked_x, marked_y, marked_z, color='red', s=50)

        if self.preview_point:
            self.ax.scatter(self.preview_point.x, self.preview_point.y, self.preview_point.z, color='green', s=50)

        if select is not None:
            select.update_points()
            for point in select.points:
                self.ax.scatter(point.x, point.y, point.z, color='cyan', s=50)
            self.ax.scatter(select.center_point.x, select.center_point.y,
                            select.center_point.z, color='purple', s=20)
        self.canvas.draw()
