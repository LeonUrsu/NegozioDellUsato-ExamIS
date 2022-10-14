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
        self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(self.finestra))
        self.finestra.statisticheBtn.clicked.connect(lambda: self.statisticheBtnClicked(self.finestra))
        self.finestra.prodottiBtn.clicked.connect(lambda: self.prodottiBtnClicked(self.finestra))
        self.finestra.accountsBtn.clicked.connect(lambda: self.accountsBtnClicked(self.finestra))
        self.finestra.backupBtn.clicked.connect(lambda: self.backupBtnClicked(self.finestra))

    # Metodo per cambiare al pulsante il colore dopo premuto
    def homeBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(1)
        finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def statisticheBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(1)
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.statisticheBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def prodottiBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(1)
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.prodottiBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def accountsBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(1)
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.accountsBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
    def backupBtnClicked(self, finestra):
        finestra.finestreSecondarie.setCurrentIndex(1)
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.backupBtn.setStyleSheet(self.pushedStyleSheet())

    def pushedStyleSheet(self):
        # style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; border-top-left-radius: 25px;}"
        return style

    def unPushedStyleSheet(self):
        # style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; border-top-left-radius: 25px;}"
        return style
