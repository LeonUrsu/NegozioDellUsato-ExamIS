import os
import pathlib

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem, QPushButton

from MVC.Controller.Controller import Controller


class UserView():


    def __init__(self, mainPath):
        #super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "UserView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.removeAndAdd(self.caricaClienteProdottiView(mainPath))
        #self.aggiungiProdottiAllaTab(mainPath, self.finestra)
        #self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(self.finestra))
        #self.finestra.iMieiProdottiBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(self.finestra))

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    def aggiungiProdottiAllaTab(self, mainPath, obj):
        lista = Controller().recuperaListaProdottiInVendita()
        objList = {"nome", "prezzo", "id prodotto", "data scadenza", "click su visualizza"}
        column = len(objList)
        obj.tab.setColumnCount(column)
        for i in range(column):
            obj.tab.setColumnWidth(i, 120)
        obj.tab.setHorizontalHeaderLabels((objList[0], objList[1], objList[2], objList[3], objList[4]))
        row = 0
        obj.tab.setRowCount(len(lista))
        for prodotto in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            #obj.tab.setItem(row, 0, chkBoxItem)
            obj.tab.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{prodotto.nomeProdotto}"))
            obj.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{prodotto.prezzoCorrente}"))
            obj.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{prodotto.idProdotto}"))
            obj.tab.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{prodotto.dataScadenza}"))
            obj.tab.setCellWidget(row, 4,
                                  self.creaBottoneVisualizzaProdottoQualsiasi(mainPath, prodotto.idProdotto, lista))
            row += 1

    # Metodo che crea un bottone grazie al idProdotto
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, idProdotto, lista):
        button = QPushButton()
        button.setText("Visualizza")
        button.clicked.connect(lambda: self.caricaifoProdottoView(mainPath, "infoProdottoPerClienteView.ui",
                                Controller().trovaProdottoTramiteId(idProdotto), lista))
        return button

    def caricaifoProdottoView(self, mainPath, prodotto):
        pass

    def caricaClienteProdottiView(self, mainPath, obj):
        filename = "UserViewProdotti.ui"

        # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A

    def removeAndAdd(self, item):
        try:
            # print(f"{self.finestra.verticalLayout_toPaste.count()}")
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)



