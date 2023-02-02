import os
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidgetItem, QPushButton
from PySide6.QtGui import QCursor

from Database.PathDatabase import PathDatabase
from MVC.controller.Controller import Controller
from MVC.model.SistemService.Logging import Logging


class ClienteProprietarioView():
    def __init__(self, mainPath):
        # super().__init__()
        loader = QUiLoader()
        #path = os.path.join(mainPath, "MVC", "view", "../../resourcesForUsatoBeato/ClienteProprietarioViews", "ClienteProprietarioView.ui")
        path = os.path.join(PathDatabase().mainDirPath, "resourcesForUsatoBeato/ClienteProprietarioViews", "ClienteProprietarioView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(mainPath, self.finestra, None))
        self.finestra.iMieiDatiBtn.clicked.connect(lambda: self.iMieiDatiBtnClicked(mainPath, self.finestra))
        self.finestra.iMieiProdottiBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(mainPath, self.finestra))

    # pulsante leftMenu, porta alla schermata home del cliente priorietario
    def homeBtnClicked(self, mainPath, finestra, lista):
        name = "ClienteProprietarioViewProdotti.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        if lista == None:
            lista = Controller().recuperaListaProdottiInVendita()
        self.aggiungiProdottiAllaTab(mainPath, obj.tab, lista)
        self.setItemsOfComboboxCategorie(obj)
        obj.cercaBtn.clicked.connect(lambda: self.cercaProdottoBtnClicked(mainPath, obj))
        if Logging.accountLoggato != None: pass
        finestra.iMieiDatiBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo che cerca il prodotto in base al nome passato e alle opzioni scelte nella tendina
    def cercaProdottoBtnClicked(self, mainPath, obj):
        textData = str(obj.filtraPerData.currentText())
        textPrezzo = str(obj.filtraPerPrezzo.currentText())
        textCategoria = str(obj.filtraPerCategoria.currentText())
        name = obj.search_le.text()
        listaCorrispondenti = Controller().elaboraCercaProdottoBtnClicked(name, textData, textPrezzo, textCategoria)
        self.homeBtnClicked(mainPath, self.finestra, listaCorrispondenti)

    # Metodo che grazie alle categorie che ci sono in dataBase si aggiungono alla tendina
    def setItemsOfComboboxCategorie(self, obj):
        categorie = Controller().recuperaListaCategorie()
        for cat in categorie:
            obj.filtraPerCategoria.addItem(cat.nome)
        self.categorieList = categorie

    # pulsante leftMenu, porta alla schermata dei dati del proprio account
    def iMieiDatiBtnClicked(self, mainPath, finestra):
        name = "iMieiDatiView.ui" #TODO data di nascita in formato errato da correggere
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        if Logging.accountLoggato != None: self.caricaInfoAccount(obj, Logging.accountLoggato)
        finestra.iMieiDatiBtn.setStyleSheet(self.pushedStyleSheet())
        finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        finestra.iMieiProdottiBtn.setStyleSheet(self.unPushedStyleSheet())

    # pulsante leftMenu, porta alla schermata dei propri prodotti
    def iMieiProdottiBtnClicked(self, mainPath, finestra):
        name = "iMieiProdottiView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        listaInVendita = Controller().recuperaProdottiInVenditaConAccount(Logging.accountLoggato)
        listaScaduti = Controller().recuperaProdottiScadutiConAccount(Logging.accountLoggato)
        listaVenduti = Controller().recuperaProdottiVendutiConAccount(Logging.accountLoggato)
        if Logging.accountLoggato != None:
            if listaInVendita != None:
                try:
                    self.aggiungiProdottiAllaTab(mainPath, obj.tabInVendita, listaInVendita)
                except:
                    pass
            if listaScaduti != None:
                try:
                    self.aggiungiProdottiAllaTab(mainPath, obj.tabScaduti, listaScaduti)
                except:
                    pass
            if listaVenduti != None:
                try:
                    self.aggiungiProdottiAllaTab(mainPath, obj.tabVenduti, listaVenduti)
                except:
                    pass



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

    # Metodo che carica una view presente nelle AdminButtonsViews grazie al nome passato
    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "view", "../../resourcesForUsatoBeato/ClienteProprietarioViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    # item = oggetto nuovo da caricare nel CentralWidget
    def removeAndAdd(self, item):
        try:
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    # Metodo che carica i dati da un account nella view
    def caricaInfoAccount(self, obj, account):
        obj.nomeDaIns.setText(account.nome)
        obj.cognomeDaIns.setText(account.cognome)
        obj.dataDiNascitaDaIns.setText(f"{account.dataDiNascita}")
        obj.idAccountDaIns.setText(f"{account.idAccount}")

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    def aggiungiProdottiAllaTab(self, mainPath, tab, lista):
        if lista == None:  # TODO mettere aumento del height
            return
        objList = ("Nome", "Prezzo", "ID", "Data", "Click su Visualizza")
        column = len(objList)
        tab.setColumnCount(column)
        for i in range(column):
            tab.setColumnWidth(i, 120)
        tab.setHorizontalHeaderLabels(objList)
        row = 0
        tab.setRowCount(len(lista))
        for prodotto in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            tab.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{prodotto.nomeProdotto}"))
            tab.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{prodotto.prezzoCorrente}"))
            tab.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{prodotto.idProdotto}"))
            tab.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{prodotto.dataScadenza}"))
            tab.setCellWidget(row, 4, self.creaBottoneVisualizzaProdottoQualsiasi(mainPath, prodotto))
            tab.resizeRowsToContents()
            row += 1

    # Metodo per creare un bottone dinamicamente e iserirlo nella tab
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, prodotto):
        button = QPushButton()
        button.setText("Visualizza")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(
            lambda: self.caricainfoProdottoView(mainPath, "infoProdottoClienteProprietarioView.ui", prodotto))
        return button

    def caricainfoProdottoView(self, mainPath, fileName, prodottoTrovato):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeProdottoDaIns.setText(prodottoTrovato.nomeProdotto)
        obj.prezzoCorrenteDaIns.setText(str(prodottoTrovato.prezzoCorrente))
        obj.prezzoOriginaleDaIns.setText(str(prodottoTrovato.prezzoOriginale))
        obj.dataDiEsposizioneDaIns.setText(f"{prodottoTrovato.dataEsposizione}")
        obj.dataDiScadenzaDaIns.setText(f"{prodottoTrovato.dataScadenza}")
        obj.idProdottoDaIns.setText(f"{prodottoTrovato.idProdotto}")
        obj.idScaffaleDaIns.setText(f"{prodottoTrovato.nomeScaffale}")
        obj.nomeCategoriaDaIns.setText(f"{prodottoTrovato.nomeCategoria}")
        obj.indietroBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(mainPath, self.finestra))
