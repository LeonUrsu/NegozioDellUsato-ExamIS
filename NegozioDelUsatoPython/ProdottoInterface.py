

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from datetime import date

from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5 import QtCore
from PySide2 import *
from MVC.Model.Attività.Amministratore import Amministratore


class ProdottoInterface(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # metodo per aggiungere prodotto alla table nella view
        """ def aggiungiProdottoTramiteApp(self,dict):
        
        idAccount = self.ui.idAccountLe.text()
        idCategoria = self.ui.idCategoriaLe.text()
        prezzo = self.ui.prezzoLe.text()
        idScaffale = self.ui.idScaffaleLe.text()
        Amministratore().inserisciProdotto(dict["idCategoria"], date.today(), "idAccount", "nome", "prezzo", ["idScaffale"])
        """
    def test(self, nome):
        nome.text()
        print(nome.str)



    def inserisciProdottiTableWidget(self,tabella):

        prodottiList = Amministratore().visualizzaProdotti()
        currentRow = 0
        for prodotto in prodottiList:
            tabella.insertRow(currentRow)
            tabella.setItem(currentRow, 0, QtWidgets.QTableWidgetItem(prodotto.nomeProdotto))
            tabella.setItem(currentRow, 1, QtWidgets.QTableWidgetItem(prodotto.idProdotto))
            tabella.setItem(currentRow, 2, QtWidgets.QTableWidgetItem(prodotto.nomeProdotto))
            #self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(QtGui.QCheckBox()))
            currentRow = currentRow+1


    def inserisciRiga(self,tabella):
        row = tabella.rowCount()
        tabella.insertRow(row)
