import copy
from operator import index

from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from MVC.Model.SistemService.File import File


class Scaffale(ServizioInterface):

    # Costruttore dellaClasse
    def __init__(self):
        self.idScaffale = None
        self.idProdotti = list()


    # Costruttore della classe, create() in EA
    def aggiungiScaffale(self, idProdotti):
        self.idScaffale = self.newId()
        if idProdotti != None: self.idProdotti = idProdotti
        return self.idScaffale


    # Metodo che salvalo scaffale nel database
    def inserisciScaffaleNelDatabase(self):
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File().deserializza(filename)
        scaffaliList.append(self)
        File().serializza(filename, scaffaliList)


    # Metodo che permette di clonare un'istanza della classe
    # return Scaffale
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    # Metodo che permette di eliminare uno scaffale salvato nel database
    # return valore booleano
    def deleteInDatabase(self, ID):
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File().deserializza(filename)
        for x in scaffaliList:
            if x.ID == ID:
                scaffaliList.pop(index(x))
        File().serializza(filename, scaffaliList)


    # Metodo che ritorna il nuovo id da assegnare al Scaffale da inserire
    # return = nuovo ID per lo Scaffale
    def newId(self):
        fileName = 'Databasa\parametri.txt'
        letto = File().leggi(fileName)
        dictLetto = letto.__dict__
        newId = dictLetto['lastIdScaffale'] + 1
        dictLetto['lastIdScaffale'] = newId
        File().scrivi(fileName, dictLetto.__str__)
        return newId


    # Metodo che prende  l'id di un oggetto e o sposta da un scaffale ad un'altro scaffale
    # idStart = id dello scaffale da dove spostare
    # idEnd = id dello scaffale dove mettere
    def cambiaScaffaleAProdotto(self, prodotto, idStart, idEnd):
        fileName = "Database\Scaffali\Scaffali.txt"
        listScaffali = File().deserializza(fileName)
        for scaffale in listScaffali:
            if scaffale.id == idStart:
                for ids in scaffale.idProdotti:
                    if ids == prodotto.idProdotto:
                       listScaffali.index(scaffale).idProdotti.index(ids).pop()
        for scaffale in listScaffali:
            if scaffale.id == idEnd:
                listScaffali.index(scaffale).idProdotti.append(prodotto.IDProdotto)
        prodotto.idScaffale = idEnd


    # Metodo che serve per leggere la lista degli scaffali all'interno del Database
    def recuperaListaOggetti(self):
        fileName = 'Database\Scaffali\Scaffali.txt'
        listScaffali = File().deserializza(fileName)
        return listScaffali


    # Metodo a cui viene passato un prodotto dai cui viene prelevato l'idProdotto e inserito
    # nella lista degli scaffali
    def aggiungiProdottoAScaffale(self, prodotto, idScaffale):
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File().deserializza(filename)
        for scaffale in scaffaliList:
            if scaffale.idScaffale == idScaffale:
                scaffale.idProdotti.append(prodotto.IDProdotto)
                File().serializza(filename, scaffaliList)
                return True
        return False


    # Metodo che dissocia un id di un prodotto da uno scaffale
    def dissociaProdottoDaScaffale(self, prodotto):
        listScaffali = self.recuperaListaOggetti()
        fileName = "Database\Clienti\Clienti.txt"
        for scaffale in listScaffali:
            if scaffale.idScaffale == prodotto.idAccount:
                for idProdotto in scaffale.idScaffale:
                    if idProdotto == prodotto.idProdotto:
                        scaffale.idProdotti.pop(index(idProdotto))
                        File().serializza(fileName, listScaffali)