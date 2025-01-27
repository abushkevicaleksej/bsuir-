import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Workspace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        self.create_workspace_widgets()

    def create_workspace_widgets(self):
        f = Figure(figsize = (5,5), dpi=100)
        a = f.add_subplot(111)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.pack()

    def process_plot(self, type, coords):
        pass