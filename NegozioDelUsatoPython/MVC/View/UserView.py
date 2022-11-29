import os
import pathlib

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem, QPushButton

from MVC.Controller.Controller import Controller


class UserView():

    def __init__(self, mainPath):
        # super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "UserView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.caricaUserProdottiView(mainPath)
        # self.aggiungiProdottiAllaTab(mainPath, self.finestra)
        # self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(self.finestra))
        # self.finestra.iMieiProdottiBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(self.finestra))

    # Metodo che crea un bottone grazie al idProdotto
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, prodotto):
        prod = prodotto  # TODO anche in admin si puo fare in qursto modo per risparmiare velocità, si potrebbe  modificare admin per avere un'ereditarietà
        button = QPushButton()
        button.setText("Visualizza")
        button.clicked.connect(lambda: self.caricaifoProdottoView(mainPath, "infoProdottoClienteView.ui", prod))
        return button

    def caricaifoProdottoView(self, mainPath, fileName, prodotto):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        # TODO caricare una nuova view delle indo del prodotto, qui andrà rimossa anche la vecchia view removeAndAdd
        self.finestra.indietroBtn.clicked.connect(lambda: self.caricaUserProdottiView(mainPath))

    def removeAndAdd(self, item):
        try:
            # print(f"{self.finestra.verticalLayout_toPaste.count()}")
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    def caricaUserProdottiView(self, mainPath):
        obj = self.caricaView(mainPath, "UserViewProdotti.ui")
        self.removeAndAdd(obj)
        self.aggiungiProdottiAllaTab(mainPath, obj)


    # Metodo che carica una view presente nella UserViews grazie al nome passato
    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "UserViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    # TODO impelmentare un menìtodo simile anche in admin, sembra più efficiente
    def aggiungiProdottiAllaTab(self, mainPath, obj):
        lista = Controller().recuperaListaProdottiInVendita()
        objList = ("nome", "prezzo", "id prodotto", "data scadenza", "click su visualizza")
        column = len(objList)
        obj.tab.setColumnCount(column)
        for i in range(column):
            obj.tab.setColumnWidth(i, 120)
        obj.tab.setHorizontalHeaderLabels(objList)
        row = 0
        obj.tab.setRowCount(len(lista))
        for prodotto in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            obj.tab.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{prodotto.nomeProdotto}"))
            obj.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{prodotto.prezzoCorrente}"))
            obj.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{prodotto.idProdotto}"))
            obj.tab.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{prodotto.dataScadenza}"))
            obj.tab.setCellWidget(row, 4,
                                  self.creaBottoneVisualizzaProdottoQualsiasi(mainPath, prodotto))
            row += 1
