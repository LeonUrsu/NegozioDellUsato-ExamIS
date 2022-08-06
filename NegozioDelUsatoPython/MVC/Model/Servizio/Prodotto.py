#CLasse Prodotto che rappresenta il prodotto con le sue caratteristiche che verrà esposto nel negozio
import copy
import json

from MVC.Model.Interfacce.DictionaryToPythonObject import JsonObjectToPythonObject
from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from datetime import date
from dateutil.relativedelta import relativedelta

from MVC.Model.SistemService.File import File


class Prodotto(ServizioInterface):


    #Costruttore della classe, create() in EA
    def __init__(self):
        self.codiceCategoria = None
        self.dataEsposizione = None
        self.dataScadenza = None
        self.idAccount = None
        self.IDProdotto = None
        self.nomeProdotto = None
        self.prezzoCorrente = None
        self.prezzoOriginale = None
        self.statoDiVendita = None
        self.IDScaffale = None


    # Costruttore della classe, create() in EA
    def __init__(self, codiceCategoria, dataEsposizione, IDAccount, nomeProdotto,
                         prezzoOriginale, statoDiVendita, IDScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataPrimoSconto = dataEsposizione + relativedelta(months=2)
        self.dataSecondoSconto = dataEsposizione + relativedelta(months=3)
        self.dataTerzoSconto = dataEsposizione + relativedelta(months=4)
        self.dataScadenza = dataEsposizione + relativedelta(months=5)
        self.IDAccount = IDAccount
        self.IDProdotto = Prodotto.newID()
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoOriginale
        self.prezzoOriginale = prezzoOriginale
        self.statoDiVendita = statoDiVendita
        self.IDScaffale = IDScaffale


    # Metodo per aggiungere i valori all'istanza creata della classe
    def aggiungiProdotto(self, codiceCategoria, dataEsposizione, IDAccount, nomeProdotto,
                         prezzoOriginale, statoDiVendita, IDScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataPrimoSconto = dataEsposizione + relativedelta(months=2)
        self.dataSecondoSconto = dataEsposizione + relativedelta(months=3)
        self.dataTerzoSconto = dataEsposizione + relativedelta(months=4)
        self.dataScadenza = dataEsposizione + relativedelta(months=5)
        self.IDAccount = IDAccount
        self.IDProdotto = Prodotto.newID()
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoOriginale
        self.prezzoOriginale = prezzoOriginale
        self.statoDiVendita = statoDiVendita
        self.IDScaffale = IDScaffale


    # Metodo che permette di clonare un'istanza della classe
    # return Prodotto
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    # Metodo che entra in azione quanado l'oggetto matura un determinato tempo di esistenza nel
    # negozio e viene applicato dolo agli oggetti che sono esposti alla vendita
    # return valore booleano
    def scontaProdotti(self):
        fileName = 'Database\Prodotti\InVendita.txt'
        listProdotti = File.deserializza(fileName)
        listProdottiAggiornata = self.controllaScadenzaProdotto(listProdotti)
        File.File.serializza(fileName, listProdottiAggiornata)


    # Metodo che sposta un determinato prodotto all'interno della memoria quando il suo stato è in cambiamento
    # return valore booleano
    def spostaProdotto(self, id, start, end):
        startfileName = f'Database\Prodotti\{start}.txt'
        endfileName = f'Database\Prodotti\{end}.txt'
        obj = self.prendiProdottoDaFile(startfileName, id)
        self.mettiProdottoSuFile(endfileName, obj)
        return obj.prezzoCorrente


    # etodo che rimuove un Prodotto da file e lo restituisce
    def prendiProdottoDaFile(self, startfileName, id):
        #strLetto = File.leggi(startfileName)
        listProdotti = File.File.deserializza(startfileName)
        popped = None
        for obj in listProdotti:
            if obj.IDProdotto == id:
                popped = listProdotti.pop(listProdotti.index(obj))
            else:
                return None
        File.File.serializza(startfileName, listProdotti)
        return popped


    # Metodo che mette un Prodotto su file
    def mettiProdottoSuFile(self, fileName, obj):
        listProdotti = File.File.deserializza(fileName)
        for prodotto in listProdotti:
            if prodotto.idProdotto == obj.idProdotto:
                listProdotti.pop(listProdotti.index(obj))
        listProdotti.append(obj)
        File.serializza(fileName, listProdotti)


    # Metodo che permette la vendita di un prodotto, lo stato dell'oggetto passa a venduto e viene spostato
    # dove vendono archviati tutti gli oggetti venduti nel database
    # return dizionario con prezzo e ID
    def vendiProdotto(self, id):
        start = 'Database\Prodotti\InVendita.txt'
        end = 'Database\Prodotti\Venduti.txt'
        prezzoCorrente = self.spostaProdotto(id, start, end)
        infoProdotto = {}
        infoProdotto['prezzoCorrente'] = prezzoCorrente
        infoProdotto['id'] = id
        infoProdotto['Prodotto'] = self.nomeProdotto
        return infoProdotto


    # Metodo che ritorna il nuovo id da assegnare al prodotto da inserire
    # return = nuovo ID per il Prodotto
    def newID(self):
        fileName = 'Databasa\parametri.txt'
        letto = File.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDProdotto']+1
        dictLetto['lastIDProdotto'] = newID
        File.scrivi(fileName, dictLetto.__str__)
        return newID


    # Metodo che controlla le date di scadenza e di sconto degli oggetti
    # listLetto = lista dei prodotti in python
    # return = lista dei prodotti in python dopo l'eventuale sconto """
    def controllaScadenzaProdotto(self, listLetto):
        date_format = '%d/%m/%Y'
        today = date.today()
        dateToday = today.strftime(date_format)
        for obj in listLetto:
            if obj.dataScadenza <= dateToday:
                self.scadenza(obj.IDProdotto)
            elif obj.dataTerzoSconto <= dateToday:
                obj.prezzoCorrente = self.sale(self.prezzoOriginale, 50)
            elif obj.dataSecondoSconto <= dateToday:
                obj.prezzoCorrente = self.sale(self.prezzoOriginale, 40)
            elif obj.dataPrimoSconto <= dateToday:
                obj.prezzoCorrente = self.sale(self.prezzoOriginale, 30)
        return listLetto


    # Metodo che sconta il prezzo di un prodotto in base al valore di sconto
    # prezzoOriginale = prezzo del prodotto al momento del inserimento nel sistema
    # prezzoCorrente = prezzo del prodotto dopo lo sconto rispetto al prezzoOriginale
    # return = prezzoCorrente del prodotto
    def sale(self, prezzoOriginale, valore):
        prezzoCorrente = prezzoOriginale * (valore/100)
        return prezzoCorrente


    # metodo che gestisce la scadenza di un oggetto spostandolo dai prodotti in vendita
    # ai prodotti scaduti
    # id = id prodotto da spostare
    def scadenza(self, id):
        start = 'Database\Prodotti\InVendita.txt'
        end = 'Database\Prodotti\Scaduti.txt'
        self.spostaProdotto(id, start, end)