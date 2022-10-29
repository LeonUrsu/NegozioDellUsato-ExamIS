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
        obj.aggiungiProdottoBtn.clicked.connect(
            lambda: amministratore.aggiungiProdottoBtnClicked(mainPath, amministratore))

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

    def aggiungiProdottoBtnClicked(self, mainPath, amministratore):
        name = "inserisciProdottoView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.saveBtn.clicked.connect(lambda: self.saveBtnClicked(mainPath, obj, amministratore))
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore))

    def saveBtnClicked(self, mainPath, obj, amministratore):
        # QLineEdit.text()
        nomeLe = obj.nomeLe.text()
        idAccountLe = obj.idAccountLe
        prezzoLe = obj.prezzoLe
        idCategoriaLe = obj.idCategoriaLe
        idScaffaleLe = obj.idScaffaleLe
        #TODO salvataggio nel sistema del prodotto e il relativo controllo dell'input
        self.prodottiBtnClicked(mainPath, amministratore)

    def pushedStyleSheet(self):
        # style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; border-top-left-radius: 15px; border-bottom-left-radius: 15px}"
        return style

    def unPushedStyleSheet(self):
        # style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; border-top-left-radius: 25px; border-bottom-left-radius: 25px;}"
        return style

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    def removeAndAdd(self, item):
        try:
            self.finestra.verticalLayout_toPaste.itemAt(0).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "AdminButtonsViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra
