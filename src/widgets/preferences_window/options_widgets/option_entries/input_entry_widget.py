from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.widgets.components.button_line_edit import ButtonLineEdit


class InputEntryWidget(QWidget):
    buttonClicked = QtCore.pyqtSignal(bool)

    def __init__(self, label_text, icon_path=None, parent=None):
        super(InputEntryWidget, self).__init__(parent)
        self.init_ui(label_text, icon_path)

    def init_ui(self, label_text, icon_path):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)

        # Options entry
        self.label = QtWidgets.QLabel(self)
        self.label.setText(label_text + ": ")
        self.layout.addWidget(self.label)

        self.button_line_edit = ButtonLineEdit(icon_path, self)
        self.button_line_edit.setClearButtonEnabled(True)
        self.button_line_edit.buttonClicked.connect(self.buttonClicked.emit)
        self.layout.addWidget(self.button_line_edit)

    def set_text(self, text):
        self.button_line_edit.setText(text)

    def get_text(self):
        return self.button_line_edit.text()
