from operator import index

from MVC.Model.SistemService.File import File



class Account(object):


    # Costruttore dell'Account, create() in EA
    def __init__(self):
        self.cliente = None
        self.nome = None
        self.cognome = None
        self.dataDiNascita = None
        self.email = None
        self.iDAccount = None
        self.iDProdotti = None
        self.numeroTelefonico = None
        self.residenza = None


    # Metodo che permette di aggiungere un Account
    def aggiungiAccount(self,cliente , nome, cognome, dataDiNascita, email,
                        idAccount, idProdotti, numeroTelefonico, residenza):
        self.cliente = True
        self.nome = nome
        self.cognome = cognome
        self.dataDiNascita = dataDiNascita
        self.email = email
        self.idAccount = self.newId()
        self.idProdotti = idProdotti
        self.numeroTelefonico = numeroTelefonico
        self.residenza = residenza
        fileName = 'Database\Account\Account.txt'
        self.mettiAccountSuFile(fileName)


    # Metodo che serve per leggere la lista degli account all'interno del Database
    def leggiAccount(self):
        fileName = 'Database\Account\Account.txt'
        file = File()
        listAccount = file.deserializza(fileName)
        return listAccount


    # Metodo che permette di eliminare un Account
    def eliminaAccount(self, idAccount):
            fileName = 'Database\Account\account.txt'
            listaccount = self.leggiAccount()
            for x in listaccount:
                if x.iDAccount == idAccount:
                    listaccount.pop(index(x))
            File.serializza(fileName, listaccount)


    # Metodo per trovare un account tramite l'email dell' Account
    def trovaAccountTramiteEmail(self, email):
        listAccount = self.leggiAccount()
        for x in listAccount:
            if x.email == email:
                return listAccount(index(x))


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
        fileName = "Databasa\parametri.txt"
        file = File()
        letto = file.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDAccount'] + 1
        dictLetto['lastIDAccount'] = self.newId
        file = File()
        file.scrivi(fileName, dictLetto.__str__)
        return self.newId


    # Metodo che rimuove un Prodotto da file e lo restituisce
    def prendiAccountDaFile(self, startfileName, idProdotto):
        file = File()
        listProdotto = file.deserializza(startfileName)
        popped = None
        for obj in listProdotto:
            if obj.idProdotto == idProdotto:
                popped = listProdotto.pop(listProdotto.index(obj))
            else:
                return None
        file = File()
        file.serializza(startfileName, listProdotto)
        return popped


    # Metodo che viene richiamato sull'istanza che deve essere messa su un file
    def mettiAccountSuFile(self, fileName):
        file = File()
        listAccount= file.deserializza(fileName)
        for account in listAccount:
            if account.idProdotto == self.idAccount:
                listAccount.pop(listAccount.index(self))
        listAccount.append(self)
        File.serializza(fileName, listAccount)


    # Metodo che aggiorna un account in base ai parametri passati dalla classe Amministratore
    def aggiornaAccount(self,cliente, nome, cognome, dataDiNascita, email,
        iDAccount, numeroTelefonico, residenza):
        fileName = 'Database\Clienti\Clienti.txt'
        account = Account.prendiAccountDaFile(fileName, iDAccount)
        if nome != account.nome: account.nome = nome
        if cognome != account.cognome: account.cognome = cognome
        if dataDiNascita != account.dataDiNascita: account.dataDiNascita = dataDiNascita
        if email != account.email: account.email = email
        if numeroTelefonico != account.numeroTelefonico: account.numeroTelefonico = numeroTelefonico
        if residenza != account.residenza: account.residenza = residenza
        fileName = "Database\Clienti\Clienti.txt"
        account.mettiAccountSuFile(fileName, account)


    # Metodo che recupera la lista degli account, trova l'account con i'id vecchio e al suo interno,
    # nella lista degli oggetti elimina l'oggetto di interesse.
    # successivamente alla prima eliminazione viene cerrcato l'account nuovo e al suo interno, nella ista degli id degli
    # oggetti si aggiunge l'id nuovo
    def aggiornaIdProdottoInAccount(self, prodotto, idVecchio, idNuovo):
        prodotto.idAccount = idNuovo
        fileName = "Database\Clienti\Clienti.txt"
        file = File()
        listAccount = file.deserializza(fileName)
        for account in listAccount:
            if account.idAccount == idVecchio:
                for idProdotto in account.idProdotti:
                    if idProdotto == prodotto.IDProdotto:
                        account.idProdotti.pop(index(idProdotto))
        for account in listAccount:
            if account.idAccount == idNuovo:
                account.idProdotti.append(prodotto.IDProdotto)