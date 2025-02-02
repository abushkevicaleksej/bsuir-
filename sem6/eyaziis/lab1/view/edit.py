from imports import *

class Edit(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief= "groove", borderwidth= 1)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_edit_widgets()

    def create_edit_widgets(self):
        edit_button = ttk.Button(self, text = 'Button 2')
        edit_button.pack()