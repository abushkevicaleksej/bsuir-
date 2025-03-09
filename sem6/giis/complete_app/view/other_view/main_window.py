from tkinter import ttk
import tkinter as tk
from model.other_model.point import Point
from model.other_model.delone_triangulation import DelaunayTriangulation
from model.other_model.voronoi_diagram import VoronoiDiagram


class OtherAppWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(expand=True, fill=tk.BOTH)

        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        self.mode_var = tk.IntVar(value=0)
        self.delone_mode_checkbox = tk.Checkbutton(self.control_frame, text="Триангуляция Делоне", variable=self.mode_var)
        self.voronoi_mode_checkbox = tk.Checkbutton(self.control_frame, text="Диаграмма Вороного", variable=self.mode_var)
        self.delone_mode_checkbox.pack(side=tk.LEFT, padx=5, pady=5)
        self.voronoi_mode_checkbox.pack(side=tk.LEFT, padx=5, pady=5)

        self.build_button = tk.Button(self.control_frame, text="Построить", command=self.build)
        self.build_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(self.control_frame, text="Очистить", command=self.clear)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas = tk.Canvas(self, width=1280, height=720, bg="white")
        self.canvas.pack()

        self.points = []
        self.canvas.bind("<Button-1>", self.add_point)

    def add_point(self, event):
        p = Point(event.x, event.y)
        self.points.append(p)
        self.draw_point(p)

    def draw_point(self, p):
        r = 3
        self.canvas.create_oval(p.x - r, p.y - r, p.x + r, p.y + r, fill="black")

    def build(self):
        if len(self.points) < 3:
            return
        delaunay = DelaunayTriangulation(self.points)
        triangles = delaunay.triangulate()
        self.canvas.delete("all")
        for p in self.points:
            self.draw_point(p)

        if self.mode_var.get() == 1:
            voronoi = VoronoiDiagram(triangles)
            voronoi_edges = voronoi.compute()
            self.draw_voronoi(voronoi_edges)
        else:
            self.draw_triangulation(triangles)

    def draw_triangulation(self, triangles):
        for t in triangles:
            coords = []
            for p in t.points:
                coords.extend([p.x, p.y])
            self.canvas.create_polygon(coords, outline="blue", fill="", width=1)

    def draw_voronoi(self, edges):
        for edge in edges:
            p1, p2 = edge
            self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="red", dash=(4, 2))

    def clear(self):
        self.canvas.delete("all")
        self.points = []