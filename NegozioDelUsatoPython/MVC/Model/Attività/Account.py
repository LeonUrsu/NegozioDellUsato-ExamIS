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
        self.dataDiNascita = dataDiNascita
        self.email = email
        self.idAccount = self.newId()
        self.idProdotti = list()
        self.numeroTelefonico = numeroTelefonico
        self.password = password
        self.residenza = residenza
        self.mettiOggettoSuListaNelFile()

    """    # Metodo che aggiunge l'account nel database
    def inserisciOggettoNelDatabase(self):
        fileName = PathDatabase().clientiTxt
        self.mettiOggettoSuListaNelFile()
    """

    # Metodo che legge la lista degli account nel file e la restituisce
    def recuperaListaOggetti(self):
        fileName = PathDatabase().clientiTxt
        listAccount = File().deserializza(fileName)
        return listAccount

    # Metodo che salva la lista degli account nel file
    def salvaListaOggetti(self, lista):
        fileName = PathDatabase().clientiTxt
        File().serializza(fileName, lista)

    # Metodo che permette di eliminare un Account dal file degli account
    # idAccount = id del account da cercare e eliminare
    # return = ritorno del account eliminato
    def eliminaAccount(self, idAccount):
        accountEliminato = None
        listaccount = self.recuperaListaOggetti()
        for x in listaccount:
            if x.iDAccount == idAccount:
                accountEliminato = listaccount.pop(index(x))
        self.salvaListaOggetti(listaccount)
        return accountEliminato

    # Metodo per trovare un account tramite l'email dell' Account
    def trovaOggettoTramiteEmail(self, email):
        listAccount = self.recuperaListaOggetti()
        for x in listAccount:
            if x.email == email:
                return listAccount(index(x))
        return None

    # Metodo per trovare un account tramite l'id dell' Account
    def trovaOggettoTramiteId(self, id):
        listAccount = self.recuperaListaOggetti()
        for account in listAccount:
            if account.idAccount == id:
                return listAccount(index(account))
            else:
                return None

    # Metodo che ritorna il nuovo id da assegnare all' Account da inserire
    # return = nuovo Id per l'Account
    def newId(self):
        fileName = PathDatabase().parametriTxt
        letto = File().leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDAccount'] + 1
        dictLetto['lastIDAccount'] = self.newId
        file = File()
        File().scrivi(fileName, dictLetto.__str__)
        return self.newId

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

    # Metodo che viene richiamato sull'istanza di Account che deve essere messa su un file
    def mettiOggettoSuListaNelFile(self):
        listAccount = Account.recuperaListaOggetti()
        for account in listAccount:
            if account.idAccount == self.idAccount:
                listAccount.pop(listAccount.index(account))
        listAccount.append(self)
        self.salvaListaOggetti(listAccount)

    # Metodo che aggiorna un account in base ai parametri passati dalla classe Amministratore
    def aggiornaAccount(self, nome, cognome, dataDiNascita, email, iDAccount, numeroTelefonico, residenza):
        fileName = PathDatabase().clientiTxt
        account = Account().prendiOggettoDaFile(fileName, iDAccount)
        if nome != account.nome: account.nome = nome
        if cognome != account.cognome: account.cognome = cognome
        if dataDiNascita != account.dataDiNascita: account.dataDiNascita = dataDiNascita
        if self.checkEmailUtente(email) == False and email != account.email: account.email = email
        if self.checkNumeroTelefonico(
            numeroTelefonico) and numeroTelefonico != account.numeroTelefonico: account.numeroTelefonico = numeroTelefonico
        if residenza != account.residenza: account.residenza = residenza
        account.mettiOggettoSuListaNelFile()

    """
    # Metodo che recupera la lista degli account, trova l'account con i'id vecchio e al suo interno,
    # nella lista degli oggetti elimina l'oggetto di interesse.
    # successivamente alla prima eliminazione viene cerrcato l'account nuovo e al suo interno, nella ista degli id degli
    # oggetti si aggiunge l'id nuovo
    def aggiornaIdProdottoInAccount(self, prodotto, idVecchio, idNuovo):
        #prodotto.idAccount = idNuovo
        fileName = PathDatabase().clientiTxt
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
        fileName = PathDatabase().clientiTxt
        listAccount = File().deserializza(fileName)
        for account in listAccount:
            if account.email == email:
                return True
        return False

    # Metodo che controlla se sul file esiste un utente con lo stesso numero telefonico
    # numero = numero da verificare
    # return = True if esiste già il numero nel sistema
    def checkNumeroTelefonico(self, numero):
        fileName = PathDatabase().clientiTxt
        listAccount = File().deserializza(fileName)
        for account in listAccount:
            if account.numero == numero:
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
