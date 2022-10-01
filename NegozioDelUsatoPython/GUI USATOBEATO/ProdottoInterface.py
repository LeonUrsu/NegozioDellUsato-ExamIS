

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PySide2 import *
from datetime import date

from PySide2 import QtCore

from MVC.Model.Attività.Amministratore import Amministratore
from ui_interface_definitiva import Ui_MainWindow


class ProdottoInterface(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # metodo per aggiungere prodotto alla table nella view
    def aggiungiProdottoTramiteApp(self):
        nome = self.ui.nomeLe.text()
        idAccount = self.ui.idAccountLe.text()
        idCategoria = self.ui.idCategoriaLe.text()
        prezzo = self.ui.prezzoLe.text()
        idScaffale = self.ui.idScaffaleLe.text()
        Amministratore().inserisciProdotto(idCategoria, date.today(), idAccount, nome, prezzo, idScaffale)

    def inserisciProdottiTableWidget(self):
        row = 0
        prodottiList = Amministratore().visualizzaProdotti()

        for prodotto in prodottiList:
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(prodotto.prezzo))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(prodotto.idProdotto))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(prodotto.nomeProdotto))
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tableWidget.setItem(row, 0, chkBoxItem)
            row = row + 1
