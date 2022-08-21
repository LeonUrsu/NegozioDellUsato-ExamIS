from operator import index

from MVC.Model.SistemService.File import File
from Database.PathDatabase import PathDatabase

class Account(object):


    # Costruttore dell'Account, create() in EA
    def __init__(self):
        self.nome = None
        self.cognome = None
        self.dataDiNascita = None
        self.email = None
        self.iDAccount = None
        self.iDProdotti = None
        self.numeroTelefonico = None
        self.password = None
        self.residenza = None


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


    # Metodo che aggiunge l'account nel database
    def inserisciLoggingNelDatabase(self):
        fileName = PathDatabase().clientiTxt
        self.mettiAccountSuFile(fileName)


    # Metodo che serve per leggere la lista degli account all'interno del Database
    def leggiAccount(self):
        fileName = PathDatabase().clientiTxt
        listAccount = File().deserializza(fileName)
        return listAccount


    # Metodo che permette di eliminare un Account
    def eliminaAccount(self, idAccount):
            fileName = PathDatabase().clientiTxt
            accountEliminato = None
            listaccount = self.leggiAccount()
            for x in listaccount:
                if x.iDAccount == idAccount:
                    accountEliminato = listaccount.pop(index(x))
            File().serializza(fileName, listaccount)



    # Metodo per trovare un account tramite l'email dell' Account
    def trovaAccountTramiteEmail(self, email):
        listAccount = self.leggiAccount()
        for x in listAccount:
            if x.email == email:
                return listAccount(index(x))
        return None


    # Metodo per trovare un account tramite l'id dell' Account
    def trovaAccountTramiteId(self, id):
        listAccount = self.leggiAccount()
        for x in listAccount :
            if x.iDAccount == self.idAccount:
                return listAccount(index(x))
            else: return None


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


    # Metodo che rimuove un Prodotto da file e lo restituisce
    def prendiAccountDaFile(self, startfileName, idAccount):
        file = File()
        listAccount = File().deserializza(startfileName)
        popped = None
        for obj in listAccount:
            if obj.idAccount == idAccount:
                popped = listAccount.pop(listAccount.index(obj))
            else:
                return None
        File().serializza(startfileName, listAccount)
        return popped


    # Metodo che viene richiamato sull'istanza di Account che deve essere messa su un file
    def mettiAccountSuFile(self, fileName):
        listAccount= File().deserializza(fileName)
        listAccount.append(self)
        File().serializza(fileName, listAccount)


    # Metodo che aggiorna un account in base ai parametri passati dalla classe Amministratore
    def aggiornaAccount(self,cliente, nome, cognome, dataDiNascita, email,
        iDAccount, numeroTelefonico, residenza):
        fileName = PathDatabase().clientiTxt
        account = Account()
        account = account.prendiAccountDaFile(fileName, iDAccount)
        if nome != account.nome: account.nome = nome
        if cognome != account.cognome: account.cognome = cognome
        if dataDiNascita != account.dataDiNascita: account.dataDiNascita = dataDiNascita
        if email != account.email: account.email = email
        if numeroTelefonico != account.numeroTelefonico: account.numeroTelefonico = numeroTelefonico
        if residenza != account.residenza: account.residenza = residenza
        account.mettiAccountSuFile(fileName, account)


    # Metodo che recupera la lista degli account, trova l'account con i'id vecchio e al suo interno,
    # nella lista degli oggetti elimina l'oggetto di interesse.
    # successivamente alla prima eliminazione viene cerrcato l'account nuovo e al suo interno, nella ista degli id degli
    # oggetti si aggiunge l'id nuovo
    def aggiornaIdProdottoInAccount(self, prodotto, idVecchio, idNuovo):
        prodotto.idAccount = idNuovo
        fileName = PathDatabase().clientiTxt
        file = File()
        listAccount = File().deserializza(fileName)
        for account in listAccount:
            if account.idAccount == idVecchio:
                for idProdotto in account.idProdotti:
                    if idProdotto == prodotto.IDProdotto:
                        account.idProdotti.pop(index(idProdotto))
        for account in listAccount:
            if account.idAccount == idNuovo:
                account.idProdotti.append(prodotto.IDProdotto)


    # Metodo che controlla se sul file esiste un utente con lo stesso indirizzo email
    # per liminare l'inconsistenza dei dati
    # listLogging = lista di credenziali utente
    # email = email da verificare
    # return = True if esiste già l'email nel sistema
    def checkEmailUtente(self, email):
        fileName = PathDatabase().clientiTxt
        listAccount = File().deserializza(fileName)
        for account in listAccount:
            if account.email == email:
                return True
        return False


    # Metodo che associa un idProdotto ad un account
    def aggiungiProdottoAAccount(self, prodotto):
        listAccount = self.leggiAccount()
        for account in listAccount:
            if account.idAccount == prodotto.idAccount:
                account.idProdotti.append(prodotto.idProdotto)
                return True
        return False


    # Metodo che dissocia un id di un prodotto da un account
    def dissociaProdottoDaAccount(self, prodotto):
        listAccount = self.leggiAccount()
        fileName = PathDatabase().clientiTxt
        for account in listAccount:
            if account.idAccount == prodotto.idAccount:
                for idProdotto in account.idProdotti:
                    if idProdotto == prodotto.idProdotto:
                        account.idProdotti.pop(index(idProdotto))
                        File().serializza(fileName, listAccount)

