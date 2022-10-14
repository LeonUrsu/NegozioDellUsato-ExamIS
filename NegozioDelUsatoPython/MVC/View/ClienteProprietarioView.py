from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog


class ClienteProprietarioView(QDialog):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        file = QFile("ClienteProprietarioView.ui")
        file.open(QFile.ReadOnly)
        finestra = loader.load(file, self)
        file.close()
        #finestra.firstWidget.mainBody.mainFrame.widget.open_close_side_bar_btn.clicked.connect(self.slideLeftMenu())
        #