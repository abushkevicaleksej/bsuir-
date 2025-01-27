import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test123")
        self.geometry('1024x640')
        self.resizable(False, False)

        self.menu = Menu(self)
        self.edit = Edit(self)
        self.main = Main(self)

        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief= "groove", borderwidth= 1)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        file_button = ttk.Button(self, text= 'Select file', command=open_file)
        process_button = ttk.Button(self, text='Process file')
        file_button.pack()
        process_button.pack()

        

class Edit(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief= "groove", borderwidth= 1)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_edit_widgets()

    def create_edit_widgets(self):
        edit_button = ttk.Button(self, text = 'Button 2')
        edit_button.pack()

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        columns = ("Word", "Morphologic info", "Occurancy")
        Table(self, columns)

class Table(ttk.Frame):
    def __init__(self, parent, columns):
        super().__init__(parent)
        tree = ttk.Treeview(columns=columns, show="headings")

        tree.pack(fill=BOTH, expand=1)
        tree.heading(columns[0], text=columns[0])
        tree.heading(columns[1], text=columns[1])
        tree.heading(columns[2], text=columns[2])

def open_file():
    filepath = filedialog.askopenfile()
    if filepath != "":
        file = filedialog.askopenfile(mode="r")
        text = file.read()
    else:
        print("Pustoi fail!")

App()