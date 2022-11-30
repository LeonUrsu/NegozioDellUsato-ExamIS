import os
import pathlib
import sys
from datetime import datetime

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem, QPushButton
from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
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
        self.caricaUserProdottiView(mainPath, None)

    # Metodo che crea un bottone grazie al idProdotto
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, prodotto):
        prod = prodotto  # TODO anche in admin si puo fare in qusto modo per risparmiare velocità, si potrebbe modificare admin per avere un'ereditarietà
        button = QPushButton()
        button.setText("Visualizza")
        button.clicked.connect(lambda: self.caricaifoProdottoView(mainPath, "infoProdottoClienteView.ui", prod))
        return button

    def caricaifoProdottoView(self, mainPath, fileName, prodottoTrovato):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeProdottoDaIns.setText(prodottoTrovato.nomeProdotto)
        obj.prezzoCorrenteDaIns.setText(prodottoTrovato.prezzoCorrente)
        obj.prezzoOriginaleDaIns.setText(prodottoTrovato.prezzoOriginale)
        obj.dataDiEsposizioneDaIns.setText(f"{prodottoTrovato.dataEsposizione}")
        obj.dataDiScadenzaDaIns.setText(f"{prodottoTrovato.dataScadenza}")
        obj.idProdottoDaIns.setText(f"{prodottoTrovato.idProdotto}")
        obj.idScaffaleDaIns.setText(f"{prodottoTrovato.idScaffale}")
        obj.nomeCategoriaDaIns.setText(f"{prodottoTrovato.nomeCategoria}")
        obj.indietroBtn.clicked.connect(lambda: self.caricaUserProdottiView(mainPath, None))

    # Metodo che cerca il prodotto in base al nome passato e alle opzion scelte nella tendina
    def cercaProdottoBtnClicked(self, mainPath, obj):
        textData = str(obj.filtraPerData.currentText())
        textPrezzo = str(obj.filtraPerPrezzo.currentText())
        textCategoria = str(obj.filtraPerCategoria.currentText())
        listaCorrispondentiData = self.ifFiltraPerDataSelected(textData)
        listaCorrispondentiPrezzo = self.ifFiltraPerPrezzo(textPrezzo)
        listaCorrispondentiCategoria = self.ifFiltraPerCategoria(textCategoria)
        listaCorrispondenti = list()
        for prodottoData in listaCorrispondentiData:
            for prodottoPrezzo in listaCorrispondentiPrezzo:
                for prodottoCategoria in listaCorrispondentiCategoria:
                    if prodottoData.idProdotto == prodottoPrezzo.idProdotto == prodottoCategoria.idProdotto:
                        listaCorrispondenti.append(prodottoData)
        if obj.search_le.text() != "":
            name = obj.search_le.text()
            temp = list()
            for prodotto in listaCorrispondenti:
                if prodotto.nomeProdotto == name:
                    temp.append(prodotto)
            listaCorrispondenti = temp
        self.caricaUserProdottiView(mainPath, listaCorrispondenti)

    # Metodo che filtra i prodotti in base al periodo scelto
    def ifFiltraPerDataSelected(self, textData):
        lista = Controller().recuperaListaProdottiInVendita()
        if textData == "Tutte le date":
            return lista
        elif textData == "ultima settimana":
            lista = Controller().filtraDataEsposizione(datetime.today() - relativedelta(days=7),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "ultimo mese":
            lista = Controller().filtraDataEsposizione(datetime.today() - relativedelta(months=1),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "ultimi tre mesi":
            lista = Controller().filtraDataEsposizione(datetime.today() - relativedelta(months=3),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        return lista

    # Metodo che filtra i prodotti in base al prezzo massimo scelto
    def ifFiltraPerPrezzo(self, textPrezzo):
        lista = Controller().recuperaListaProdottiInVendita()
        if textPrezzo == "tutti i prezzi":
            return lista
        elif textPrezzo == "0€ - 10€ ":
            lista = Controller().filtraPrezzo(0, 10, PathDatabase().inVenditaTxt)
        elif textPrezzo == "10€ - 20€":
            lista = Controller().filtraPrezzo(10, 20, PathDatabase().inVenditaTxt)
        elif textPrezzo == "20€ - 50€":
            lista = Controller().filtraPrezzo(20, 50, PathDatabase().inVenditaTxt)
        elif textPrezzo == ">50€":
            lista = Controller().filtraPrezzo(50, sys.maxsize, PathDatabase().inVenditaTxt)
        return lista

    # Metodo che filtra i prodotti in base alla categoria scelta nella tendina della view
    def ifFiltraPerCategoria(self, textCategoria):
        listaProdotti = Controller().recuperaListaProdottiInVendita()
        if textCategoria == "Tutte le Categorie" or textCategoria == "":
            return listaProdotti
        categoriaIdFiltro = None
        for categoria in self.categorieList:
            if textCategoria == categoria.nome:
                categoriaIdFiltro = categoria.idCategoria
        listaProdottiTrovati = list()
        if categoriaIdFiltro == None: return listaProdotti
        for prodotto in listaProdotti:
            if prodotto.idCategoria == categoriaIdFiltro:
                listaProdottiTrovati.append(prodotto)
        if not listaProdottiTrovati:
            return listaProdotti
        else:
            return listaProdottiTrovati

    # Metodo che recupera i nomi delle categorie presenti nella comboBox
    def getITemsOfComboboxOfCategoria(self, obj):
        return [obj.filtraPerData.itemText(i) for i in range(obj.filtraPerData.count())]

    def removeAndAdd(self, item):
        try:
            # print(f"{self.finestra.verticalLayout_toPaste.count()}")
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    # Metodo che carica la vista della View del User con i prodotti disponibili
    def caricaUserProdottiView(self, mainPath, lista):
        obj = self.caricaView(mainPath, "UserViewProdotti.ui")
        self.removeAndAdd(obj)
        self.aggiungiProdottiAllaTab(mainPath, obj, lista)
        self.setItemsOfComboboxCategorie(obj)
        # TODO filtro per categorie ancora non funzionante
        obj.cercaBtn.clicked.connect(lambda: self.cercaProdottoBtnClicked(mainPath, obj))

    # Metodo che grazie alle categorie che ci sono in dataBase si aggiungono alla tendina
    def setItemsOfComboboxCategorie(self, obj):
        categorie = Controller().recuperaListaCategorie()  # TODO
        for cat in categorie:
            obj.filtraPerCategoria.addItem(cat.nome)
        self.categorieList = categorie

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
    # TODO impelmentare un metodo simile anche in admin, sembra più efficiente
    def aggiungiProdottiAllaTab(self, mainPath, obj, lista):
        if lista == None:
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
