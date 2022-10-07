import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog, QApplication



class AmministratoreView(QDialog):
    def __init__(self):
        super(AmministratoreView, self).__init__()
        loader = QUiLoader()
        file = QFile("AmministratoreTestingView.ui")

        file.open(QFile.ReadOnly)
        prima = loader.load(file, self)
        file.close()



class Prima(QDialog):
    def __init__(self):
        super(Prima, self).__init__()
        loader = QUiLoader()
        file = QFile("prima.ui")
        file.open(QFile.ReadOnly)
        prima = loader.load(file, self)
        file.close()
        prima.gotosecbtn.clicked.connect(self.gotosec)
        prima.exitbtn.clicked.connect(self.exit)


    def gotosec(self):
        seconda = Seconda()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(seconda)
        widget.setCurrentIndex(widget.currentIndex())

    def exit(self):
        sys.exit(app.exec_())

class Seconda(QDialog):
    def __init__(self):
        super(Seconda, self).__init__()
        loader = QUiLoader()
        file = QFile("seconda.ui")
        file.open(QFile.ReadOnly)
        seconda = loader.load(file, self)
        file.close()
        seconda.gotopribtn.clicked.connect(self.gotoprim)

    def gotoprim(self):
        prima = Prima()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(prima)
        widget.setCurrentIndex(widget.currentIndex())

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
adminView = AmministratoreView()
widget.addWidget(adminView)
"""prima = Prima()
widget.addWidget(prima)"""
widget.setFixedHeight(570)
widget.setFixedWidth(920)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("exiting")