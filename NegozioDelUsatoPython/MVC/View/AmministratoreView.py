import os
import sys
from datetime import datetime
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtGui import QCursor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QPushButton
from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
from MVC.Controller.Controller import Controller
from MVC.Model.Attività.Account import Account


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
    def homeBtnClicked(self, mainPath, amministratore):
        name = "homeView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    def statisticheBtnClicked(self, mainPath, amministratore):
        name = "statisticheView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        stats = Controller().trovaUltimeStatistiche()
        if stats != None:
            obj.guadagnoTotaleLabel.setText(stats.prodottiVendutiTotali)
            obj.prodottiVendutiLabel.setText(stats.guadagnoTotale)
            obj.clientiProprietariLabel.setText(stats.numeroClientiProprietari)
            obj.cat1.setText(stats.tendenzaCategorie[0])
            obj.cat2.setText(stats.tendenzaCategorie[1])
            obj.cat3.setText(stats.tendenzaCategorie[2])

    # Metodo per gestire i pulsanti premuti sul menu sinistroo
    def prodottiBtnClicked(self, mainPath, amministratore, lista):
        name = "prodottiView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
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

    # Metodo che cerca il prodotto in base al nome passato
    def cercaProdottoBtnClicked(self, mainPath, amministratore, obj):
        textData = str(obj.filtraPerData.currentText())
        textPrezzo = str(obj.filtraPerPrezzo.currentText())
        listaCorrispondentiData = self.ifFiltraPerDataSelected(textData)
        listaCorrispondentiPrezzo = self.ifFiltraPerPrezzo(textPrezzo)
        listaCorrispondenti = list()
        for prodottoData in listaCorrispondentiData:
            for prodottoPrezzo in listaCorrispondentiPrezzo:
                if prodottoData.idProdotto == prodottoPrezzo.idProdotto:
                    listaCorrispondenti.append(prodottoData)
        if obj.search_le.text() != "":
            name = obj.search_le.text()
            temp = list()
            for prodotto in listaCorrispondenti:
                if prodotto.nomeProdotto == name:
                    temp.append(prodotto)
            listaCorrispondenti = temp
        self.prodottiBtnClicked(mainPath, amministratore, listaCorrispondenti)

    # Metodo che filtra i prodotti in base al periodo scelto
    def ifFiltraPerDataSelected(self, textData):
        lista = None
        if textData == "Da Sempre":
            lista = Controller().recuperaListaProdottiInVendita()
        elif textData == "Ultima Settimana":
            lista = Controller().filtraDataEsposizione(datetime.today() - relativedelta(days=7),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "Ultimo Mese":
            lista = Controller().filtraDataEsposizione(datetime.today() - relativedelta(months=1),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "Ultimo Trimestre":
            lista = Controller().filtraDataEsposizione(datetime.today() - relativedelta(months=3),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        return lista

    # Metodo che filtra i prodotti in base al prezzo massimo scelto
    def ifFiltraPerPrezzo(self, textPrezzo):
<<<<<<< HEAD
        lista = None
        if textPrezzo == "Tutti i Prezzi":
            lista = Controller().recuperaListaProdottiInVendita()
        elif textPrezzo == "<100€":
            lista = Controller().filtraPrezzo(0, 100, PathDatabase().inVenditaTxt)
        elif textPrezzo == "<50€":
            lista = Controller().filtraPrezzo(0, 50, PathDatabase().inVenditaTxt)
        elif textPrezzo == "<20€":
            lista = Controller().filtraPrezzo(0, 20, PathDatabase().inVenditaTxt)
=======
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
>>>>>>> 8d81679bbb23c26ab392c4da9a708fbd648e8cca
        return lista

    # Metodo che elimina gli oggetti nel database tramite la lista id
    def rimuoviProdottoBtnClicked(self, mainPath, amministratore, obj):
        listaId = list()
        for box in range(obj.tab.rowCount()):
            if obj.tab.item(box, 0).checkState() == QtCore.Qt.Checked:
                listaId.append(int(obj.tab.item(box, 3).text()))
        Controller().eliminaProdottiTramiteListaId(listaId)
        self.prodottiBtnClicked(mainPath, amministratore, None)

    # Metodo che vende i prodotti selezionati nella lista dei prodotti
    def vendiProdottoBtnClicked(self, mainPath, amministratore, obj):
        listaId = list()
        for box in range(obj.tab.rowCount()):
            if obj.tab.item(box, 0).checkState() == QtCore.Qt.Checked:
                listaId.append(int(obj.tab.item(box, 3).text()))
        Controller().vendiProdottiTramiteListaId(listaId)
        self.prodottiBtnClicked(mainPath, amministratore, None)
        # TODO fare un finestra che si apre al posto della ricevuta di acquisto

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    def accountsBtnClicked(self, mainPath, amministratore, lista):
        name = "accountsView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        if lista == None:
            lista = Controller().recuperaListaAccounts()
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        self.aggiungiAccountsAllaTab(mainPath, obj, amministratore, lista)
        obj.aggiungiBtn.clicked.connect(lambda: amministratore.aggiungiClienteBtnClicked(mainPath, amministratore))
        obj.rimuoviBtn.clicked.connect(lambda: amministratore.rimuoviClienteBtnClicked(mainPath, obj, amministratore))
        obj.cercaBtn.clicked.connect(lambda: amministratore.cercaClienteBtnClicked(mainPath, obj, amministratore))

    def cercaClienteBtnClicked(self, mainPath, obj, amministratore):
        textNome = str(obj.nome_le.text())
        textCognome = str(obj.cognome_le.text())
        lista = Controller().filtraClienti(textNome, textCognome)
        self.accountsBtnClicked(mainPath, amministratore, lista)

    # Metodo per gestire i pulsanti premuti sul menu sinistro
    def backupBtnClicked(self, mainPath, amministratore):
        name = "backupView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.pushedStyleSheet())
        obj.pushButton.clicked.connect(lambda: self.effettuaBackup(obj))

    # Metodo per effettuare il backup dei dati
    def effettuaBackup(self, obj):
        Controller().effettuaBackup()
        obj.stato.setText("Backup eseguito")

    # Metodo che si attiva alla pressione del prodottiBtn
    def aggiungiProdottoBtnClicked(self, mainPath, amministratore):
        name = "inserisciProdottoView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.aggiungiBtn.clicked.connect(lambda: self.saveProdottoBtnClicked(mainPath, obj, amministratore))
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore, None))

    # Metodo che si attiva alla pressione del aggiungiBtn
    def aggiungiClienteBtnClicked(self, mainPath, amministratore):
        name = "inserisciClienteView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.saveBtn.clicked.connect(lambda: self.saveClienteBtnClicked(mainPath, obj, amministratore, None))
        obj.indietroBtn.clicked.connect(lambda: self.accountsBtnClicked(mainPath, amministratore, None))

    # Metodo che rimuove account dal database del sistema e si attiva alla pressione di rimuoviBtn
    def rimuoviClienteBtnClicked(self, mainPath, obj, amministratore):
        listaId = list()
        for box in range(obj.tab.rowCount()):
            if obj.tab.item(box, 0).checkState() == QtCore.Qt.Checked:
                listaId.append(int(obj.tab.item(box, 3).text()))
        Controller().eliminaAccountTramiteListaId(listaId)
        self.accountsBtnClicked(mainPath, amministratore, None)

    # Metodo che si attiva alla pressione del aggiungiProdottoBtn
    def saveProdottoBtnClicked(self, mainPath, obj, amministratore):
        nomeLe = obj.nomeLe.text()
        idAccountLe = obj.idAccountLe.text()
        prezzoLe = obj.prezzoLe.text()
        idCategoriaLe = obj.idCategoriaLe.text()
        idScaffaleLe = obj.idScaffaleLe.text()
        if self.checkerSaveProdottoBtnClicked(nomeLe, idAccountLe, prezzoLe, idCategoriaLe, idScaffaleLe):
            pass
        else:
            self.prodottiBtnClicked(mainPath, amministratore, None)
        Controller().amministratoresaveProdottoBtn(nomeLe, idAccountLe, datetime.today(), prezzoLe, idCategoriaLe,
                                                   idScaffaleLe)
        self.prodottiBtnClicked(mainPath, amministratore, None)

    # Metodo che si attiva alla pressione del saveClienteBtn
    def saveClienteBtnClicked(self, mainPath, obj, amministratore, lista):
        nomeLe = obj.nomeLe.text()
        cognomeLe = obj.cognomeLe.text()
        dataNascitaLe = obj.dataNascitaLe.text()
        emailLe = obj.emailLe.text()
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
        # style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; " \
                "border-top-left-radius: 15px; border-bottom-left-radius: 15px}"
        return style

    # Metodo che restitiusce la stringa nel metodo
    def unPushedStyleSheet(self):
        # style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; " \
                "border-top-left-radius: 25px; border-bottom-left-radius: 25px;}"
        return style

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    def removeAndAdd(self, item):
        try:
            # print(f"{self.finestra.verticalLayout_toPaste.count()}")
            for wid in range(self.finestra.verticalLayout_toPaste.count()):
                self.finestra.verticalLayout_toPaste.itemAt(wid).widget().deleteLater()
        except:
            pass
        self.finestra.verticalLayout_toPaste.addWidget(item)

    # Metodo che carica una view presente nelle AdminButtonsViews grazie al nome passato
    def caricaView(self, mainPath, name):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "AdminButtonsViews", name)
        file = QFile(path)
        file.open(QFile.ReadOnly)
        finestra = loader.load(file)
        file.close()
        return finestra

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    def aggiungiProdottiAllaTab(self, mainPath, obj, amministratore, lista):
        # lista = Controller().recuperaListaProdottiInVendita()
        column = 6
        obj.tab.setColumnCount(column)
        obj.tab.setColumnWidth(0, 15)
        for i in range(column):
            obj.tab.setColumnWidth(i + 1, 100)
        obj.tab.setHorizontalHeaderLabels(
            (None, "nome", "prezzo", "id prodotto", "data scadenza", "click su visualizza"))
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
            obj.tab.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{prodotto.dataScadenza}"))
            obj.tab.setCellWidget(row, 5,
                                  self.creaBottoneVisualizzaProdottoQualsiasi(mainPath, prodotto.idProdotto,
                                                                              amministratore, lista))
            row += 1

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    def aggiungiAccountsAllaTab(self, mainPath, obj, amministratore, lista):
        # lista = Controller().recuperaListaAccounts()
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
            row += 1

    # Metodo che crea un bottone grazie al idProdotto
    def creaBottoneVisualizzaProdottoQualsiasi(self, mainPath, idProdotto, amministratore, lista):
        # button = QToolButton()
        button = QPushButton()
        button.setText("Visualizza")
        button.clicked.connect(lambda: self.caricaifoProdottoView(mainPath, "infoProdottoView.ui",
                                                                  Controller().trovaProdottoTramiteId(idProdotto),
                                                                  amministratore, lista))
        return button

    # Metodo che crea un bottone grazie al idAccount
    def creaBottoneVisualizzaAccountQualsiasi(self, mainPath, idAccount, amministratore, lista):
        # button = QToolButton()
        button = QPushButton()
        button.setText("Visualizza")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(lambda: self.caricaifoAccountView(mainPath, "infoaccountView.ui",
                                                                 Controller().trovaAccountTramiteId(idAccount),
                                                                 amministratore, lista))
        return button

    # Metodo che carica le info di un prodotto all'interno della View
    def caricaifoProdottoView(self, mainPath, fileName, prodottoTrovato, amministratore, lista):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeProdottoDaIns.setText(prodottoTrovato.nomeProdotto)
        obj.prezzoCorrenteDaIns.setText(prodottoTrovato.prezzoCorrente)
        obj.prezzoOriginaleDaIns.setText(prodottoTrovato.prezzoOriginale)
        obj.dataDiEsposizioneDaIns.setText(f"{prodottoTrovato.dataEsposizione}")
        obj.dataDiScadenzaDaIns.setText(f"{prodottoTrovato.dataScadenza}")
        obj.idProdottoDaIns.setText(f"{prodottoTrovato.idProdotto}")
        obj.idScaffaleDaIns.setText(f"{prodottoTrovato.idScaffale}")
        obj.nomeCategoriaDaIns.setText(f"{prodottoTrovato.idCategoria}")
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore, lista))

    # Metodo che carica le info di un account all'interno della View
    def caricaifoAccountView(self, mainPath, fileName, account, amministratore, lista):
        obj = self.caricaView(mainPath, fileName)
        self.removeAndAdd(obj)
        obj.nomeDaIns.setText(account.nome)
        obj.cognomeDaIns.setText(account.cognome)
        obj.dataDiNascitaDaIns.setText(account.dataDiNascita)
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

    # Metodo per controllare la validità dei dati inseriti dall'utente
    def checkerSaveProdottoBtnClicked(self, nomeLe, idAccountLe, prezzoLe, idCategoriaLe, idScaffaleLe):
        if nomeLe == "": return False
        if not idAccountLe.isalnum(): return False
        if not prezzoLe.isalnum(): return False
        if prezzoLe != "": return False
        if not idCategoriaLe.isalnum(): return False
        if not idScaffaleLe.isalnum(): return False
        return True

    # Metodo per controllare la validità dei dati inseriti dall'utente
    def checkerSaveClienteBtnClicked(self, nomeLe, cognomeLe, dataDiNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                                     cittaLe, viaLe, piazzaLe, civicoLe, citofonoLe):
        if nomeLe == "": return False
        if cognomeLe == "": return False
        if not self.validateDate(dataDiNascitaLe): return False
        if not telefonoLe.isalnum(): return False
        if not capLe.isalnum(): return False
        return True

    def validateDate(self, date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except:
            print("data non valida")
            return False
