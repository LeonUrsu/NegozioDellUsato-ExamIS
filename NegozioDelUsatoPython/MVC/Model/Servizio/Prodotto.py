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
    def aggiungiProdotto(self, codiceCategoria, dataEsposizione, IDAccount, nomeProdotto,
                         prezzoCorrente, prezzoOriginale, statoDiVendita, IDScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataPrimoSconto = dataEsposizione + relativedelta(months=2)
        self.dataSecondoSconto = dataEsposizione + relativedelta(months=3)
        self.dataTerzoSconto = dataEsposizione + relativedelta(months=4)
        self.dataScadenza = dataEsposizione + relativedelta(months=5)
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
        fileName = 'Database\Prodotti\InVendita.txt'
        strLetto = File.leggi(fileName)
        listLetto = dictionaryDecoder(json.loads(strLetto))
        listLetto = controllaScadenzaProdotto(listLetto)
        contenuto = dictionaryEndcoder(listLetto)
        File.scrivi(fileName, contenuto.__str__)


    #Metodo che sposta un determinato prodotto all'interno della memoria quando il suo stato è in cambiamento
    #return valore booleano
    def spostaProdotto(self, id, start, end):
        startfileName = f'Database\Prodotti\{start}.txt'
        endfileName = f'Database\Prodotti\{end}.txt'
        strLetto = File.leggi(startfileName)
        list = dictionaryDecoder(json.loads(strletto))
        for obj in list:
            if obj.IDProdotto == id:
                popped = list.pop(list.index(obj))
            else:
                return False
        contenuto = dictionaryEndcoder(list)
        File.scrivi(fileName, contenuto.__str__)
        strLetto = File.leggi(endfileName)
        list = dictionaryDecoder(json.loads(strletto))
        list.append(popped)
        contenuto = dictionaryEndcoder(list)
        File.scrivi(fileName, contenuto.__str__)
        return True
        

    #Metodo che permette la vendita di un prodotto, lo stato dell'oggetto passa a venduto e viene spostato
    #dove vendono archviati tutti gli oggetti venduti nel database
    #return valore booleano
    def vendiProdotto(self):
        todo


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    #contenuto list
    #return dictionary
    def dictionaryEndcoder(self, contenuto):
        dict = json.dumps([self.__dict__ for self in contenuto])
        return dict


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    #contenuto dictionary
    #return list
    def dictionaryDecoder(self, contenuto):
        return [Test(x['var'], x['var2']) for x in letto]


    #Metodo che ritorna il nuovo id da assegnare al prodotto da inserire
    def getNewIDProdotto(self):
        fileName = 'Databasa\parametri.txt'
        letto = File.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDProdotto']+1
        dictLetto['lastIDProdotto'] = newID
        File.scrivi(fileName,dictLetto.__str__)
        return newID


    #Metodo che controlla le date di scadenza e di sconto degli oggetti

    def controllaScadenzaProdotto(self, listLetto):
        date_format = '%d/%m/%Y'
        today = date.today()
        dateToday = today.strftime(date_format)
        for obj in listLetto:
            if obj.dataScadenza <= dateToday:
                scadenza()todo
            elif obj.dataTerzoSconto <= dateToday:
                sconta(obj, 50)
            elif obj.dataSecondoSconto <= dateToday:
                sconta(obj, 40)
            elif obj.dataPrimoSconto <= dateToday:
                sconta(obj, 30)
        return listLetto
