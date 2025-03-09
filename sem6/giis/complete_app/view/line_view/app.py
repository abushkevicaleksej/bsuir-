import tkinter as tk
from tkinter import *
from tkinter import ttk
from view.line_view.menu import Menu
from view.line_view.main_view import Main
from utils import center_window

class LineAppWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(expand=True, fill=tk.BOTH)

        self.main = Main(self)
        self.menu = Menu(self, self.main.workspace, self.main.table)

        # self.mainloop()