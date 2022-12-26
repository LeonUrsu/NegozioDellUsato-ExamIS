# CLasse Prodotto che rappresenta il prodotto con le sue caratteristiche che verrà esposto nel negozio
import json
from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Scaffale import Scaffale
from MVC.Model.SistemService.File import File


class Prodotto(ServizioInterface):

    # Costruttore della classe, create() in EA
    def __init__(self):
        pass

    # Metodo per aggiungere i valori all'istanza creata della classe
    def aggiungiProdotto(self, idCategoria, dataEsposizione, idAccount, nomeProdotto,
                         prezzoOriginale, nomeScaffaleLe, nomeCategoria):
        self.idCategoria = idCategoria
        self.nomeCategoria = nomeCategoria
        self.dataEsposizione = dataEsposizione
        self.idAccount = idAccount
        self.dataPrimoSconto = dataEsposizione + relativedelta(months=2)
        self.dataSecondoSconto = dataEsposizione + relativedelta(months=3)
        self.dataTerzoSconto = dataEsposizione + relativedelta(months=4)
        self.dataScadenza = dataEsposizione + relativedelta(months=5)
        self.idProdotto = Prodotto().newId()
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoOriginale
        self.prezzoOriginale = prezzoOriginale
        self.nomeScaffale = nomeScaffaleLe

    # Metodo che viene richiamato su un prodotto e serve per inserirlo nella
    # lista degli oggetti in vendita
    def associaOggettoAdOggetti(self):
        Scaffale().associaProdottoAScaffale(self)
        Categoria().aggiungiProdottiInCategoria(self)
        Account().associaProdottoAdAccount(self)
        self.mettiOggettoSuListaNelFile()

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
                    #Scaffale().dissociaProdottoDaScaffale(eliminato)
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
        obj = self.rimuoviOggettoDaFileName(start, id)
        obj.mettiOggettoSuListaNelFileName(end)
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
    def rimuoviOggettoDaFileName(self, fileName, id):
        listProdotti = File().deserializza(fileName)
        popped = None
        for prodotto in listProdotti:
            if prodotto.idProdotto == id:
                popped = prodotto
                listProdotti.pop(listProdotti.index(prodotto))
        File().serializza(fileName, listProdotti)
        return popped

    # Metodo che mette un Prodotto su file
    def mettiOggettoSuListaNelFile(self):
        fileName = PathDatabase.inVenditaTxt
        listProdotti = File().deserializza(fileName)
        for prodotto in listProdotti:
            if prodotto.idProdotto == self.idProdotto:
                listProdotti.pop(listProdotti.index(prodotto))
        listProdotti.append(self)
        File().serializza(fileName, listProdotti)

    # Metodo che mette un Prodotto su file
    def mettiOggettoSuListaNelFileName(self, fileName):
        listProdotti = File().deserializza(fileName)
        for prodotto in listProdotti:
            if prodotto.idProdotto == self.idProdotto:
                listProdotti.pop(listProdotti.index(prodotto))
        listProdotti.append(self)
        File().serializza(fileName, listProdotti)

    # Metodo che aggiorna un prodotto in base ai parametri passati dalla classe amministratore
    # idCategoria
    def aggiornaProdotto(self, nomeCategoria, dataEsposizione,
                         nomeProdotto, prezzoCorrente, nomeScaffaleLe, idProdotto):
        fileName = PathDatabase().inVenditaTxt
        prodottoTrovato = Prodotto().rimuoviOggettoDaFileName(fileName, idProdotto)
        if nomeCategoria != prodottoTrovato.idCategoria and nomeCategoria != "":
            prodottoTrovato.nomeCategoria = nomeCategoria
            Categoria().aggiornaCategoriaProdotto(prodottoTrovato.nomeCategoria, nomeCategoria)
        if dataEsposizione != prodottoTrovato.dataEsposizione and dataEsposizione != None:
            prodottoTrovato.dataEsposizione = dataEsposizione
        if nomeProdotto != prodottoTrovato.nomeProdotto and nomeProdotto != "":
            prodottoTrovato.nomeProdotto = nomeProdotto
        if prezzoCorrente != prodottoTrovato.prezzoCorrente and prezzoCorrente != "":
            prodottoTrovato.prezzoCorrente = prezzoCorrente
        idScaffale = Scaffale().trovaScaffaleConNome(nomeScaffaleLe)
        if nomeScaffaleLe != prodottoTrovato.nomeScaffale and nomeScaffaleLe != "":
            prodottoTrovato.nomeScaffaleLe = nomeScaffaleLe
            Scaffale().cambiaScaffaleAProdotto(prodottoTrovato, prodottoTrovato.idProdotto, idScaffale)
        prodottoTrovato.mettiOggettoSuListaNelFileName(fileName)
        return prodottoTrovato

    # Metodo che ritorna il nuovo id da assegnare al prodotto da inserire
    # return = nuovo ID per il Prodotto
    def newId(self):
        fileName = PathDatabase().parametriTxt
        letto = File().leggi(fileName)
        dictLetto = json.loads(letto)
        newId = int(dictLetto['lastIdAccount'] + 1)
        dictLetto['lastIdProdotto'] = newId
        File().scrivi(fileName, json.dumps(dictLetto))
        return newId

    # Metodo che controlla le date di scadenza e di sconto degli oggetti
    # listLetto = lista dei prodotti in python
    # return = lista dei prodotti in python dopo l'eventuale sconto
    def controllaScadenzaProdotto(self, listLetto):
        dateToday = datetime.today().date()
        for obj in listLetto:
            if obj.dataScadenza.date() <= dateToday:
                self.scadenza(obj.IDProdotto)
            elif obj.dataTerzoSconto.date() <= dateToday:
                obj.prezzoCorrente = self.sale(self.prezzoOriginale, 50)
            elif obj.dataSecondoSconto.date() <= dateToday:
                obj.prezzoCorrente = self.sale(self.prezzoOriginale, 40)
            elif obj.dataPrimoSconto.date() <= dateToday:
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
    def scadenza(self, id): # TODO si puo modificare per più efficienza
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

    # Metodo per recuperare la lista degli oggetti in vendita
    def recuperaListaProdottiInVendita(self):
        return File().deserializza(PathDatabase.inVenditaTxt)

    # Metodo per recuperare la lista degli oggetti eliminati
    def recuperaListaProdottiEliminati(self):
        return File().deserializza(PathDatabase.eliminatiTxt)

    # Metodo per recuperare la lista degli oggetti scaduti
    def recuperaListaProdottiScaduti(self):
        return File().deserializza(PathDatabase.scadutiTxt)

    # Metodo per recuperare la lista degli oggetti venduti
    def recuperaListaProdottiVenduti(self):
        return File().deserializza(PathDatabase.vendutiTxt)

    # Metodo per recuperare la lista dei prodotti tramite un fileName
    def recuperaListaOggetti(self):
        return None

    # Metodo che recupera le liste dai file e li mette su una lista
    def recuperaListOfLists(self):
        listProdottiInVendita = File().deserializza(PathDatabase().inVenditaTxt)
        listProdottiVenduti = File().deserializza(PathDatabase().vendutiTxt)
        listProdottiScaduti = File().deserializza(PathDatabase().scadutiTxt)
        listProdottiEliminati = File().deserializza(PathDatabase().eliminatiTxt)
        listTotale = list()
        listTotale.append(listProdottiInVendita)
        listTotale.append(listProdottiVenduti)
        listTotale.append(listProdottiScaduti)
        listTotale.append(listProdottiEliminati)
        return listTotale

    # Metodo che recupera gli oggetti associati ad un account
    def recuperaListaProdottiInAssociatiAdAccount(self, account, lista):
        listaFiltrata = list()
        for oggetto in lista:
            if oggetto.idAccount:
                if account.idAccount == int(oggetto.idAccount):
                    listaFiltrata.append(oggetto)
        return listaFiltrata
