

import tkinter as tk

class Lab1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабораторная работа #1")
        self.wm_state('zoomed')
        self.canvas_width = 800
        self.canvas_height = 800
        self.debug_mode = False

        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="white", highlightbackground='gray')
        self.canvas.pack(padx=5, pady=5, side=tk.LEFT)

        self.toolbar = tk.Frame(self.master)
        self.toolbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.debug_var = tk.BooleanVar()
        self.debug_checkbox = tk.Checkbutton(self.toolbar, text="Отладочный режим", variable=self.debug_var, command=self.toggle_debug_mode)
        self.debug_checkbox.pack()

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("ЦДА")
        self.algorithm_menu = tk.OptionMenu(self.toolbar, self.algorithm_var, "ЦДА", "Брезенхем", "Ву")
        self.algorithm_menu.pack()

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

        self.debug_text = tk.Text(self.master, height=48, width=45)
        self.debug_text.pack(side=tk.RIGHT)

        self.debug_text.insert(tk.END, "Для отладки\n")

        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

    def toggle_debug_mode(self):
        self.debug_mode = self.debug_var.get()

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        self.end_x = event.x
        self.end_y = event.y

    def end_draw(self, event):
        self.canvas.delete("line")
        self.draw_line()

    def draw_line(self):
        if self.algorithm_var.get() == "ЦДА":
            if self.debug_mode:
                self.debug_text.insert(tk.END, "ЦДА:\n")
            self.draw_dda(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.algorithm_var.get() == "Брезенхем":
            if self.debug_mode:
                self.debug_text.insert(tk.END, "Брезенхем:\n")
            self.draw_bresenham(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.algorithm_var.get() == "Ву":
            if self.debug_mode:
                self.debug_text.insert(tk.END, "Ву:\n")
            self.draw_wu(self.start_x, self.start_y, self.end_x, self.end_y)

    def draw_dda(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        steps = max(abs(dx), abs(dy))
        x_increment = dx / steps
        y_increment = dy / steps
        x = x0
        y = y0
        for _ in range(steps):
            self.canvas.create_rectangle(round(x), round(y), round(x), round(y), fill="black")
            x += x_increment
            y += y_increment
            if self.debug_mode:
                self.debug_text.insert(tk.END, f"({round(x)}, {round(y)})\n")
                self.debug_text.see(tk.END)
                self.update()
                self.after(50)

    def draw_bresenham(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while x0 != x1 or y0 != y1:
            self.canvas.create_rectangle(x0, y0, x0, y0, fill="black")
            if self.debug_mode:
                self.debug_text.insert(tk.END, f"({x0}, {y0})\n")
                self.debug_text.see(tk.END)
                self.update()
                self.after(50)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def draw_wu(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        if dx > dy:
            if x0 > x1:
                x0, y0, x1, y1 = x1, y1, x0, y0
            gradient = dy / dx
            xend = round(x0)
            yend = y0 + gradient * (xend - x0)
            xgap = 1 - (x0 + 0.5) % 1
            xpxl1 = xend
            ypxl1 = int(yend)
            self.canvas.create_rectangle(xpxl1, ypxl1, xpxl1, ypxl1, fill="black", width=1)
            self.canvas.create_rectangle(xpxl1, ypxl1 + 1, xpxl1, ypxl1 + 1, fill="black", width=1)
            intery = yend + gradient

            xend = round(x1)
            yend = y1 + gradient * (xend - x1)
            xgap = (x1 + 0.5) % 1
            xpxl2 = xend
            ypxl2 = int(yend)
            self.canvas.create_rectangle(xpxl2, ypxl2, xpxl2, ypxl2, fill="black", width=1)
            self.canvas.create_rectangle(xpxl2, ypxl2 + 1, xpxl2, ypxl2 + 1, fill="black", width=1)

            for x in range(xpxl1 + 1, xpxl2):
                self.canvas.create_rectangle(x, int(intery), x, int(intery), fill="black", width=1)
                self.canvas.create_rectangle(x, int(intery) + 1, x, int(intery) + 1, fill="black", width=1)
                intery += gradient
                if self.debug_mode:
                    self.debug_text.insert(tk.END, f"({x}, {int(intery)})\n")
                    self.debug_text.see(tk.END)
                    self.update()
                    self.after(50)
        else:
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0
            gradient = dx / dy
            yend = round(y0)
            xend = x0 + gradient * (yend - y0)
            ygap = 1 - (y0 + 0.5) % 1
            ypxl1 = yend
            xpxl1 = int(xend)
            self.canvas.create_rectangle(xpxl1, ypxl1, xpxl1, ypxl1, fill="black", width=1)
            self.canvas.create_rectangle(xpxl1 + 1, ypxl1, xpxl1 + 1, ypxl1, fill="black", width=1)
            interx = xend + gradient

            yend = round(y1)
            xend = x1 + gradient * (yend - y1)
            ygap = (y1 + 0.5) % 1
            ypxl2 = yend
            xpxl2 = int(xend)
            self.canvas.create_rectangle(xpxl2, ypxl2, xpxl2, ypxl2, fill="black", width=1)
            self.canvas.create_rectangle(xpxl2 + 1, ypxl2, xpxl2 + 1, ypxl2, fill="black", width=1)

            for y in range(ypxl1 + 1, ypxl2):
                self.canvas.create_rectangle(int(interx), y, int(interx), y, fill="black", width=1)
                self.canvas.create_rectangle(int(interx) + 1, y, int(interx) + 1, y, fill="black", width=1)
                interx += gradient
                if self.debug_mode:
                    self.debug_text.insert(tk.END, f"({int(interx)}, {y})\n")
                    self.debug_text.see(tk.END)
                    self.update()
                    self.after(50)

if __name__ == "__main__":
   lab1 = Lab1()
   lab1.mainloop()
