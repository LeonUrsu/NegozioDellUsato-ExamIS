import sys

from Custom_Widgets.Widgets import *
from ui_interface_definitiva import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtWidgets
from PySide2 import *
from MVC.Model.Attività.Amministratore import *



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.mainpage = Ui_MainWindow()
        self.mainpage.setupUi(self)

        self.mainpage.homeBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.home))
        self.mainpage.homeBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.homeBtn.objectName()))


        self.mainpage.prodottiBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.prodotti))
        self.mainpage.prodottiBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.prodottiBtn.objectName()))


        self.mainpage.statisticBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.prodotti))
        self.mainpage.prodottiBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.prodottiBtn.objectName()))


        self.mainpage.accountBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.accounts))
        self.mainpage.accountBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.accountBtn.objectName()))


        self.mainpage.statisticBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.statistiche))
        self.mainpage.statisticBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.statisticBtn.objectName()))


        self.mainpage.loginBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.login))
        self.mainpage.loginBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.loginBtn.objectName()))

        
        #self.loadData()

        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.mainpage)
        ########################################################################

        self.show()

    def changeStyleSheet(self,bottone):
        self.mainpage.leftMenu.setStyleSheet(f"#{bottone}"
                                             "\n{"
"background-color:#1a1f39;\n"
"padding : 10px 5px;\n"
"text-align:left;\n"
"border-top-left-radius:25px;\n}\nQPushButton\n{\nbackground-color:#2a2c49;\n"
"border = 0px;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	color:#78799c;\n}")

    """def loadData(self):
        prodottiList = list()
        row = 0

        for x in range(5):
            dati = {"Nome": "nome"+x.__str__(), "ID": x.__str__(), "Data": x.__str__(), "Prezzo": x.__str__()}
            prodottiList.append(dati)


             self.mainpage.tableWidget.insertRow(row)
                self.mainpage.tableWidget.horizontalHeader()
                self.mainpage.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(testo))
               # self.mainpage.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(prodotto["ID"]))
               # self.mainpage.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(prodotto["Nome"]))

                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                self.mainpage.tableWidget.setItem(row, 0, chkBoxItem)
                row = row + 1"""

# esegui app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
    #end





