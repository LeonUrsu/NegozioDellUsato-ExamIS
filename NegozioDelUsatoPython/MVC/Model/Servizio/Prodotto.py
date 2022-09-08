# CLasse Prodotto che rappresenta il prodotto con le sue caratteristiche che verrà esposto nel negozio
import copy
import json

from operator import index

from Database.PathDatabase import PathDatabase

from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from datetime import date
from dateutil.relativedelta import relativedelta

from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Scaffale import Scaffale
from MVC.Model.SistemService.File import File


class Prodotto(ServizioInterface):

    # Costruttore della classe, create() in EA
    def __init__(self):
        pass

    # Metodo per aggiungere i valori all'istanza creata della classe
    def aggiungiProdotto(self, codiceCategoria, dataEsposizione, idAccount, nomeProdotto,
                         prezzoOriginale, idScaffale):
        self.codiceCategoria = codiceCategoria
        self.dataEsposizione = dataEsposizione
        self.dataPrimoSconto = dataEsposizione + relativedelta(months=2)
        self.dataSecondoSconto = dataEsposizione + relativedelta(months=3)
        self.dataTerzoSconto = dataEsposizione + relativedelta(months=4)
        self.dataScadenza = dataEsposizione + relativedelta(months=5)
        self.idAccount = idAccount
        #TODO fare controllo su id account
        self.idProdotto = Prodotto().newId()
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoOriginale
        self.prezzoOriginale = prezzoOriginale
        self.idScaffale = idScaffale

    # Metodo che viene richiamato su un prodotto e serve per inserirlo nella
    # lista degli oggetti in vendita
    def inserisciOggettoNelDatabase(self):
        filename = PathDatabase().inVenditaTxt
        Scaffale().associaProdottoAScaffale(self)
        Categoria().aggiungiProdottiInCategoria(self)
        Account().associaProdottoAdAccount(self)
        self.mettiOggettoSuListaNelFile(filename)

    # Metodo che permette di clonare un'istanza della classe
    # return Prodotto
    def clone(self):
        deepCopy = copy.deepcopy(self)
        return deepCopy

    # Metodo che elimina i prodotti nel database
    def eliminaProdotto(self, idProdotto):
        listPath = self.pathList()
        for path in listPath:
            listProdotti = File().deserializza(path)
            for prodotto in listProdotti:
                if prodotto.idProdotto == idProdotto:
                    eliminato = listProdotti.pop(listProdotti.index(prodotto))
                    end = PathDatabase().eliminatiTxt
                    Prodotto().spostaProdotto(prodotto.idProdotto, path, end)
                    Account().dissociaProdottoDaAccount(eliminato)
                    Categoria().diminuisciProdottiInCategoria(eliminato)
                    Scaffale().dissociaProdottoDaScaffale(eliminato)
                    return True
            return False

    # Metodo che entra in azione quanado l'oggetto matura un determinato tempo di esistenza nel
    # negozio e viene applicato dolo agli oggetti che sono esposti alla vendita
    # return valore booleano
    def scontaProdotti(self):
        fileName = PathDatabase().inVenditaTxt
        listProdotti = File().deserializza(fileName)
        listProdottiAggiornata = self.controllaScadenzaProdotto(listProdotti)
        file = File()
        file.serializza(fileName, listProdottiAggiornata)

    # Metodo che sposta un determinato prodotto all'interno della memoria quando il suo stato è in cambiamento
    # return valore booleano
    def spostaProdotto(self, id, start, end):
        obj = self.rimuoviOggettoDaFile(start, id)
        obj.mettiOggettoSuListaNelFile(end)
        return obj

    def trovaOggettoTramiteId(self, id):
        listaFile = self.recuperaListOfLists()
        for listProdotti in listaFile:
            for prodotto in listProdotti:
                if prodotto.idProdotto == id:
                    return listProdotti[listProdotti.index(prodotto)]
        return None


    # Metodo che rimuove un Prodotto da file e lo restituisce, la lista verrà serializzata su file senza
    # l'oggetto rimosso precedentemente
    def rimuoviOggettoDaFile(self, fileName, id):
        listProdotti = File().deserializza(fileName)
        popped = None
        for prodotto in listProdotti:
            if prodotto.idProdotto == id:
                popped = prodotto
                listProdotti.pop(listProdotti.index(prodotto))
        File().serializza(fileName, listProdotti)
        return popped

    # Metodo che mette un Prodotto su file
    def mettiOggettoSuListaNelFile(self, fileName):
        listProdotti = File().deserializza(fileName)
        for prodotto in listProdotti:
            if prodotto.idProdotto == self.idProdotto:
                listProdotti.pop(listProdotti.index(prodotto))
        listProdotti.append(self)
        File().serializza(fileName, listProdotti)

    """    # Metodo che permette la vendita di un prodotto, lo stato dell'oggetto passa a venduto e viene spostato
    # dove vendono archviati tutti gli oggetti venduti nel database
    # return dizionario con prezzo e ID
    def vendiProdotto(self, id):
        start = PathDatabase().inVenditaTxt
        end = PathDatabase().vendutiTxt
        prodotto = self.spostaProdotto(id, start, end)
        prezzoCorrente = prezzoprezzoCorrente
        return infoProdotto"""

    # Metodo che aggiorna un prodotto in base ai parametri passati dalla classe amministratore
    def aggiornaProdotto(self, codiceCategoria, dataEsposizione,
                         nomeProdotto, prezzoOriginale, idScaffale, idProdotto):
        fileName = PathDatabase().inVenditaTxt
        prodottoTrovato = Prodotto().rimuoviOggettoDaFile(fileName, idProdotto)
        if codiceCategoria != prodottoTrovato.codiceCategoria:
            prodottoTrovato.codiceCategoria = codiceCategoria
            Categoria().aggiornaCategoriaProdotto(prodottoTrovato, prodottoTrovato.codiceCategoria, codiceCategoria)
        if dataEsposizione != prodottoTrovato.dataEsposizione: prodottoTrovato.dataEsposizione = dataEsposizione
        if nomeProdotto != prodottoTrovato.nomeProdotto: prodottoTrovato.nomeProdotto = nomeProdotto
        if prezzoOriginale != prodottoTrovato.prezzoOriginale: prodottoTrovato.prezzoOriginale = prezzoOriginale
        if idScaffale != prodottoTrovato.idScaffale:
            prodottoTrovato.idScaffale = idScaffale
            Scaffale().cambiaScaffaleAProdotto(prodottoTrovato, prodottoTrovato.idProdotto, idScaffale)
        prodottoTrovato.mettiOggettoSuListaNelFile(fileName)

    # Metodo che ritorna il nuovo id da assegnare al prodotto da inserire
    # return = nuovo ID per il Prodotto
    def newId(self):
        fileName = PathDatabase().parametriTxt
        letto = File().leggi(fileName)
        dictLetto = json.loads(letto)
        newId = dictLetto['lastIdProdotto'] + 1
        dictLetto['lastIdProdotto'] = newId
        File().scrivi(fileName, json.dumps(dictLetto))
        return newId

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
        prezzoCorrente = prezzoOriginale * (valore / 100)
        return prezzoCorrente

    # metodo che gestisce la scadenza di un oggetto spostandolo dai prodotti in vendita
    # ai prodotti scaduti
    # id = id prodotto da spostare
    def scadenza(self, id):
        start = PathDatabase().inVenditaTxt
        end = PathDatabase().scadutiTxt
        self.spostaProdotto(id, start, end)

    # Metodo che ritorna un lista con i percorsi dei vari file
    def pathList(self):
        fileName1 = PathDatabase().inVenditaTxt
        fileName2 = PathDatabase().vendutiTxt
        fileName3 = PathDatabase().scadutiTxt
        listPath = list()
        listPath.append(fileName1)
        listPath.append(fileName2)
        listPath.append(fileName3)
        return listPath

    # Metodo per recuperare la lista dei prodotti tramite un fileName
    def recuperaListaOggetti(self, fileName):
        return File().deserializza(fileName)

    def dissociaProdottiDaAccount(self, account):
        inVendita = PathDatabase().inVenditaTxt
        venduti = PathDatabase().vendutiTxt
        scaduti = PathDatabase().scadutiTxt
        listTotale = self.recuperaListOfLists()
        for list in listTotale:
            for prodotto in list:
                if prodotto.idAccount == account.idAccount:
                    prodotto.idAccount = None
        File().serializza(inVendita, listTotale[0])
        File().serializza(venduti, listTotale[1])
        File().serializza(scaduti, listTotale[2])
        return True

    # Metodo che recupera le liste dai file e li mette su una lista
    def recuperaListOfLists(self):
        listProdottiInVendita = self.recuperaListaOggetti(PathDatabase().inVenditaTxt)
        listProdottiVenduti = self.recuperaListaOggetti(PathDatabase().vendutiTxt)
        listProdottiScaduti = self.recuperaListaOggetti(PathDatabase().scadutiTxt)
        listTotale = list()
        listTotale.append(listProdottiInVendita)
        listTotale.append(listProdottiVenduti)
        listTotale.append(listProdottiScaduti)
        return listTotale

    # se il prodotto non ha id cliente dee essere comunnque venduto#####################################################################################################################
