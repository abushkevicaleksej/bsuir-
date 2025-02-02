from imports import *
from view.table import Table
from view.workspace import Workspace

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = ttk.Frame(self, relief="groove", borderwidth=1)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        self.workspace = Workspace(self.bottom_frame)
        self.table = Table(self.bottom_frame)