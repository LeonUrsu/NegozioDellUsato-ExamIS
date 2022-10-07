import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore , QtGui, QtWidgets



class Prima(QDialog):
    def __init__(self):
        super().__init__()
        self.mainpage = QUiLoader().load("prima.ui", self)
        self.mainpage.button.clicked.connect(self.gotosec)

    def gotosec(self):
        seconda = Seconda()
        widget.addWidget(seconda)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Seconda(QDialog):
    def __init__(self):
        super(Seconda, self).__init__()
        loadUi("seconda.ui", self)
        self.gotopribtn.clicked.connect(self.gotoprim)

    def gotoprim(self):
        prima = Prima()
        widget.addWidget(prima)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
prima = Prima()
widget.addWidget(prima)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("exiting")