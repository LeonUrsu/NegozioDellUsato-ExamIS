
from Custom_Widgets.Widgets import *
from PyQt5.QtWidgets import QWidget, QMainWindow
from ProdottoInterface import ProdottoInterface
from ui_interface_definitiva import *
from PyQt5 import *

class AmministratoreView(QWidget):

    def __init__(self, parent= None ):
        super(QMainWindow).__init__(parent)
        loadUi("AmministratoreView.ui", self)
        """
                self.cambiaPagina(self.mainpage.aggiungiBtn, self.mainpage.aggiungiProdottopg)
                self.cambiaPagina(self.mainpage.homeBtn, self.mainpage.home)
                self.cambiaPagina(self.mainpage.prodottiBtn, self.mainpage.prodotti)
                self.cambiaPagina(self.mainpage.accountBtn, self.mainpage.accounts)
                self.cambiaPagina(self.mainpage.statisticBtn, self.mainpage.statistiche)
                self.cambiaPagina(self.mainpage.saveBtn, self.mainpage.prodotti)
                self.mainpage.saveBtn.clicked.connect(lambda: ProdottoInterface().test(self.mainpage.nomeLe))
                self.mainpage.rimuoviBtn.clicked.connect(lambda: ProdottoInterface().inserisciProdottiTableWidget(self.mainpage.tableWidget))
        
        
        
        
                # APPLY JSON STYLESHEET
                # self = QMainWindow class
                # self.ui = Ui_MainWindow / user interface class
                loadJsonStyle(self, self.mainpage)
                ########################################################################
        
        
                #quit Button
                self.mainpage.quitBtn.clicked.connect(lambda: QtCore.QCoreApplication.instance().quit())
        
                self.show()
            """

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
