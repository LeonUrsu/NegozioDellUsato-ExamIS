import os

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem, QPushButton
from PySide6.QtGui import QCursor

from Database.PathDatabase import PathDatabase
from MVC.controller.Controller import Controller


class UserView():

    def __init__(self, mainPath):
        loader = QUiLoader()
        path = os.path.join(PathDatabase().mainDirPath, "resourcesForUsatoBeato/UserViews", "UserView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        catList = Controller().recuperaListaCategorie()
        self.caricaUserProdottiView(mainPath, catList)

    # Metodo che crea un bottone grazie al idProdotto
    # mainPath = path del main
    # prodotto da usare per caricare dati
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, prodotto):
        prod = prodotto
        button = QPushButton()
        button.setText("Visualizza")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(lambda: self.caricainfoProdottoView(mainPath, "infoProdottoClienteView.ui", prod))
        return button

    # Metodo per caricare i dati di un prodotto nella view
    # mainPath = path del main
    # fileName = nome del file da caricare
    # prodottoTrovato = prodotto da utilizzare per i dati
    def caricainfoProdottoView(self, mainPath, fileName, prodottoTrovato):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeProdottoDaIns.setText(prodottoTrovato.nomeProdotto)
        obj.prezzoCorrenteDaIns.setText(prodottoTrovato.prezzoCorrente)
        obj.prezzoOriginaleDaIns.setText(prodottoTrovato.prezzoOriginale)
        obj.dataDiEsposizioneDaIns.setText(f"{prodottoTrovato.dataEsposizione}")
        obj.dataDiScadenzaDaIns.setText(f"{prodottoTrovato.dataScadenza}")
        obj.idProdottoDaIns.setText(f"{prodottoTrovato.idProdotto}")
        obj.idScaffaleDaIns.setText(f"{prodottoTrovato.nomeScaffale}")
        obj.nomeCategoriaDaIns.setText(f"{prodottoTrovato.nomeCategoria}")
        obj.indietroBtn.clicked.connect(lambda: self.caricaUserProdottiView(mainPath, None))

    # Metodo che cerca il prodotto in base al nome passato e alle opzion scelte nella tendina
    # mainPath = path del main
    # fileName = nome del file da caricare
    # obj = view da utilizzare per caricare i dati
    def cercaProdottoBtnClicked(self, mainPath, obj):
        textData = str(obj.filtraPerData.currentIndex())
        textPrezzo = str(obj.filtraPerPrezzo.currentIndex())
        textCategoria = str(obj.filtraPerCategoria.currentText())
        name = obj.search_le.text()
        listaCorrispondenti = Controller().elaboraCercaProdottoBtnClicked(name, textData, textPrezzo, textCategoria)
        self.caricaUserProdottiView(mainPath, listaCorrispondenti)

    # Metodo che cerca il prodotto in base al nome passato
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    def cercaProdottoBtnClicked(self, mainPath, obj):
        textData = str(obj.filtraPerData.currentIndex())
        textPrezzo = str(obj.filtraPerPrezzo.currentIndex())
        textCategoria = str(obj.filtraPerCategoria.currentText())
        name = obj.search_le.text()
        listaCorrispondenti = Controller().elaboraCercaProdottoBtnClicked(name, textData, textPrezzo, textCategoria)
        self.caricaUserProdottiView(mainPath, listaCorrispondenti)

    # Metodo che recupera i nomi delle categorie presenti nella comboBox
    # obj = view da utilizzare per caricare i dati
    def getITemsOfComboboxOfCategoria(self, obj):
        return [obj.filtraPerData.itemText(i) for i in range(obj.filtraPerData.count())]

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    # item = oggetto nuovo da caricare nel CentralWidget
    def removeAndAdd(self, item):
        try:
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    # Metodo che carica la vista della view del User con i prodotti disponibili
    # mainPath = path del main
    # lista = lista di prodotti da caricare nella view
    def caricaUserProdottiView(self, mainPath, lista):
        obj = self.caricaView(mainPath, "UserViewProdotti.ui")
        self.removeAndAdd(obj)
        self.aggiungiProdottiAllaTab(mainPath, obj, lista)
        self.setItemsOfComboboxCategorie(obj)
        obj.cercaBtn.clicked.connect(lambda: self.cercaProdottoBtnClicked(mainPath, obj))

    # Metodo che grazie alle categorie che ci sono in dataBase si aggiungono alla tendina
    # obj = view da utilizzare per caricare i dati
    def setItemsOfComboboxCategorie(self, obj):
        categorie = Controller().recuperaListaCategorie()
        for cat in categorie:
            obj.filtraPerCategoria.addItem(cat.nome)
        self.categorieList = categorie

    # Metodo che carica una view presente nella UserViews grazie al nome passato
    # mainPath = path del main
    # name = file da caricare
    def caricaView(self, mainPath, fileName):
        loader = QUiLoader()
        path = os.path.join(mainPath,"resourcesForUsatoBeato/UserViews", fileName)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    # mainPath = path del main
    # lista = lista di oggetti da caricare nella tab
    # obj = view da utilizzare per caricare i dati
    def aggiungiProdottiAllaTab(self, mainPath, obj, lista):
        if lista == None:
            lista = Controller().recuperaListaProdottiInVendita()
        objList = ("Nome", "Prezzo", "ID Prodotto", "Data di scadenza", "Click Su Visualizza")
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
            obj.tab.resizeRowsToContents()
            row += 1
