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
                         prezzoOriginale, statoDiVendita, IDScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataPrimoSconto = dataEsposizione + relativedelta(months=2)
        self.dataSecondoSconto = dataEsposizione + relativedelta(months=3)
        self.dataTerzoSconto = dataEsposizione + relativedelta(months=4)
        self.dataScadenza = dataEsposizione + relativedelta(months=5)
        self.IDAccount = IDAccount
        self.IDProdotto = Prodotto.getNewIDProdotto()
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoOriginale
        self.prezzoOriginale = prezzoOriginale
        self.statoDiVendita = statoDiVendita
        self.IDScaffale = IDScaffale



    #Metodo che permette di clonare un'istanza della classe
    #return Prodotto
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


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
        obj = prendiProdottoDaFile(startfileName, id)
        mettiProdottoSuFile(endfileName, obj)
        return obj.prezzoCorrente


    #Metodo che rimuove un Prodotto da file e lo restituisce
    def prendiProdottoDaFile(self, fileName, id):
        strLetto = File.leggi(startfileName)
        list = dictionaryDecoder(json.loads(strletto))
        popped = None
        for obj in list:
            if obj.IDProdotto == id:
                popped = list.pop(list.index(obj))
            else:
                return False
        contenuto = dictionaryEndcoder(list)
        File.scrivi(fileName, contenuto.__str__)
        return popped


    #Metodo che mette un Prodotto su file
    def mettiProdottoSuFile(self, fileName, obj):
        strLetto = File.leggi(endfileName)
        list = dictionaryDecoder(json.loads(strletto))
        list.append(obj)
        contenuto = dictionaryEndcoder(list)
        File.scrivi(fileName, contenuto.__str__)


    #Metodo che permette la vendita di un prodotto, lo stato dell'oggetto passa a venduto e viene spostato
    #dove vendono archviati tutti gli oggetti venduti nel database
    #return valore booleano
    def vendiProdotto(self, id):
        start = 'Database\Prodotti\InVendita.txt'
        end = 'Database\Prodotti\Venduti.txt'
        prezzoCorrente = spostaProdotto(id, start, end)
        infoProdotto = {}
        infoProdotto['prezzoCorrente'] = prezzoCorrente
        infoProdotto['id'] = id
        return infoProdotto


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
    #listLetto = lista dei prodotti in python
    #return = lista dei prodotti in python dopo l'eventuale sconto """
    def controllaScadenzaProdotto(self, listLetto):
        date_format = '%d/%m/%Y'
        today = date.today()
        dateToday = today.strftime(date_format)
        for obj in listLetto:
            if obj.dataScadenza <= dateToday:
                scadenza(obj.IDProdotto)
            elif obj.dataTerzoSconto <= dateToday:
                obj.prezzoCorrente = sale(prezzoOriginale, 50)
            elif obj.dataSecondoSconto <= dateToday:
                obj.prezzoCorrente = sale(prezzoOriginale, 40)
            elif obj.dataPrimoSconto <= dateToday:
                obj.prezzoCorrente = sale(prezzoOriginale, 30)
        return listLetto


    #Metodo che sconta il prezzo di un prodotto in base al valore di sconto
    #prezzoOriginale = prezzo del prodotto al momento del inserimento nel sistema
    #prezzoCorrente = prezzo del prodotto dopo lo sconto rispetto al prezzoOriginale
    #return = prezzoCorrente del prodotto
    def sale(self, prezzoOriginale, valore):
        prezzoCorrente = prezzoOriginale * (valore/100)
        return prezzoCorrente


    #metodo che gestisce la scadenza di un oggetto spostandolo dai prodotti in vendita
    #ai prodotti scaduti
    #id = id prodotto da spostare
    def scadenza(self, id):
        start = 'Database\Prodotti\InVendita.txt'
        end = 'Database\Prodotti\Scaduti.txt'
        spostaProdotto(id, start, end)

