import sys

from Custom_Widgets.Widgets import *

from ProdottoInterface import ProdottoInterface
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

        self.cambiaPagina(self.mainpage.aggiungiBtn, self.mainpage.aggiungiProdottopg)
        self.cambiaPagina(self.mainpage.homeBtn, self.mainpage.home)
        self.cambiaPagina(self.mainpage.prodottiBtn, self.mainpage.prodotti)
        self.cambiaPagina(self.mainpage.accountBtn, self.mainpage.accounts)
        self.cambiaPagina(self.mainpage.statisticBtn, self.mainpage.statistiche)
        self.cambiaPagina(self.mainpage.loginBtn, self.mainpage.login)
        self.cambiaPagina(self.mainpage.saveBtn, self.mainpage.prodotti)
        self.mainpage.saveBtn.clicked.connect(lambda: ProdottoInterface().aggiungiProdottoTramiteApp())
        self.mainpage.rimuoviBtn.clicked.connect(lambda: ProdottoInterface().inserisciProdottiTableWidget())
        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.mainpage)
        ########################################################################


        #quit Button
        self.mainpage.quitBtn.clicked.connect(lambda: QtCore.QCoreApplication.instance().quit())

        self.show()

    #Metodo che implementa il cambiamento della finestra al click di un PushButton
    def cambiaPagina(self,bottone,finestra):
        bottone.clicked.connect(
            lambda: self.mainpage.finestreSecondarie.setCurrentWidget(finestra))
        bottone.clicked.connect(
            lambda: self.changeStyleSheet(bottone.objectName()))

     #Metodo che implementa il cambio della grafica del PushButton cliccato
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

# esegui app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
    #end





