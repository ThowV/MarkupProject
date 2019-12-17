import mistune
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets


class MarkupPreviewerUI(object):
    def setup_ui(self, parent_widget):
        # Preview dock widget master
        self.preview_dock_widget = QtWidgets.QDockWidget(parent_widget)
        self.preview_dock_widget.setStyleSheet("")
        self.preview_dock_widget.setObjectName("PreviewDockWidget")

        # Preview widget
        self.preview_widget = QtWidgets.QWidget()
        self.preview_widget.setObjectName("PreviewWidget")

        # Preview layout
        self.preview_layout = QtWidgets.QGridLayout(self.preview_widget)
        self.preview_layout.setContentsMargins(3, 3, 3, 3)
        self.preview_layout.setObjectName("PreviewLayout")

        # Preview content
        self.preview_web_engine_widget = QtWebEngineWidgets.QWebEngineView()
        self.preview_web_engine_widget.setObjectName("PreviewWebEngineWidget")
        self.preview_web_engine_widget.setHtml("<h1>This is some test HTML</h1>")
        self.preview_layout.addWidget(self.preview_web_engine_widget, 0, 0, 1, 1)

        # Finalization
        self.preview_dock_widget.setWidget(self.preview_widget)
        parent_widget.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.preview_dock_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.preview_dock_widget.setWindowTitle(_translate("MainWindow", "Markdown preview"))
