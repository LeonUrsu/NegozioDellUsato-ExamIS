import copy
from operator import index

from Database.PathDatabase import PathDatabase
from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from MVC.Model.SistemService.File import File


class Scaffale(ServizioInterface):

    # Costruttore dellaClasse
    def __init__(self):
        pass

    # Costruttore della classe, create() in EA
    def aggiungiScaffale(self, nomeScaffale, idProdotti):
        self.nomeScaffale = nomeScaffale
        self.idScaffale = self.newId()
        if idProdotti != None:
            self.idProdotti = idProdotti
        else:
            self.idProdotti = list()
        return self.idScaffale

    # Metodo che salvalo scaffale nel database
    def inserisciScaffaleNelDatabase(self):
        filename = PathDatabase().scaffaliTxt
        scaffaliList = File().deserializza(filename)
        scaffaliList.append(self)
        File().serializza(filename, scaffaliList)

    # Metodo che permette di clonare un'istanza della classe
    # return Scaffale
    def clone(self):
        deepCopy = copy.deepcopy(self)
        return deepCopy

    # Metodo che permette di eliminare uno scaffale salvato nel database
    # return valore booleano
    def deleteInDatabase(self, ID):
        filename = PathDatabase().scaffaliTxt
        scaffaliList = File().deserializza(filename)
        for x in scaffaliList:
            if x.ID == ID:
                scaffaliList.pop(index(x))
        File().serializza(filename, scaffaliList)

    # Metodo che ritorna il nuovo id da assegnare al Scaffale da inserire
    # return = nuovo ID per lo Scaffale
    def newId(self):
        fileName = PathDatabase().parametriTxt
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
        fileName = PathDatabase().scaffaliTxt
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
        fileName = PathDatabase().scaffaliTxt
        listScaffali = File().deserializza(fileName)
        return listScaffali

    # Metodo a cui viene passato un prodotto dai cui viene prelevato l'idProdotto e inserito
    # nella lista degli scaffali
    def associaProdottoAScaffale(self, prodotto):
        filename = PathDatabase().scaffaliTxt
        scaffaliList = File().deserializza(filename)
        for scaffale in scaffaliList:
            if scaffale.nomeScaffale == prodotto.nomeScaffale:
                scaffale.idProdotti.append(prodotto.IdProdotto)
                File().serializza(filename, scaffaliList)
                return True
        self.__init__().aggiungiScaffale(prodotto.nomeScaffale, None)
        return False

    # Metodo che dissocia un id di un prodotto da uno scaffale
    def dissociaProdottoDaScaffale(self, prodotto):
        listScaffali = self.recuperaListaOggetti()
        fileName = PathDatabase().accountTxt
        for scaffale in listScaffali:
            if scaffale.nomeScaffale == prodotto.nomeScaffale:
                for idProdotto in scaffale.idProdotti:
                    if idProdotto == prodotto.idProdotto:
                        scaffale.idProdotti.pop(index(idProdotto))
                        File().serializza(fileName, listScaffali)

    # Metodo per trovare il id scaffale tramite nomeScaffale
    def trovaScaffaleConNome(self, nomeScaffale):
        lista = self.recuperaListaOggetti()
        for obj in lista:
            if obj.nomeScaffale == nomeScaffale:
                return obj.idScaffale
        return None
