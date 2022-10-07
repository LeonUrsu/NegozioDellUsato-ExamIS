import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QApplication


class Prima(QDialog):
    def __init__(self):
        super(Prima, self).__init__()
        loadUi("prima.ui", self)
        self.button.clicked.connect(self.gotosec)

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