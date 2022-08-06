from MVC.Model.SistemService.File import File


class Account:

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
                        iDAccount, iDProdotti, numeroTelefonico, residenza):
        self.cliente = True
        self.nome = nome
        self.cognome = cognome
        self.dataDiNascita = dataDiNascita
        self.email = email
        self.iDAccount = newID()
        self.iDProdotti = IDProdotti
        self.numeroTelefonico = numeroTelefonico
        self.residenza = residenza
        #fare metodo per aggiungere account in database
        fileName = 'Database\Account\Account.txt'
        self.mettiAccountSuFile(fileName, self)


    # Metodo che serve per leggere la lista degli account all'interno del Database
    def leggiAccount(self):
        fileName = 'Database\Account\Account.txt'
        listAccount = File.deserializza(self, fileName)
        return listAccount


    # Metodo che permette di eliminare un Account
    def eliminaAccount(self, iDAccount):
            fileName = 'Database\Account\account.txt'
            listaccount = leggiAccount()
            for x in listaccount:
                if x.iDAccount == iDAccount:
                    listaccount.pop(index(x))
            File.serializza(fileName, listaccount)


    # Metodo per trovare un account tramite l'email dell' Account
    def trovaAccountTramiteEmail(self, email):
        listAccount = leggiAccount(self)
        for x in listAccount :
            if x.email == email:
                return listAccount(index(x))


    # Metodo per trovare un account tramite l'id dell' Account
    def trovaAccountTramiteId(self, id):
        listAccount = leggiAccount(self)
        for x in listAccount :
            if x.iDAccount == iDAccount:
                return listAccount(index(x))
            else: return None


    # Metodo che ritorna il nuovo id da assegnare all' Account da inserire
    # return = nuovo Id per l'Account
    def newID(self):
            fileName = 'Databasa\parametri.txt'
            letto = File.leggi(fileName)
            dictLetto = letto.__dict__
            newID = dictLetto['lastIDAccount'] + 1
            dictLetto['lastIDAccount'] = newId
            File.scrivi(fileName, dictLetto.__str__)
            return newId


    # etodo che rimuove un Prodotto da file e lo restituisce
    def prendiAccountDaFile(self, startfileName, id):
        #strLetto = File.leggi(startfileName)
        listAccount = File.File.deserializza(startfileName)
        popped = None
        for obj in listAccount:
            if obj.iDAccount == id:
                popped = listAccount.pop(listAccount.index(obj))
            else:
                return None
        File.File.serializza(startfileName, listAccount)
        return popped


    # Metodo che mette un Account su file
    def mettiAccountSuFile(self, fileName, obj):
        listProdotti = File.File.deserializza(fileName)
        for prodotto in listProdotti:
            if prodotto.idProdotto == obj.idProdotto:
                listProdotti.pop(listProdotti.index(obj))
        listProdotti.append(obj)
        File.serializza(fileName, listProdotti)
