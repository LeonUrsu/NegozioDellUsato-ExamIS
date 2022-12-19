import datetime
import json
from operator import index
from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from MVC.Model.SistemService.File import File
from Database.PathDatabase import PathDatabase


class Account(ServizioInterface):

    # Costruttore dell'Account, create() in EA
    def __init__(self):
        pass

    # Metodo che permette di inizializzare l'istanza Account
    def aggiungiAccount(self, nome, cognome, dataDiNascita, email, numeroTelefonico, password, residenza):
        self.nome = nome
        self.cognome = cognome
        self.dataDiNascita = self.pairDataDiNascita(dataDiNascita)
        self.email = email.lower()
        self.idAccount = self.newId()
        self.idProdotti = list()
        if self.checkNumeroTelefonico(numeroTelefonico):
            self.numeroTelefonico = numeroTelefonico
        else:
            self.numeroTelefonico = None
        self.password = password
        self.residenza = residenza
        self.mettiOggettoSuListaNelFile()
        return self

    # Metodo che legge la lista degli account nel file e la restituisce
    def recuperaListaOggetti(self):
        fileName = PathDatabase().accountTxt
        listAccount = File().deserializza(fileName)
        return listAccount

    # Metodo che salva la lista degli account nel file
    def salvaListaOggetti(self, lista):
        fileName = PathDatabase().accountTxt
        File().serializza(fileName, lista)

    # Metodo che permette di eliminare un Account dal file degli account
    # idAccount = id del account da cercare e eliminare
    # return = ritorno del account eliminato
    def eliminaAccount(self, idAccount):
        accountEliminato = None
        listaccount = self.recuperaListaOggetti()
        for account in listaccount:
            if account.idAccount == idAccount:
                accountEliminato = account
                listaccount.pop(listaccount.index(account))
        self.salvaListaOggetti(listaccount)
        return accountEliminato

    # Metodo per trovare un account tramite l'email dell' Account
    def trovaOggettoTramiteEmail(self, email):
        listAccount = self.recuperaListaOggetti()
        for account in listAccount:
            if account.email == email:
                return listAccount[listAccount.index(account)]
        return None

    # Metodo per trovare un account tramite l'id dell' Account
    def trovaOggettoTramiteId(self, id):
        listaAccount = self.recuperaListaOggetti()
        for account in listaAccount:
            if account.idAccount == id:
                return listaAccount[listaAccount.index(account)]
        return None

    # Metodo che ritorna il nuovo id da assegnare all' Account da inserire
    # return = nuovo Id per l'Account
    def newId(self):
        fileName = PathDatabase().parametriTxt
        letto = File().leggi(fileName)
        dictLetto = json.loads(letto)
        newId = dictLetto['lastIdAccount'] + 1
        dictLetto['lastIdAccount'] = newId
        File().scrivi(fileName, json.dumps(dictLetto))
        return newId

    """    # Metodo che rimuove un Prodotto da file e lo restituisce
    def prendiOggettoDaFile(self, startfileName, idAccount):
        file = File()
        listAccount = File().deserializza(startfileName)
        popped = None
        for obj in listAccount:
            if obj.idAccount == idAccount:
                popped = listAccount.pop(listAccount.index(obj))
            else:
                return None
        File().serializza(startfileName, listAccount)
        return popped"""

    def mettiOggettoSuListaNelFile(self):
        listAccount = Account.recuperaListaOggetti(self)
        for account in listAccount:
            if account.idAccount == self.idAccount:
                listAccount.pop(listAccount.index(account))
        listAccount.append(self)
        self.salvaListaOggetti(listAccount)

    # Metodo che aggiorna un account in base ai parametri passati dalla classe Amministratore
    def aggiornaAccount(self, nome, cognome, dataDiNascita, email, idAccount, numeroTelefonico, residenza):
        account = Account().trovaOggettoTramiteId(idAccount)
        if nome != "": account.nome = nome
        if cognome != "": account.cognome = cognome
        if dataDiNascita != "": account.dataDiNascita = self.pairDataDiNascita(dataDiNascita)
        if self.checkEmailUtente(email) == False and email != "":
            account.email = email
        if not self.checkNumeroTelefonico(numeroTelefonico) and numeroTelefonico != "":
            account.numeroTelefonico = numeroTelefonico
        if residenza != None:
            if residenza.cap != "":
                account.residenza.cap = residenza.cap
            if residenza.via != "":
                account.residenza.via = residenza.via
            if residenza.citta != "":
                account.residenza.citta = residenza.citta
            if residenza.civico != "":
                account.residenza.civico = residenza.civico
            if residenza.piazza != "":
                account.residenza.piazza = residenza.piazza
            if residenza.citofono != "":
                account.residenza.citofono = residenza.citofono
        account.mettiOggettoSuListaNelFile()
        return account

    # Metodo che grazie ad un formato strasforma una data in str in datetime
    def pairDataDiNascita(self, dataStr):
        format = "%d/%m/%Y"
        dataPaired = datetime.datetime.strptime(dataStr, format)
        return dataPaired

    """
    # Metodo che recupera la lista degli account, trova l'account con i'id vecchio e al suo interno,
    # nella lista degli oggetti elimina l'oggetto di interesse.
    # successivamente alla prima eliminazione viene cerrcato l'account nuovo e al suo interno, nella ista degli id degli
    # oggetti si aggiunge l'id nuovo
    def aggiornaIdProdottoInAccount(self, prodotto, idVecchio, idNuovo):
        #prodotto.idAccount = idNuovo
        fileName = PathDatabase().accountTxt
        listAccount = File().deserializza(fileName)
        for account in listAccount:
            if account.idAccount == idVecchio:
                for idProdotto in account.idProdotti:
                    if idProdotto == prodotto.IDProdotto:
                        account.idProdotti.pop(index(idProdotto))
        for account in listAccount:
            if account.idAccount == idNuovo:
                account.idProdotti.append(prodotto.IDProdotto)
    """

    # Metodo che controlla se sul file esiste un utente con lo stesso indirizzo email
    # email = email da verificare
    # return = True if esiste già l'email nel sistema
    def checkEmailUtente(self, email):
        accountFile = PathDatabase().accountTxt
        listAccount = File().deserializza(accountFile)
        for account in listAccount:
            if email == "admin":
                return True
            if account.email == email:
                return True
        return False

    # Metodo che controlla se sul file esiste un utente con lo stesso numero telefonico
    # numero = numero da verificare
    # return = True if esiste già il numero nel sistema
    def checkNumeroTelefonico(self, numero):
        fileName = PathDatabase().accountTxt
        listAccount = File().deserializza(fileName)
        for account in listAccount:
            if account.numeroTelefonico == numero:
                return True
        return False

    # Metodo che associa un idProdotto ad un account
    def associaProdottoAdAccount(self, prodotto):
        listAccount = self.recuperaListaOggetti()
        for account in listAccount:
            if account.idAccount == prodotto.idAccount:
                account.idProdotti.append(prodotto.idProdotto)
                self.salvaListaOggetti(listAccount)
                return True
        return False

    # Metodo che dissocia un id di un prodotto da un account
    def dissociaProdottoDaAccount(self, prodotto):
        listAccount = self.recuperaListaOggetti()
        for account in listAccount:
            if account.idAccount == prodotto.idAccount:
                for idProdotto in account.idProdotti:
                    if idProdotto == prodotto.idProdotto:
                        account.idProdotti.pop(index(idProdotto))
                        self.salvaListaOggetti(listAccount)

    # Metodo che controlla l'esistenza di un id
    def checkEsistenzaIdAccount(self, id):
        prodotto = self.trovaOggettoTramiteId(id)
        if not prodotto == None:
            return True
        return False
