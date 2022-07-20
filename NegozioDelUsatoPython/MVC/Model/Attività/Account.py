from MVC.Model.SistemService.File import File
import json

class Account:

    #Costruttore dell'Account , create() in EA
    def __init__(self):
        self.cliente = None
        self.nome = None
        self.cognome = None
        self.dataDiNascita = None
        self.email = None
        self.IDAccount = None
        self.IDProdotti = None
        self.numeroTelefonico = None
        self.residenza = None


    #Metodo che permette di aggiungere un Account
    def aggiungiAccount(self,cliente , nome, cognome, dataDiNascita, email,
                        IDAccount, IDProdotti, numeroTelefonico, residenza):
        self.cliente = True
        self.nome = nome
        self.cognome = cognome
        self.dataDiNascita = dataDiNascita
        self.email = email
        self.IDAccount = newID()
        self.IDProdotti = IDProdotti
        self.numeroTelefonico = numeroTelefonico
        self.residenza = residenza


    # Metodo che serve per leggere la lista degli account all'interno del Database
    def leggiAccount(self):
        fileName = 'Database\Account\account.txt'
        listAccount = File.deserializza(self, fileName)
        return listAccount

    #Metodo che permette di eliminare un Account
    def eliminaAccount(self, IDAccount):
            fileName = 'Database\Account\account.txt'
            listaccount = leggiAccount()
            for x in listaccount:
                if x.IDAccount == IDAccount:
                    listaccount.pop(index(x))
            File.serializza(fileName, listaccount)


    #Metodo per trovare un account tramite l'ID dell'account
    def trovaAccount(self, IDAccount):
        listaccount = leggiAccount(self)
        for x in listaccount :
            if x.IDAccount == IDAccount
                return listaccount(index(x))
        return None

    #Metodo per trovare un account tramite l'email dell' Account
    def trovaAccount(self, email):
        listaccount = leggiAccount(self)
        for x in listaccount :
            if x.email == email
                return listaccount(index(x))


    # Metodo che ritorna il nuovo id da assegnare all' Account da inserire
    # return = nuovo ID per l'Account
    def newID(self):
            fileName = 'Databasa\parametri.txt'
            letto = File.leggi(fileName)
            dictLetto = letto.__dict__
            newID = dictLetto['lastIDAccount'] + 1
            dictLetto['lastIDAccount'] = newID
            File.scrivi(fileName, dictLetto.__str__)
            return newID



