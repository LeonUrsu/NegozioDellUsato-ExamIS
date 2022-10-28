import os

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget


class AmministratoreView(QWidget):
    def __init__(self, mainPath):
        super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "AmministratoreView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()

    # Metodo per cambiare al pulsante il colore dopo premuto
    def homeBtnClicked(self, mainPath, amministratore):
        name = "homeView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def statisticheBtnClicked(self, mainPath, amministratore):
        name = "statisticheView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def prodottiBtnClicked(self, mainPath, amministratore):
        name = "prodottiView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def accountsBtnClicked(self, mainPath, amministratore):
        name = "accountsView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def backupBtnClicked(self, mainPath, amministratore):
        name = "backupView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.pushedStyleSheet())

    def pushedStyleSheet(self):
        # style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; border-top-left-radius: 15px; border-bottom-left-radius: 15px}"
        return style

    def unPushedStyleSheet(self):
        # style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; border-top-left-radius: 25px; border-bottom-left-radius: 25px;}"
        return style

    def removeAndAdd(self, item):
        for i in range(self.finestra.verticalLayout_toPaste.count()):
            self.finestra.verticalLayout_toPaste.itemAt(i).widget().deleteLater()
        self.finestra.verticalLayout_toPaste.addWidget(item)

    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "AdminButtonsViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra
