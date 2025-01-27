from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from PyQt5.QtCore import Qt

from view.forms import MainForm, GridDataForm


class MainView(QMainWindow):    
    draw_line_switcher = False

    def __init__(self):
        super(MainView, self).__init__()
        self.ui = MainForm(self)
        self.grid = GridDataForm(self)
        self.paint_model = None
        self.cache_points = []
        self.cache_saturation = []
        
        self.init_UI()
        
    def init_UI(self):
        self.ui.DrawPushButton.clicked.connect(self.draw_line)
        
        self._hide_interface()
    
    def _hide_interface(self):
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        def _draw_grid():
            pen = QPen(Qt.black)
            pen.setWidth(1)
            painter.setPen(pen)

            # Draw the coordinate grid
            for x in range(self.grid.start_x, self.grid.start_x + self.grid.size + 1, self.grid.spacing):
                painter.drawLine(x, self.grid.start_y, x, self.grid.start_y + self.grid.size)

            for y in range(self.grid.start_y, self.grid.start_y + self.grid.size + 1, self.grid.spacing):
                painter.drawLine(self.grid.start_x, y, self.grid.start_x + self.grid.size, y)
        
            # Draw axis labels
            font = QFont("Arial", 15)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(self.grid.start_x - 15, self.grid.start_y + self.grid.size + 15, "0")
            painter.drawText(self.grid.start_x + self.grid.size // 2 - 5, self.grid.start_y + self.grid.size + 25, "Ось X")
            painter.drawText(self.grid.start_x - 25, self.grid.start_y + self.grid.size // 2 - 5, "Ось Y")

        _draw_grid()

        color = QColor(0, 0, 255)
        if self.draw_line_switcher:
            paint_template = self.grid.PAINT_TEMPLATES[self.ui.LineManagerComboBox.currentText()]
            self.paint_model = paint_template(coords=self.points)
            draw_points = self.paint_model.coords

            for i in range(len(draw_points)):
                point1 = self._calc_point(draw_points[i])
                # point2 = self._calc_point(draw_points[i + 1])
                self.cache_points.append((point1[0], point1[1]))
                if s := self.paint_model._c:
                    saturation = int(s[i] * 255)
                    self.cache_saturation.append(saturation)
                    color.setHsv(color.hue(), saturation, color.value())

                painter.setBrush(color)                        
                painter.drawRect(point1[0], point1[1], self.grid.spacing, self.grid.spacing)
        else:
            si = 0
            for x, y in self.cache_points:
                if self.cache_saturation:
                    saturation = self.cache_saturation[si]
                    color.setHsv(color.hue(), saturation, color.value())
                    si += 1
                painter.setBrush(color)
                painter.drawRect(x, y, self.grid.spacing, self.grid.spacing)
        self.draw_line_switcher = False
        

    def draw_line(self):
        self.draw_line_switcher = True
        self.cache_points = []
        self.cache_saturation = []
        self.update()
        print("Line drawed!")

    def get_explain_data(self):
        if self.paint_model:
            return self.paint_model.res_table, str(self.paint_model)
        
        return {}, ''
    
    @property
    def points(self):
        return (
            self.ui.x1SpinBox.value(),
            self.ui.y1SpinBox.value(), 
            self.ui.x2SpinBox.value(),
            self.ui.y2SpinBox.value()
        )

    def _calc_point(self, coords):
        x1, y1 = coords
        return (
            x1 * self.grid.POINT_MULT + self.grid.start_x,
            self.grid.size -  y1 * self.grid.POINT_MULT + self.grid.start_y - 10
        )