import os

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class ClienteProprietarioView():
    def __init__(self, mainPath):
        # super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "ClienteProprietarioView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(mainPath, self.finestra))
        self.finestra.iMieiDatiBtn.clicked.connect(lambda: self.iMieiDatiBtnClicked(mainPath, self.finestra))
        self.finestra.iMieiProdottiBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(mainPath, self.finestra))

    # pulsante leftMenu, porta alla schermata home del cliente priorietario
    def homeBtnClicked(self, mainPath, finestra):
        name = "homeView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        # TODO
        finestra.iMieiDatiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.unPushedStyleSheet())

    # pulsante leftMenu, porta alla schermata dei dati del proprio account
    def iMieiDatiBtnClicked(self, mainPath, finestra):
        name = "iMieiDatiView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        # TODO
        finestra.iMieiDatiBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.unPushedStyleSheet())

    # pulsante leftMenu, porta alla schermata dei propri prodotti
    def iMieiProdottiBtnClicked(self, mainPath, finestra):
        name = "iMieiProdottiView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        # TODO
        finestra.iMieiDatiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.pushedStyleSheet())

    def pushedStyleSheet(self):
        # style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; " \
                "border-top-left-radius: 15px; border-bottom-left-radius: 15px}"
        return style

    def unPushedStyleSheet(self):
        # style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; " \
                "border-top-left-radius: 25px; border-bottom-left-radius: 25px;}"
        return style

    # TODO fare metodo che aggiunge i prodotti posseduti dal cliente proprietario
    # TODO fare metrodo per usare le tendine dei filtri nel cliente e amministratore

    # Metodo che carica una view presente nelle AdminButtonsViews grazie al nome passato
    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "ClienteProprietarioViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    def removeAndAdd(self, item):
        try:
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)