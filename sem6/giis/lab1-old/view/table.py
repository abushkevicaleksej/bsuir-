import tkinter as tk
from tkinter import *
from tkinter import ttk

class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.create_table_widgets()

    def create_table_widgets(self):
        self.table = ttk.Treeview(self, show="headings", columns=("iteration", "x", "y", "plot"))
        self.table.pack(side=LEFT, fill=BOTH, expand=True)

        self.table.heading("iteration", text="Итерация")
        self.table.heading("x", text="X")
        self.table.heading("y", text="Y")
        self.table.heading("plot", text="Plot(X; Y)")

        self.table.column("iteration", width=80, anchor=CENTER)
        self.table.column("x", width=100, anchor=CENTER)
        self.table.column("y", width=100, anchor=CENTER)
        self.table.column("plot", width=150, anchor=CENTER)

        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.table.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.table.configure(yscroll=scrollbar.set)

    def update_table(self, points):

        self.table.delete(*self.table.get_children())

        for i, (x, y) in enumerate(points):
            self.table.insert("", "end", values=(i + 1, x, y, f"({x}; {y})"))

    def clear_table(self):
        self.table.delete(*self.table.get_children())

