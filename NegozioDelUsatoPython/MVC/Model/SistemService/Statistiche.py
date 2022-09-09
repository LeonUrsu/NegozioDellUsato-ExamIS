import datetime
from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
from MVC.Model.SistemService.File import File


class Statistiche:


    # Costruttore della classe
    def __init__(self):
        data = None
        guadagnoTotale = 0
        guadagnoInData = 0
        numeroClientiProprietari = None
        prodottiVendutiInData = 0
        prodottiVendutiTotali = 0
        tendenzaCategorie = None #prime tre categorie di tendenza


    # Metodo per la defizizione di un oggetto Statistiche
    def definizioneStatistiche(self):
        listProdotti = self.getListProdottiVenduti()
        listProdottiInData = self.getProdottiVendutiInData(listProdotti)
        self.data = datetime.datetime.today()
        self.numeroClientiProprietari = self.getNumeroClienti()
        self.prodottiVendutiTotali = len(listProdotti)
        self.prodottiVendutiInData = len(listProdottiInData)
        self.tendenzaCategorie = self.tendenzaCategorie(listProdotti)
        self.guadagnoTotale = self.calcolaGuadagno(listProdotti)
        self.guadagnoInData = self.calcolaGuadagno(listProdottiInData)
        self.salvataggioStatitiche()


    # Metodo che appende la satistica creata e salva tutte le statistiche nel database
    def salvataggioStatitiche(self):
        fileName = PathDatabase().statisticheTxt
        file = File()
        listStatistiche = file.deserializza(fileName)
        listStatistiche.append(self)
        file.serializza(fileName, listStatistiche)


    # Metodo per vedere quanti clienti proprietari sono registrati
    def getNumeroClienti(self):
        fileName = PathDatabase().accountTxt
        file = File()
        listClienti = file.deserializza(fileName)
        numeroClienti = len(listClienti)
        return numeroClienti


    # Metodo che prende la lista dei prodotti venduti
    def getListProdottiVenduti(self):
        fileName = PathDatabase().vendutiTxt
        file = File()
        listVenduti = file.deserializza(fileName)
        return listVenduti


    # Metodo che calcola l'ammontare complessivo dei prodotti passati tramite listProdotti
    # listProdotti = lista dei prodotti
    def calcolaGuadagno(self, listProdotti):
        totale = 0
        for prodotto in listProdotti:
            totale += prodotto.prezzoCorrente
        return totale


    # Metodo che prende la lista dei prodotti venduti nelle 24 ore anticedenti
    def getProdottiVendutiInData(self, listProdotti):
        list = []
        dataFiltro = datetime.datetime.today() - relativedelta(days=1)
        for prodotto in listProdotti:
            if prodotto.data >= dataFiltro:
                list.append(prodotto)
        return list


    # Metodo che prende le categorie con tendenza maggiore e le restituisce come un dizionario
    # listProdotti = lista di prodotti da cui calcolare la repitizione delle loro categorie(tendenza)
    def tendenzaCategorie(self, listProdotti):
        dict = {}
        numeroDiChiavi = 3
        for prodotto in listProdotti:
            try:
                prova = dict[prodotto.nome]     # possibile generatore di KeyError
                dict[prodotto.nome] += 1
            except KeyError:
                dict[prodotto.nome] = 1
        return self.topKeysInDict(dict, numeroDiChiavi)


    # Metodo che prende il numeroDiChiavi con valore piu alto
    # return dizionario con le categorie di tendenenza
    def topKeysInDict(self, dict, numeroDiChiavi):
        my_keys = sorted(dict, key=dict.get, reverse=True)[:numeroDiChiavi]
        return my_keys


    # Metodo che viene richiamato dall'Amministratore per la visualizzazione delle statistiche.
    # Esegue una lettura nel database di tutte le statistiche presenti e le restituisce come lista,
    # la lista verra' trasmessa alla WIEW per la visualizzazione grafica
    def visualizzaStatistiche(self):
        fileName = PathDatabase().statisticheTxt
        file = File()
        listStatistiche = file.deserializza(fileName)
        return listStatistiche