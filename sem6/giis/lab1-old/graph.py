import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test123")
        self.geometry('1024x640')
        self.resizable(False, False)

        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(fill=X, expand=False)
        self.create_widgets()

    def create_widgets(self):
        file_button = ttk.Button(self, text='Select file', command=open_file)
        process_button = ttk.Button(self, text='Process file')
        file_button.pack()
        process_button.pack()


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = ttk.Frame(self, relief="groove", borderwidth=1)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        self.workspace = Workspace(self.bottom_frame)
        self.table = Table(self.bottom_frame)

class Workspace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.create_edit_widgets()

    def create_edit_widgets(self):
        edit_button = ttk.Button(self, text='Button 3')
        edit_button.pack(pady=10)

class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.create_edit_widgets()

    def create_edit_widgets(self):
        edit_button = ttk.Button(self, text='Button 2')
        edit_button.pack(pady=10)

App()