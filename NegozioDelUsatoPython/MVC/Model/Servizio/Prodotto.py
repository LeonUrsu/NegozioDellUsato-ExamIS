import datetime
from types import SimpleNamespace

from MVC.Model.SistemService.File import File
import json

#CLasse Prodotto che rappresenta il prodotto con le sue caratteristiche che verrà esposto nel negozio
from MVC.Model.Interfacce.DictionaryToPythonObject import JsonObjectToPythonObject


class Prodotto(JsonObjectToPythonObject):


    #Costruttore della classe, create() in EA
    def __init__(self):
        self.codiceCategoria = None
        self.dataEsposizione = None
        self.dataScadenza = None
        self.IDAccount = None
        self.IDProdotto = None
        self.nomeProdotto = None
        self.prezzoCorrente = None
        self.prezzoOriginale = None
        self.statoDiVendita = None
        self.IDScaffale = None


    #Metodo per aggiungere i valori all'istanza creata della classe e salvarla nel database
    def aggiungiProdotto(self, codiceCategoria, dataEsposizione, dataScadenza, IDAccount, nomeProdotto,
                         prezzoCorrente, prezzoOriginale, statoDiVendita, IDScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataScadenza = dataScadenza
        self.IDAccount = IDAccount
        self.IDProdotto = Prodotto.getNewIDProdotto()
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoCorrente
        self.prezzoOriginale = prezzoOriginale
        self.statoDiVendita = statoDiVendita
        self.IDScaffale = IDScaffale



    #Metodo che permette di clonare un'istanza della classe
    #return Prodotto
    def clone(self):
        todo


    #Metodo che entra in azione quanado l'oggetto matura un determinato tempo di esistenza nel
    #negozio e viene applicato dolo agli oggetti che sono esposti alla vendita
    #return valore booleano
    def scontaProdotti(self):
        letto = File.leggi('Database\Prodotti\InVendita.txt')
        dictLetto = dictionaryEndcoder(self, letto)
        for i



    #Metodo che sposta un determinato prodotto all'interno della memoria quando il suo stato è in cambiamento
    #return valore booleano
    def spostaProdotto(self):
        todo


    #Metodo che permette la vendita di un prodotto, lo stato dell'oggetto passa a venduto e viene spostato
    #dove vendono archviati tutti gli oggetti venduti nel database
    #return valore booleano
    def vendiProdotto(self):
        todo


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def dictionaryEndcoder(self, contenuto):
        json_string = json.dumps([self.__dict__ for self in contenuto])
        return json_string


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def dictionaryDecoder(self, contenuto):
        pyLetto = json.loads(contenuto, object_hook=lambda d: SimpleNamespace(**d))
        return pyLetto


    #Metodo che ritorna il nuovo id da assegnare al prodotto da inserire
    def getNewIDProdotto(self):
        fileName = 'Databasa\parametri.txt'
        letto = File.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDProdotto']+1
        dictLetto['lastIDProdotto'] = newID
        File.scrivi(fileName,dictLetto.__str__)
        return newID
