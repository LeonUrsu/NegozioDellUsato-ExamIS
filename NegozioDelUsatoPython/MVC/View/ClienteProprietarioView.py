import os
import sys

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog, QApplication, QPushButton


class ClienteProprietarioView():
    def __init__(self, mainPath):
        #super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "ClienteProprietarioView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(self.finestra))
        self.finestra.iMieiDatiBtn.clicked.connect(lambda: self.iMieiDatiBtnClicked(self.finestra))
        self.finestra.iMieiProdottiBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(self.finestra))

    # pulsante leftMenu, porta alla schermata home del cliente priorietario
    def homeBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(1)
        finestra.iMieiDatiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.unPushedStyleSheet())

    # pulsante leftMenu, porta alla schermata dei dati del proprio account
    def iMieiDatiBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(2)
        finestra.iMieiDatiBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.unPushedStyleSheet())


    # pulsante leftMenu, porta alla schermata dei propri prodotti
    def iMieiProdottiBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(0)
        finestra.iMieiDatiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.pushedStyleSheet())

    def pushedStyleSheet(self):
        #style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; border-top-left-radius: 25px;}"
        return style

    def unPushedStyleSheet(self):
        #style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; border-top-left-radius: 25px;}"
        return style
