import datetime
from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.File import File


class Statistiche:

    # Costruttore della classe
    def __init__(self):
        pass

    # Metodo per la defizizione di un oggetto Statistiche
    def aggiungiStatistiche(self):
        self.rimuoviStatsConData()
        listProdotti = self.getListProdottiVenduti()
        listProdottiInData = self.getProdottiVendutiInData()
        self.data = datetime.datetime.today()
        self.numeroClientiProprietari = self.getNumeroClienti()
        self.prodottiVendutiTotali = len(listProdotti)
        self.prodottiVendutiInData = len(listProdottiInData)
        self.tendenzaCategorie = self.tendenzaCategorie()
        self.guadagnoTotale = self.calcolaGuadagno(self.getListProdottiVenduti())
        self.guadagnoInData = self.calcolaGuadagno(self.getProdottiVendutiInData())
        self.salvataggioStatitiche()

    # Metodo che appende la satistica creata e salva tutte le statistiche nel database
    def salvataggioStatitiche(self):
        fileName = PathDatabase().statisticheTxt
        file = File()
        listStatistiche = file.deserializza(fileName)
        listStatistiche.append(self)
        file.serializza(fileName, listStatistiche)

    # Metodo che cerca tra le statistiche dsponibili e trova la più recente, ritorna None se non ci sono statistiche
    def trovaUltimeStatistiche(self):
        fileName = PathDatabase().statisticheTxt
        file = File()
        listStatistiche = file.deserializza(fileName)
        if len(listStatistiche) == 0: return None
        statistica = None
        ultimaData = listStatistiche[0].data
        for stats in listStatistiche:
            if stats.data >= ultimaData:
                statistica = stats
        return statistica

    # Metodo per vedere quanti clienti proprietari sono registrati
    def getNumeroClienti(self):
        listClienti = Account().recuperaListaOggetti()
        numeroClienti = len(listClienti)
        return numeroClienti

    # Metodo che prende la lista dei prodotti venduti
    def getListProdottiVenduti(self):
        listVenduti = Prodotto().recuperaListaProdottiVenduti()
        return listVenduti

    # Metodo che calcola l'ammontare complessivo dei prodotti passati tramite listProdotti
    # listProdotti = lista dei prodotti
    def calcolaGuadagno(self, listProdotti):
        totale = 0
        for prodotto in listProdotti:
            totale += prodotto.prezzoCorrente
        return totale

    # Metodo che prende la lista dei prodotti venduti nelle 24 ore anticedenti
    def getProdottiVendutiInData(self):
        listVenduti = self.getListProdottiVenduti()
        dataFiltro = datetime.datetime.today() - relativedelta(days=1)
        lista = list()
        for prodotto in listVenduti:
            if prodotto.dataEsposizione >= dataFiltro:
                lista.append(prodotto)
        return lista

    # Metodo che prende le categorie con tendenza maggiore e le restituisce come un dizionario
    # listProdotti = lista di prodotti da cui calcolare la repitizione delle loro categorie(tendenza)
    def tendenzaCategorie(self):
        listCategorie = Categoria().recuperaListaOggetti()
        listCategorie.sort(key=lambda x: x.oggettiTotali, reverse=True)
        del listCategorie[3:len(listCategorie)]
        return listCategorie

    # Metodo che passata una lista di categorie trova la lista con piu oggetti
    def maxOggettiCategoria(self, lista):
        massimo = 0
        for ogg in lista:
            if ogg.oggettiTotali > massimo:
                massimo = ogg.oggettiTotali
        return massimo

    # Metodo che prende il numeroDiChiavi con valore piu alto
    # return dizionario con le categorie di tendenenza
    def topKeysInDict(self, dict):
        lista = list()
        for obj in sorted(dict, key=dict.get, reverse=False):
            lista.append(obj)
        return lista

    # Metodo che viene richiamato dall'Amministratore per la visualizzazione delle statistiche.
    # Esegue una lettura nel database di tutte le statistiche presenti e le restituisce come lista,
    # la lista verra' trasmessa alla WIEW per la visualizzazione grafica
    def visualizzaStatistiche(self):
        fileName = PathDatabase().statisticheTxt
        file = File()
        listStatistiche = file.deserializza(fileName)
        return listStatistiche

    # Metodo che rimuove le statistiche con la stessa data nello stesso giorno per non creare inconsistenza
    def rimuoviStatsConData(self):
        todayDate = datetime.datetime.today().date()
        lista = self.visualizzaStatistiche()
        for stats in lista:
            if stats.date.date() == todayDate:
                lista.pop(lista.index(stats))
        File().serializza(PathDatabase.statisticheTxt, lista)
