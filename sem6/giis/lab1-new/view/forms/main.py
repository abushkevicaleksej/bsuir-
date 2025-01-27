from PyQt5 import QtCore, QtWidgets

from model.cda import CDAManager
from model.brez import BrazenhemManager
from model.wu import WuManager

class MainForm(object):
    def __init__(self, form) -> None:
        self.setupUi(form)

    def setupUi(self, LineForm):
        LineForm.setObjectName("LineForm")
        LineForm.resize(700, 700)
        self.DrawPushButton = QtWidgets.QPushButton(LineForm)
        self.DrawPushButton.setGeometry(QtCore.QRect(310, 660, 89, 25))
        self.DrawPushButton.setObjectName("DrawPushButton")
        self.LineManagerComboBox = QtWidgets.QComboBox(LineForm)
        self.LineManagerComboBox.setGeometry(QtCore.QRect(575, 20, 111, 25))
        self.LineManagerComboBox.setObjectName("LineManagerComboBox")
        self.LineManagerComboBox.addItem("")
        self.LineManagerComboBox.addItem("")
        self.LineManagerComboBox.addItem("")
        self.x1SpinBox = QtWidgets.QSpinBox(LineForm)
        self.x1SpinBox.setGeometry(QtCore.QRect(640, 100, 48, 26))
        self.x1SpinBox.setObjectName("x1SpinBox")
        self.y1SpinBox = QtWidgets.QSpinBox(LineForm)
        self.y1SpinBox.setGeometry(QtCore.QRect(640, 140, 48, 26))
        self.y1SpinBox.setObjectName("y1SpinBox")
        self.x2SpinBox = QtWidgets.QSpinBox(LineForm)
        self.x2SpinBox.setGeometry(QtCore.QRect(640, 180, 48, 26))
        self.x2SpinBox.setObjectName("x2SpinBox")
        self.y2SpinBox = QtWidgets.QSpinBox(LineForm)
        self.y2SpinBox.setGeometry(QtCore.QRect(640, 220, 48, 26))
        self.y2SpinBox.setObjectName("y2SpinBox")
        self.x1Label = QtWidgets.QLabel(LineForm)
        self.x1Label.setGeometry(QtCore.QRect(610, 100, 31, 31))
        self.x1Label.setObjectName("x1Label")
        self.y1Label = QtWidgets.QLabel(LineForm)
        self.y1Label.setGeometry(QtCore.QRect(610, 140, 31, 31))
        self.y1Label.setObjectName("y1Label")
        self.x2Label = QtWidgets.QLabel(LineForm)
        self.x2Label.setGeometry(QtCore.QRect(610, 180, 31, 31))
        self.x2Label.setObjectName("x2Label")
        self.y2Label = QtWidgets.QLabel(LineForm)
        self.y2Label.setGeometry(QtCore.QRect(610, 220, 31, 31))
        self.y2Label.setObjectName("y2Label")
        self.ExplainPushButton = QtWidgets.QPushButton(LineForm)
        self.ExplainPushButton.setGeometry(QtCore.QRect(600, 660, 89, 25))
        self.ExplainPushButton.setObjectName("ExplainPushButton")

        self.retranslateUi(LineForm)
        QtCore.QMetaObject.connectSlotsByName(LineForm)

    def retranslateUi(self, LineForm):
        _translate = QtCore.QCoreApplication.translate
        LineForm.setWindowTitle(_translate("LineForm", "Form"))
        self.DrawPushButton.setText(_translate("LineForm", "Рисовать"))
        self.LineManagerComboBox.setItemText(0, _translate("LineForm", "ЦДА"))
        self.LineManagerComboBox.setItemText(1, _translate("LineForm", "Метод Брезенхема"))
        self.LineManagerComboBox.setItemText(2, _translate("LineForm", "Метод Ву"))
        self.x1Label.setText(_translate("LineForm", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">X1</span></p></body></html>"))
        self.y1Label.setText(_translate("LineForm", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Y1</span></p></body></html>"))
        self.x2Label.setText(_translate("LineForm", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">X2</span></p></body></html>"))
        self.y2Label.setText(_translate("LineForm", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Y2</span></p></body></html>"))
        self.ExplainPushButton.setText(_translate("LineForm", "Подробный режим"))


class GridDataForm:
    MARGIN = 100
    COORD_LEN = 50
    POINT_MULT = 10
    PAINT_TEMPLATES = {
        'ЦДА': CDAManager,
        'Метод Брезенхема': BrazenhemManager,
        'Метод Ву': WuManager,
    }

    def __init__(self, view):
        self.size = min(view.width(), view.height()) - 2 * self.MARGIN # 500
        self.spacing = self.size // self.COORD_LEN # 10
        self.start_x = (view.width() - self.size) // 2 # 100
        self.start_y = (view.height() - self.size) // 2 # 100

