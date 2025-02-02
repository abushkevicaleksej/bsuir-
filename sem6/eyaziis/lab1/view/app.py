from imports import *
from view.edit import Edit
from view.main_win import Main
from tkinter import Menu, filedialog, messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test123")
        self.geometry('1024x640')
        self.resizable(False, False)
        center_window(self,1024, 640)
        #self.menu = Menu(self)
        #self.edit = Edit(self)
        self.main = Main(self)
        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        main_menu = Menu(self)

        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label = "Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        main_menu.add_cascade(label="File", menu=file_menu)

        about_menu = Menu(main_menu, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about)
        main_menu.add_cascade(label="Help", menu=about_menu)

        self.config(menu=main_menu)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open a file")
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)

    def save_file(self, content):
        file_path = filedialog.asksaveasfilename(title="Save a file", defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)

    def show_about(self):
        messagebox.showinfo("About", "праграма для языков чтоб разложить текст")