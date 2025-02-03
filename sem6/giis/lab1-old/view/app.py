import tkinter as tk
from tkinter import *
from view.menu import Menu
from view.main_view import Main
from view.center_window import center_window

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test123")
        self.geometry('1280x720')
        self.resizable(False, False)
        center_window(self, 1280, 720)

        self.main = Main(self)
        self.menu = Menu(self, self.main.workspace, self.main.table)

        self.mainloop()