import copy
from operator import index

from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from MVC.Model.SistemService.File import File


class Scaffale(ServizioInterface):


    # Costruttore della classe, create() in EA
    def __init__(self, IDProdotti, posto):
        self.ID = self.newID()
        self.IDProdotti = IDProdotti
        self.posto = posto


    # Metodo che salva lo scaffale nel database dopo averlo inizializzato
    def saveInDatabase(self):
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File.deserializza(filename)
        scaffaliList.append(self)
        File.serializza(self, filename, scaffaliList)


    # Metodo che permette di clonare un'istanza della classe
    # return Scaffale
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    #Metodo che permette di eliminare uno scaffale salvato nel database
    #return valore booleano
    def deleteInDatabase(self, ID):
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File.deserializza(filename)
        for x in scaffaliList:
            if x.ID == ID:
                scaffaliList.pop(index(x))
        File.serializza(filename, scaffaliList)


    # Metodo che ritorna il nuovo id da assegnare al Scaffale da inserire
    # return = nuovo ID per lo Scaffale
    def newID(self):
        fileName = 'Databasa\parametri.txt'
        letto = File.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDScaffale'] + 1
        dictLetto['lastIDScaffale'] = newID
        File.scrivi(fileName, dictLetto.__str__)
        return newID


