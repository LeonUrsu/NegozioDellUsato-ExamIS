from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget


class AmministratoreView(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        file = QFile("AmministratoreView.ui")
        file.open(QFile.ReadOnly)
        loader.load(file)
        file.close()
