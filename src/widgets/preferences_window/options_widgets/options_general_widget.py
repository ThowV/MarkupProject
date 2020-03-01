from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget


class OptionsGeneralWidget(QWidget):
    def __init__(self, parent=None):
        super(OptionsGeneralWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(18, 18, 18, 18)

        self.test_label = QtWidgets.QLabel("", self)
        self.layout.addWidget(self.test_label)