import os
from datetime import datetime
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QLabel, QToolButton

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

    # Metodo per cambiare al pulsante il colore dopo premuto
    def homeBtnClicked(self, mainPath, amministratore):
        name = "homeView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())

    # Metodo per cambiare al pulsante il colore dopo premuto
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


    # Metodo per cambiare al pulsante il colore dopo premuto
    def prodottiBtnClicked(self, mainPath, amministratore):
        name = "prodottiView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        self.aggiungiProdottiAllaTab(obj)
        obj.aggiungiBtn.clicked.connect(lambda: amministratore.aggiungiProdottoBtnClicked(mainPath, amministratore))
        #TODO obj.rimuoviBtn.clicked.connect(lambda: amministratore.rimuoviProdottoBtnClicked(mainPath, amministratore))

    # Metodo per cambiare al pulsante il colore dopo premuto
    def accountsBtnClicked(self, mainPath, amministratore):
        name = "accountsView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        amministratore.finestra.homeBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.statisticheBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.prodottiBtn.setStyleSheet(self.unPushedStyleSheet())
        amministratore.finestra.accountsBtn.setStyleSheet(self.pushedStyleSheet())
        amministratore.finestra.backupBtn.setStyleSheet(self.unPushedStyleSheet())
        self.aggiungiAccountsAllaTab(obj)
        obj.aggiungiBtn.clicked.connect(lambda: amministratore.aggiungiClienteBtnClicked(mainPath, amministratore))
        #TODO obj.rimuoviBtn.clicked.connect(lambda: amministratore.rimuoviClienteBtnClicked(mainPath, amministratore))

    # Metodo per cambiare al pulsante il colore dopo premuto
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
        obj.saveBtn.clicked.connect(lambda: self.saveProdottoBtnClicked(mainPath, obj, amministratore))
        obj.indietroBtn.clicked.connect(lambda: self.prodottiBtnClicked(mainPath, amministratore))

    # Metodo che si attiva alla pressione del aggiungiBtn
    def aggiungiClienteBtnClicked(self, mainPath, amministratore):
        name = "inserisciClienteView.ui"
        obj = self.caricaView(mainPath, name)
        self.removeAndAdd(obj)
        obj.saveBtn.clicked.connect(lambda: self.saveClienteBtnClicked(mainPath, obj, amministratore))
        obj.indietroBtn.clicked.connect(lambda: self.accountsBtnClicked(mainPath, amministratore))

    # Metodo che si attiva alla pressione del saveProdottoBtn
    def saveProdottoBtnClicked(self, mainPath, obj, amministratore):
        nomeLe = obj.nomeLe.text()
        idAccountLe = obj.idAccountLe.text()
        prezzoLe = obj.prezzoLe.text()
        idCategoriaLe = obj.idCategoriaLe.text()
        idScaffaleLe = obj.idScaffaleLe.text()
        if self.checkerSaveProdottoBtnClicked(nomeLe, idAccountLe, prezzoLe, idCategoriaLe, idScaffaleLe):
            pass
        else:
            self.prodottiBtnClicked(mainPath, amministratore)
        Controller().amministratoresaveProdottoBtn(nomeLe, idAccountLe, datetime.today(), prezzoLe, idCategoriaLe,
                                                   idScaffaleLe)
        self.prodottiBtnClicked(mainPath, amministratore)

    # Metodo che si attiva alla pressione del saveClienteBtn
    def saveClienteBtnClicked(self, mainPath, obj, amministratore):
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
            self.accountsBtnClicked(mainPath, amministratore)
            return
        Controller().saveCLienteBtnClicked(nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                                           citofonoLe, viaLe, piazzaLe, civicoLe, citofonoLe)

    # Metodo che restitiusce la stringa nel metodo
    def pushedStyleSheet(self):
        # style = 'QPushButton {background-color: #1a1f39; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #1a1f39; padding:10px 5px; text-align: left; border-top-left-radius: 15px; border-bottom-left-radius: 15px}"
        return style

    # Metodo che restitiusce la stringa nel metodo
    def unPushedStyleSheet(self):
        # style = 'QPushButton {background-color: #2a2c49; color: #78799c;}'
        style = "QPushButton {color: #78799c; background-color: #2a2c49; padding: 10px 5px; text-align: left; border-top-left-radius: 25px; border-bottom-left-radius: 25px;}"
        return style

    # Metodo che: rimuove un widget B che era stato messo in un widget A e mette un widget C nel widget A
    def removeAndAdd(self, item):
        try:
            self.finestra.verticalLayout_toPaste.itemAt(0).widget().deleteLater()
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
    def aggiungiProdottiAllaTab(self, obj):
        lista = Controller().recuperaListaProdottiInVendita()
        colonne = 5
        obj.tab.setColumnCount(colonne)
        obj.tab.setColumnWidth(0, 15)
        for i in range(colonne):
            obj.tab.setColumnWidth(i + 1, 100)
        obj.tab.setHorizontalHeaderLabels((None, "nome", "prezzo", "idProdotto", "dataScadenza"))

        row = 0
        obj.tab.setRowCount(len(lista))
        for prodotto in lista:
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            obj.tab.setItem(row, 0, chkBoxItem)
            obj.tab.setItem(row, 1, QtWidgets.QTableWidgetItem(prodotto.nomeProdotto))
            obj.tab.setItem(row, 2, QtWidgets.QTableWidgetItem(prodotto.prezzoCorrente))
            obj.tab.setItem(row, 3, QtWidgets.QTableWidgetItem(prodotto.idProdotto))
            obj.tab.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{prodotto.dataScadenza}"))
            row += 1
            self.aggiungiBottoniAllaTabProdotti(row, obj)

    # Metodo che aggiunge i prodotti in vendita al tableWidget
    def aggiungiAccountsAllaTab(self, obj):
        lista = Controller().recuperaListaAccounts()
        colonne = 5
        obj.tab.setColumnCount(colonne)
        obj.tab.setColumnWidth(0, 15)
        for i in range(colonne):
            obj.tab.setColumnWidth(i + 1, 100)
        obj.tab.setHorizontalHeaderLabels((None, "nome", "cognome", "idAccount", "email"))
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
            row += 1

    # Metodo per aggiungere un bottone su ogni riga della tabella per poter visualizzare le info del prodotto
    #TODO metono non funzionante
    def aggiungiBottoniAllaTabProdotti(self, rowNumber, obj):
        #QWidget.__init__(self, parent)
        #self.button_layout = QHBoxLayout()
        #self.widget_layout = QVBoxLayout()
        for button_number in range(rowNumber):
            button = QToolButton()
            button.setText(str(button_number))
            button.setObjectName('Button%d' % button_number)
            button.released.connect(self.button_released)
            #self.button_layout.addWidget(button)
            obj.tab.setItem(button_number, 5, button)

        #self.status_label = QLabel('No button clicked')
        #self.widget_layout.addItem(self.button_layout)
        #self.widget_layout.addWidget(self.status_label)
        #self.setLayout(self.widget_layout)

    # Metodo che accompagna il metodo aggiungiBottoniAllaTabProdotti()
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))

    # Metodo per controllare la validità dei dati inseriti dall'utente
    def checkerSaveProdottoBtnClicked(self, nomeLe, idAccountLe, prezzoLe, idCategoriaLe, idScaffaleLe):
        if nomeLe != "":
            if idAccountLe.isalnum():
                if prezzoLe.isalnum():
                    if idCategoriaLe.isalnum():
                        if idScaffaleLe.isalnum():
                            return True
        return False

    # Metodo per controllare la validità dei dati inseriti dall'utente
    def checkerSaveClienteBtnClicked(self, nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                                     cittaLe, viaLe, piazzaLe, civicoLe, citofonoLe):
        if nomeLe != "":
            if cognomeLe != "":
                if self.validateDate(dataNascitaLe):
                    if telefonoLe.isalnum():
                        if capLe.isalnum():
                            return True
        return False

    def validateDate(self, date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except:
            return False
