import tkinter as tk
from tkinter import *
from view.center_window import center_window
from view.workspace import Workspace
from view.menu import Menu

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test123")
        self.geometry('1280x720')
        self.resizable(False, False)
        center_window(self, 1280, 720)
        self.menu = Menu(self)
        self.mainloop()