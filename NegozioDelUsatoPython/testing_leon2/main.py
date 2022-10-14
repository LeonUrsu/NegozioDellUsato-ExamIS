import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QFile, QPropertyAnimation
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog, QApplication, QTableWidget, QWidget, QCheckBox, QTableWidgetItem, QVBoxLayout, \
    QLayout, QHBoxLayout, QGridLayout, QPushButton


class Finestra(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        file = QFile("finestra.ui")
        file.open(QFile.ReadOnly)
        loader.load(file)
        file.close()



class ClienteProprietarioView(QDialog):
    def __init__(self):
        super(ClienteProprietarioView, self).__init__()
        loader = QUiLoader()
        file = QFile("ClienteProprietarioView.ui")
        file.open(QFile.ReadOnly)
        prima = loader.load(file, self)
        file.close()
        widget.primoWidget.setMinimumWidth(920)
        widget.primoWidget.setMinimumHeight(570)
        #prima.firstWidget.mainBody.mainFrame.widget.open_close_side_bar_btn.clicked.connect(self.slideLeftMenu())



class AmministratoreView(QDialog):
    def __init__(self):
        super(AmministratoreView, self).__init__()
        loader = QUiLoader()
        file = QFile("AmministratoreView.ui")
        file.open(QFile.ReadOnly)
        prima = loader.load(file, self)
        file.close()
        #prima.firstWidget.mainBody.mainFrame.widget.open_close_side_bar_btn.clicked.connect(self.slideLeftMenu())


    def slideLeftMenu(self):
        # Get current left menu width
        width = self.leftMenu
        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/align-left.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


class Prima(QDialog):
    def __init__(self):
        super(Prima, self).__init__()
        loader = QUiLoader()
        file = QFile("prima.ui")
        file.open(QFile.ReadOnly)
        self.prima = loader.load(file, self)
        file.close()
        #self.prima.gotosecbtn.clicked.connect(self.gotosec)
        #self.prima.exitbtn.clicked.connect(self.exit)


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
        self.seconda = loader.load(file, self)
        file.close()
        self.seconda.gotopribtn.clicked.connect(self.gotoprim)
        self.seconda.gotolistbtn.clicked.connect(self.gotolist)

    def gotoprim(self):
        prima = Prima()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(prima)
        widget.setCurrentIndex(widget.currentIndex())

    def gotolist(self):
        form = Form()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(form)
        widget.setCurrentIndex(widget.currentIndex())

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        loader = QUiLoader()
        file = QFile("Form.ui")
        file.open(QFile.ReadOnly)
        forma = loader.load(file, self)
        file.close()
        lista = self.listFiller()
        forma.tab.setColumnWidth(0, 50)
        forma.tab.setColumnWidth(1, 200)
        forma.tab.setColumnWidth(2, 200)
        row = 0
        forma.tab.setRowCount(len(lista))
        for persona in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            forma.tab.setItem(row, 0, chkBoxItem)
            forma.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(persona.nome))
            forma.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(persona.cognome))
            row += 1
        forma.ok.clicked.connect(lambda: self.printed(forma))

    def printed(self, forma):
        data = []
        for row in range(forma.tab.rowCount()):
            it = forma.tab.item(row, 0)
            if it.checkState() == PySide6.QtCore.Qt.CheckState.Checked:
                print(f"row {row} is True")
            elif it.checkState() == PySide6.QtCore.Qt.CheckState.Unchecked:
                print(f"row {row} is False")

    def listFiller(self):
        class persona(object):
            def __init__(self, nome, cognome):
                self.nome = nome
                self.cognome = cognome
        listaPerDeathNote = list()
        for x in range(10):
            listaPerDeathNote.append(persona(f"yvonne{x}", f"olivieri{x}"))
        return listaPerDeathNote







app = QApplication(sys.argv)


"""
<<<<<<< HEAD
=======
widget = QtWidgets.QStackedWidget()
<<<<<<< HEAD
var = True
if var:
    adminView = AmministratoreView()
    widget.addWidget(adminView)
else:
    prima = Prima()
    widget.addWidget(prima)
=======
>>>>>>> c32fa2adec740ce657f5462d2b45356973c991fa
var = 3
if var == 1:
    primoWidget = AmministratoreView()
    widget.addWidget(primoWidget)
elif var == 2:
    primoWidget = Prima()
    widget.addWidget(primoWidget)
elif var == 3:
    primoWidget = ClienteProprietarioView()
    widget.addWidget(primoWidget)"""

"""widget.primoWidget.setMinimumWidth(920)
widget.primoWidget.setMinimumHeight(570)"""

<<<<<<< HEAD
=======
#widget = AmministratoreView()
>>>>>>> 1238a42e8da49da60ce56a3708be6b3a68d7b8b2
widget.show()
>>>>>>> c32fa2adec740ce657f5462d2b45356973c991fa


#widget = QtWidgets.QStackedWidget()
loader = QUiLoader()
file = QFile("stacked.ui")
file.open(QFile.ReadOnly)
rar = loader.load(file)
file.close()

file = QFile("ClienteProprietarioView.ui")
file.open(QFile.ReadOnly)
prima = loader.load(file)
file.close()

rar.verticalLayout.addWidget(prima)


"""for i in reversed(range(rar.verticalLayout.count())):
    rar.verticalLayout.itemAt(i).widget().setParent(None)

file = QFile("seconda.ui")
file.open(QFile.ReadOnly)
seconda = loader.load(file)
file.close()
rar.verticalLayout.addWidget(seconda)
"""

rar.show()

try:
    sys.exit(app.exec())
except:
    print("exiting")