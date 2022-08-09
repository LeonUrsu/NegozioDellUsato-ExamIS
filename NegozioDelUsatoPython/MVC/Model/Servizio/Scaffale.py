import copy
from operator import index

from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from MVC.Model.SistemService.File import File


class Scaffale(ServizioInterface):


    def __init__(self):
        pass

    # Costruttore della classe, create() in EA
    def __init__(self, idProdotti, posto):
        file = File()
        self.id = self.newId()
        self.idProdotti = idProdotti
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = file.deserializza(filename)
        scaffaliList.append(self)
        file.serializza(filename, scaffaliList)


    # Metodo che permette di clonare un'istanza della classe
    # return Scaffale
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    #Metodo che permette di eliminare uno scaffale salvato nel database
    #return valore booleano
    def deleteInDatabase(self, ID):
        filename = 'Database\Scaffali\Scaffali.txt'
        file = File()
        scaffaliList = file.deserializza(filename)
        for x in scaffaliList:
            if x.ID == ID:
                scaffaliList.pop(index(x))
        file.serializza(filename, scaffaliList)


    # Metodo che ritorna il nuovo id da assegnare al Scaffale da inserire
    # return = nuovo ID per lo Scaffale
    def newId(self):
        file = File()
        fileName = 'Databasa\parametri.txt'
        letto = file.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDScaffale'] + 1
        dictLetto['lastIDScaffale'] = newID
        file.scrivi(fileName, dictLetto.__str__)
        return newID


    # Metodo che prende  l'id di un oggetto e o sposta da un scaffale ad un'altro scaffale
    # idStart = id dello scaffale da dove spostare
    # idEnd = id dello scaffale dove mettere
    def cambiaScaffale(self, prodotto, idStart, idEnd):
        indexStart = 0
        fileName = "Database\Scaffali\Scaffali.txt"
        file = File()
        listScaffali = file.deserializza(fileName)
        for scaffale in listScaffali:
            if scaffale.id == idStart:
                #indexStart = listScaffali.index(scaffale)
                for ids in scaffale.idProdotti:
                    if ids == prodotto.IDProdotto:
                       listScaffali.index(scaffale).idProdotti.index(ids).pop()
        for scaffale in listScaffali:
            if scaffale.id == idEnd:
                listScaffali.index(scaffale).idProdotti.append(prodotto.IDProdotto)
        prodotto.idScaffale = idEnd