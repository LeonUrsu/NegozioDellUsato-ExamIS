import os
from datetime import datetime
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtGui import QCursor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QPushButton
from MVC.Controller.Controller import Controller



class AmministratoreView(QWidget):
    def __init__(self, mainPath):
        super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "AmministratoreView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    # mainPath = path del main
    # amministratore = oggetto AmministratoreView
    def statisticheBtnClicked(self, mainPath, amministratore):
        name = "statisticheView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.statisticheBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        stats = Controller().trovaUltimeStatistiche()
        if stats != None:
            try:
                obj.guadagnoTotaleLabel.setText(str(stats.prodottiVendutiTotali))
            except:
                pass
            try:
                obj.prodottiVendutiLabel.setText(str(stats.guadagnoTotale))
            except:
                pass
            try:
                obj.clientiProprietariLabel.setText(str(stats.numeroClientiProprietari))
            except:
                pass
            try:
                obj.cat1.setText(f"{stats.nomePrimaCategoriaTendenza} - n:{stats.numeroPrimaCategoriaTendenza}")
            except:
                pass
            try:
                obj.cat2.setText(f"{stats.nomeSecondaCategoriaTendenza} - n:{stats.numeroSecondaCategoriaTendenza}")
            except:
                pass
            try:
                obj.cat3.setText(f"{stats.nomeTerzaCategoriaTendenza} - n:{stats.numeroTerzaCategoriaTendenza}")
            except:
                pass

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    # mainPath = path del main
    # lista = lista con prodotti da caricare nella tab
    # amministratore = oggetto AmministratoreView
    def prodottiBtnClicked(self, mainPath, amministratore, lista):
        obj = self.caricaView(mainPath, "prodottiView.ui")
        self.removeAndAdd(obj)
        self.setItemsOfComboboxCategorie(obj)
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        if lista == None:
            lista = Controller().recuperaListaProdottiInVendita()
        self.aggiungiProdottiAllaTab(mainPath, obj, amministratore, lista)
        obj.aggiungiBtn.clicked.connect(lambda: amministratore.aggiungiProdottoBtnClicked(mainPath, amministratore))
        obj.rimuoviBtn.clicked.connect(lambda: amministratore.rimuoviProdottoBtnClicked(mainPath, amministratore, obj))
        obj.vendiBtn.clicked.connect(lambda: amministratore.vendiProdottoBtnClicked(mainPath, amministratore, obj))
        obj.cercaBtn.clicked.connect(lambda: amministratore.cercaProdottoBtnClicked(mainPath, amministratore, obj))

    # Metodo che grazie alle categorie che ci sono in dataBase si aggiungono alla tendina
    # obj = view caricata
    def setItemsOfComboboxCategorie(self, obj):
        categorie = Controller().recuperaListaCategorie()
        for cat in categorie:
            obj.filtraPerCategoria.addItem(cat.nome)
        self.categorieList = categorie

    # Metodo che cerca il prodotto in base al nome passato
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    def cercaProdottoBtnClicked(self, mainPath, amministratore, obj):
        textData = str(obj.filtraPerData.currentIndex())
        textPrezzo = str(obj.filtraPerPrezzo.currentIndex())
        textCategoria = str(obj.filtraPerCategoria.currentText())
        name = obj.search_le.text()
        listaCorrispondenti = Controller().elaboraCercaProdottoBtnClicked(name, textData, textPrezzo, textCategoria)
        self.prodottiBtnClicked(mainPath, amministratore, listaCorrispondenti)

    # Metodo che elimina gli oggetti nel database tramite la lista id
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    def rimuoviProdottoBtnClicked(self, mainPath, amministratore, obj):
        listaId = list()
        for box in range(obj.tab.rowCount()):
            if obj.tab.item(box, 0).checkState() == QtCore.Qt.Checked:
                listaId.append(int(obj.tab.item(box, 3).text()))
        Controller().eliminaProdottiTramiteListaId(listaId)
        self.prodottiBtnClicked(mainPath, amministratore, None)

    # Metodo che vende i prodotti selezionati nella lista dei prodotti
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    def vendiProdottoBtnClicked(self, mainPath, amministratore, obj):
        listaId = list()
        for box in range(obj.tab.rowCount()):
            if obj.tab.item(box, 0).checkState() == QtCore.Qt.Checked:
                listaId.append(int(obj.tab.item(box, 3).text()))
        ricevuta = Controller().vendiProdottiTramiteListaId(listaId)
        self.prodottiBtnClicked(mainPath, amministratore, None)
        self.aperturaRicevuta(mainPath, amministratore, ricevuta)

    # Metodo per gestire l'apertura di una view per inserirci i dati della ricevuta
    # mainPath = path del main
    # amministratore = oggetto AmministratoreView
    # ricevuta = ricevuta da essere usata per caricare i dati dei prodotti venduti
    def aperturaRicevuta(self, mainPath, amministratore, ricevuta):
        name = "ricevutaUsatoBeato.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.dataDaIns.setText(f"{datetime.today()}")
        lista = ricevuta.prodotti
        if lista == None:
            return
        objList = ("nome", "prezzo vendita", "id")
        column = len(objList)
        obj.tab.setColumnCount(column)
        for i in range(column):
            obj.tab.setColumnWidth(i, 120)
        obj.tab.setHorizontalHeaderLabels(objList)
        row = 0
        obj.tab.setRowCount(len(lista))
        totale = 0
        for prodotto in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            obj.tab.setItem(row, 0, QtWidgets.QTableWidgetItem(prodotto["nomeProdotto"]))
            obj.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(prodotto["prezzoCorrente"]))
            obj.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(prodotto["idProdotto"]))
            totale += int(prodotto["prezzoCorrente"])
            obj.tab.resizeRowsToContents()
            row += 1
        obj.totaleDaIns.setText(f"{totale}")
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore, None))

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    # mainPath = path del main
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def accountsBtnClicked(self, mainPath, amministratore, lista):
        name = "accountsView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        if lista == None:
            lista = Controller().recuperaListaAccounts()
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        self.aggiungiAccountsAllaTab(mainPath, obj, amministratore, lista)
        obj.aggiungiBtn.clicked.connect(lambda: amministratore.aggiungiClienteBtnClicked(mainPath, amministratore))
        obj.rimuoviBtn.clicked.connect(lambda: amministratore.rimuoviClienteBtnClicked(mainPath, obj, amministratore))
        obj.cercaBtn.clicked.connect(lambda: amministratore.cercaClienteBtnClicked(mainPath, obj, amministratore))

    # Metodo che gestisce la ricerca di in cliente nella view
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def cercaClienteBtnClicked(self, mainPath, obj, amministratore):
        textNome = obj.nome_le.text()
        textCognome = obj.cognome_le.text()
        lista = Controller().filtraClienti(textNome, textCognome)
        self.accountsBtnClicked(mainPath, amministratore, lista)

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    # mainPath = path del main
    # amministratore = oggetto AmministratoreView
    def backupBtnClicked(self, mainPath, amministratore):
        name = "backupView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.pushedStyleSheet())
        obj.pushButton.clicked.connect(lambda: self.effettuaBackup(obj))

    # Metodo per effettuare il backup dei dati
    # obj = view caricata
    def effettuaBackup(self, obj):
        Controller().effettuaBackup()
        obj.stato.setText("Backup eseguito")

    # Metodo che si attiva alla pressione del prodottiBtn
    # mainPath = path del main
    # amministratore = oggetto AmministratoreView
    def aggiungiProdottoBtnClicked(self, mainPath, amministratore):
        name = "inserisciProdottoView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.aggiungiBtn.clicked.connect(lambda: self.saveProdottoBtnClicked(mainPath, obj, amministratore))
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore, None))

    # Metodo che si attiva alla pressione del aggiungiBtn
    # mainPath = path del main
    # amministratore = oggetto AmministratoreView
    def aggiungiClienteBtnClicked(self, mainPath, amministratore):
        name = "inserisciClienteView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.aggiungiBtn.clicked.connect(lambda: self.saveClienteBtnClicked(mainPath, obj, amministratore))
        obj.indietroBtn.clicked.connect(lambda: self.accountsBtnClicked(mainPath, amministratore, None))

    # Metodo che rimuove account dal database del sistema e si attiva alla pressione di rimuoviBtn
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def rimuoviClienteBtnClicked(self, mainPath, obj, amministratore):
        listaId = list()
        for box in range(obj.tab.rowCount()):
            if obj.tab.item(box, 0).checkState() == QtCore.Qt.Checked:
                listaId.append(int(obj.tab.item(box, 3).text()))
        Controller().eliminaAccountTramiteListaId(listaId)
        self.accountsBtnClicked(mainPath, amministratore, None)

    # Metodo che si attiva alla pressione del aggiungiProdottoBtn
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    def saveProdottoBtnClicked(self, mainPath, obj, amministratore):
        nomeLe = obj.nomeLe.text()
        idAccountLe = obj.idAccountLe.text()
        prezzoLe = obj.prezzoLe.text()
        nomeCategoriaLe = obj.nomeCategoriaLe.text()
        nomeScaffaleLe = obj.nomeScaffaleLe.text()
        if self.checkerSaveProdottoBtnClicked(nomeLe, idAccountLe, prezzoLe, nomeCategoriaLe):
            pass
        else:
            self.prodottiBtnClicked(mainPath, amministratore, None)
        Controller().amministratoresaveProdottoBtn(datetime.today(), idAccountLe, nomeLe, prezzoLe, nomeScaffaleLe,
                                                   nomeCategoriaLe)
        self.prodottiBtnClicked(mainPath, amministratore, None)

    # Metodo che si attiva alla pressione del saveClienteBtn
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    def saveClienteBtnClicked(self, mainPath, obj, amministratore):
        nomeLe = obj.nomeLe.text()
        cognomeLe = obj.cognomeLe.text()
        dataNascitaLe = obj.dataNascitaLe.text()
        emailLe = (obj.emailLe.text()).lower()
        passwordLe = obj.passwordLe.text()
        telefonoLe = obj.telefonoLe.text()
        capLe = obj.capLe.text()
        cittaLe = obj.cittaLe.text()
        viaLe = obj.viaLe.text()
        piazzaLe = obj.piazzaLe.text()
        civicoLe = obj.civicoLe.text()
        citofonoLe = obj.citofonoLe.text()
        if self.checkerSaveClienteBtnClicked(nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                                             citofonoLe, viaLe, piazzaLe, civicoLe, citofonoLe):
            pass
        else:
            self.accountsBtnClicked(mainPath, amministratore, None)
            return
        Controller().saveCLienteBtnClicked(nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                                           cittaLe, viaLe, piazzaLe, civicoLe, citofonoLe)
        self.accountsBtnClicked(mainPath, amministratore, None)

    # Metodo che restitiusce la stringa nel metodo
    def pushedStyleSheet(self):
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; " \
                "border-top-left-radius: 15px; border-bottom-left-radius: 15px}"
        return style

    # Metodo che restitiusce la stringa nel metodo
    def unPushedStyleSheet(self):
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; " \
                "border-top-left-radius: 25px; border-bottom-left-radius: 25px;}"
        return style

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    # item = oggetto nuovo da caricare nel CentralWidget
    def removeAndAdd(self, item):
        try:
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    # Metodo che carica una view presente nelle AdminButtonsViews grazie al nome passato
    # mainPath = path del main
    # name = nome del file da caricare
    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "AdminButtonsViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra

    # Metodo che aggiunge i prodotti in vendita al tableWidget della finestra
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def aggiungiProdottiAllaTab(self, mainPath, obj, amministratore, lista):
        if lista == None:
            lista = Controller().recuperaListaProdottiInVendita()
        objList = (None, "Nome", "Prezzo", "ID Prodotto", "Data di Scadenza", "Click Su Visualizza")
        column = len(objList)
        obj.tab.setColumnCount(column)
        obj.tab.setColumnWidth(0, 15)
        for i in range(column):
            obj.tab.setColumnWidth(i + 1, 100)
        obj.tab.setHorizontalHeaderLabels(objList)
        row = 0
        obj.tab.setRowCount(len(lista))
        for prodotto in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            obj.tab.setItem(row, 0, chkBoxItem)
            obj.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{prodotto.nomeProdotto}"))
            obj.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{prodotto.prezzoCorrente}"))
            obj.tab.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{prodotto.idProdotto}"))
            obj.tab.setItem(row, 4, QtWidgets.QTableWidgetItem(prodotto.dataScadenza.strftime("%Y-%m-%d %H:%M:%S")))
            obj.tab.setCellWidget(row, 5,
                                  self.creaBottoneVisualizzaProdottoQualsiasi(mainPath, prodotto.idProdotto,
                                                                              amministratore, lista))
            obj.tab.resizeRowsToContents()
            row += 1

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def aggiungiAccountsAllaTab(self, mainPath, obj, amministratore, lista):
        colonne = 6
        obj.tab.setColumnCount(colonne)
        obj.tab.setColumnWidth(0, 15)
        for i in range(colonne):
            obj.tab.setColumnWidth(i + 1, 100)
        obj.tab.setHorizontalHeaderLabels((None, "nome", "cognome", "id account", "email", "click su visualizza"))
        row = 0
        obj.tab.setRowCount(len(lista))
        for account in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            obj.tab.setItem(row, 0, chkBoxItem)
            obj.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(account.nome))
            obj.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(account.cognome))
            obj.tab.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{account.idAccount}"))  # serve solo per fare int a str
            obj.tab.setItem(row, 4, QtWidgets.QTableWidgetItem(account.email))
            obj.tab.setCellWidget(row, 5,
                                  self.creaBottoneVisualizzaAccountQualsiasi(mainPath, account.idAccount,
                                                                             amministratore, lista))
            obj.tab.resizeRowsToContents()
            row += 1

    # Metodo che crea un bottone grazie al idProdotto
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, idProdotto, amministratore, lista):
        button = QPushButton()
        button.setText("Visualizza")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(lambda: self.caricainfoProdottoView(mainPath, "infoProdottoView.ui",
                                                                   Controller().trovaProdottoTramiteId(idProdotto),
                                                                   amministratore, lista))

        return button

    # Metodo che crea un bottone grazie al idAccount
    # mainPath = path del main
    # obj = view caricata
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def creaBottoneVisualizzaAccountQualsiasi(self, mainPath, idAccount, amministratore, lista):
        button = QPushButton()
        button.setText("Visualizza")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(lambda: self.caricainfoAccountView(mainPath, "infoaccountView.ui",
                                                                  Controller().trovaAccountTramiteId(idAccount),
                                                                  amministratore, lista))
        return button

    # Metodo che carica le info di un prodotto all'interno della View
    def caricainfoProdottoView(self, mainPath, fileName, prodottoTrovato, amministratore, lista):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeProdottoDaIns.setText(prodottoTrovato.nomeProdotto)
        obj.prezzoCorrenteDaIns.setText(prodottoTrovato.prezzoCorrente)
        obj.prezzoOriginaleDaIns.setText(prodottoTrovato.prezzoOriginale)
        obj.dataDiEsposizioneDaIns.setText(prodottoTrovato.dataEsposizione.strftime("%Y-%m-%d %H:%M:%S"))
        obj.dataDiScadenzaDaIns.setText(prodottoTrovato.dataScadenza.strftime("%Y-%m-%d %H:%M:%S"))
        obj.idProdottoDaIns.setText(f"{prodottoTrovato.idProdotto}")
        obj.nomeScaffaleDaIns.setText(f"{prodottoTrovato.nomeScaffale}")
        obj.nomeCategoriaDaIns.setText(f"{prodottoTrovato.nomeCategoria}")
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore, lista))
        obj.aggiornaBtn.clicked.connect(lambda: self.aggiornaProdottoBtnClicked(mainPath, amministratore,
                                                                                prodottoTrovato.idProdotto))

    # Metodo che gestische il caricamento della view per aggiornare il prodotto
    def aggiornaProdottoBtnClicked(self, mainPath, amministratore, idProdotto):
        # self.aggiungiProdottoBtnClicked(mainPath, amministratore)
        name = "aggiornaProdottoView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.aggiornaBtn.clicked.connect(
            lambda: self.confermaAggiornaProdottoBtnClicked(mainPath, obj, amministratore, idProdotto))
        obj.indietroBtn.clicked.connect(lambda: self.caricainfoProdottoView(mainPath, "infoProdottoView.ui",
                                                                            Controller().trovaProdottoTramiteId(
                                                                                idProdotto), amministratore, None))

    # Metodo che si attiva alla conferma dell'aggionramento del prodotto
    def confermaAggiornaProdottoBtnClicked(self, mainPath, obj, amministratore, idProdotto):
        nomeLe = obj.nomeLe.text()
        prezzoLe = obj.prezzoLe.text()
        nomeCategoriaLe = obj.nomeCategoriaLe.text()
        nomeScaffaleLe = obj.nomeScaffaleLe.text()
        Controller().aggiornaProdotto(nomeCategoriaLe, None, nomeLe, prezzoLe, nomeScaffaleLe, idProdotto)
        self.caricainfoProdottoView(mainPath, "infoProdottoView.ui", Controller().trovaProdottoTramiteId(idProdotto),
                                    amministratore, None)

    # Metodo che carica le info di un account all'interno della View
    # mainPath = path del main
    # fileName = nome del file da caricare
    # account = account da cui caricare dati
    # amministratore = oggetto AmministratoreView
    # lista = lista prodotti da aggiungere alla tab
    def caricainfoAccountView(self, mainPath, fileName, account, amministratore, lista):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeDaIns.setText(account.nome)
        obj.cognomeDaIns.setText(account.cognome)
        obj.dataDiNascitaDaIns.setText(account.dataDiNascita.strftime("%Y-%m-%d %H:%M:%S"))
        obj.emailDaIns.setText(account.email)
        obj.passwordDaIns.setText(account.password)
        obj.idAccountDaIns.setText(f"{account.idAccount}")
        obj.numeroTelefonicoDaIns.setText(account.numeroTelefonico)
        obj.cittaDaIns.setText(account.residenza.citta)
        obj.capDaIns.setText(account.residenza.cap)
        obj.citofonoDaIns.setText(account.residenza.citofono)
        obj.viaDaIns.setText(account.residenza.via)
        obj.piazzaDaIns.setText(account.residenza.piazza)
        obj.civicoDaIns.setText(account.residenza.civico)
        obj.indietroBtn.clicked.connect(lambda: self.accountsBtnClicked(mainPath, amministratore, lista))
        obj.aggiornaBtn.clicked.connect(lambda: self.aggiornaAccountBtnClicked(mainPath, amministratore,
                                                                               account.idAccount))

    # Metodo che carica la view per aggiornare l'account e ne gestisce i pulsanti
    def aggiornaAccountBtnClicked(self, mainPath, amministratore, idAccount):
        name = "aggiornaAccountView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.aggiornaBtn.clicked.connect(
            lambda: self.confermaAggiornaAccountBtnClicked(mainPath, obj, amministratore, idAccount))  # TODO
        obj.indietroBtn.clicked.connect(lambda: self.caricainfoAccountView(mainPath, "infoAccountView.ui",
                                                                           Controller().trovaAccountTramiteId(
                                                                               idAccount), amministratore, None))

    # Metodo che si attiva alla conferma dell'aggiornamento del prodotto
    def confermaAggiornaAccountBtnClicked(self, mainPath, obj, amministratore, idAccount):
        nomeLe = obj.nomeLe.text()
        cognomeLe = obj.cognomeLe.text()
        dataDiNascitaLe = obj.dataDiNascitaLe.text()
        emailLe = obj.emailLe.text()
        telefonoLe = obj.telefonoLe.text()
        capLe = obj.capLe.text()
        citofonoLe = obj.citofonoLe.text()
        cittaLe = obj.cittaLe.text()
        viaLe = obj.viaLe.text()
        piazzaLe = obj.piazzaLe.text()
        civicoLe = obj.civicoLe.text()
        Controller().aggiornaAccount(idAccount, nomeLe, cognomeLe, dataDiNascitaLe, emailLe, telefonoLe, capLe, citofonoLe, cittaLe, viaLe, piazzaLe, civicoLe) # TODO
        self.caricainfoAccountView(mainPath, "infoAccountView.ui", Controller().trovaAccountTramiteId(idAccount),
                                   amministratore, None)

    # Metodo per controllare la validità dei dati inseriti dall'utente
    # * = parametri str o datetime da controllare per errori umani
    def checkerSaveProdottoBtnClicked(self, nomeLe, idAccountLe, prezzoLe, nomeCategoriaLe):
        if nomeLe == "": return False
        if not idAccountLe.isalnum(): return False
        if not prezzoLe.isalnum(): return False
        if prezzoLe != "": return False
        if not nomeCategoriaLe == "": return False
        if Controller().checkEsistenzaCategoriaInDatabase(nomeCategoriaLe): return False
        return True

    # Metodo per controllare la validità dei dati inseriti dall'utente]
    # * = parametri str o datetime da controllare per errori umani
    def checkerSaveClienteBtnClicked(self, nomeLe, cognomeLe, dataDiNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                                     cittaLe, viaLe, piazzaLe, civicoLe, citofonoLe):
        if nomeLe == "": return False
        if cognomeLe == "": return False
        if not self.validateDate(dataDiNascitaLe): return False
        if not telefonoLe.isalnum(): return False
        if not capLe.isalnum(): return False
        return True

    # Metodo per validare la data nel formato corretto se è corretta restituisce True, False altrimenti
    def validateDate(self, date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except:
            return False
