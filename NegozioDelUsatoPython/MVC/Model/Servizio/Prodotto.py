import datetime
import MVC.Model.SistemService.File
import json

#CLasse Prodotto che rappresenta il prodotto con le sue caratteristiche che verrà esposto nel negozio
from MVC.Model.Interfacce.DictionaryToPythonObject import JsonObjectToPythonObject


class Prodotto():


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
    def aggiungiProdotto(self, codiceCategoria, dataEsposizione, dataScadenza, IDAccount, IDProdotto, nomeProdotto,
                         prezzoCorrente, prezzoOriginale, statoDiVendita, IDScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataScadenza = dataScadenza
        self.IDAccount = IDAccount
        self.IDProdotto = IDProdotto
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoCorrente
        self.prezzoOriginale = prezzoOriginale
        self.statoDiVendita = statoDiVendita
        self.IDScaffale = IDScaffale
        letto = MVC.File()


    #Metodo che permette di clonare un'istanza della classe
    #return Prodotto
    def clone(self):
        todo


    #Metodo che entra in azione quanado l'oggetto matura un determinato tempo di esistenza nel
    #negozio e viene applicato dolo agli oggetti che sono esposti alla vendita
    #return valore booleano
    def scontaProdotto(self):
        todo


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
    def DictionaryEndcoder(self, object):
        
        dictObject = object.__dict__
        MVC.File.scrivi('Database\Prodotti\InVendita', dictObject)


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def DictionaryDecoder(self):
        letto = File
        ProdottoObj = json.loads(json.dumps(dict1), object_hook=Prodotto)
