import tkinter as tk
from tkinter import *
from tkinter import ttk

class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.create_table_widgets()

    def create_table_widgets(self):
        table = ttk.Treeview(master=self, show="headings")
        table.pack(side = LEFT, fill = BOTH, expand = True)

        # table.heading("x", text="X")
        # table.heading("y", text="Y")
        # table.heading("coords", text="Координаты")
        #
        # table.column("x", stretch=YES, width=100)
        # table.column("y", stretch=YES, width=100)
        # table.column("coords", stretch=YES, width=100)