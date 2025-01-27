from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from PyQt5.QtCore import Qt, QPoint

from view.forms import ExplainForm


class ExplainView(QMainWindow):    
    TABLE_LABLE_TEMPLATE = "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">{model_name}</span></p></body></html>" 
    COLUMN_STEP_NAME = "i, step"
    
    def __init__(self):
        super(ExplainView, self).__init__()
        self.ui = ExplainForm(self)
        self.init_UI()
        
    def init_UI(self):
        self._hide_interface()
                
    def _hide_interface(self):
        pass
    
    def set_table_data(self, data: dict, model_name: str):
        rows_count = len(data.keys())
        data_values = list(data.values())
        columns_count = len(data_values[0]) + 1
        
        columns_names = [self.COLUMN_STEP_NAME]
        columns_names.extend(list(data_values[0].keys()))
        
        self.ui.ExplainTableWidget.setRowCount(rows_count)
        self.ui.ExplainTableWidget.setColumnCount(columns_count)
        self.ui.ExplainTableWidget.setHorizontalHeaderLabels(columns_names)
        self.ui.ExplainTableWidget.verticalHeader().setVisible(False)
        
        self.ui.PaintModelLabel.setAlignment(Qt.AlignCenter)
        self.ui.PaintModelLabel.setText(self.TABLE_LABLE_TEMPLATE.format(model_name=model_name))
        
        for irow in range(rows_count):
            for icol, col in enumerate(columns_names):
                if col == self.COLUMN_STEP_NAME:
                    item = QTableWidgetItem(str(irow))
                else:    
                    item = QTableWidgetItem(str(data_values[irow][col]))
                self.ui.ExplainTableWidget.setItem(irow, icol, item)
