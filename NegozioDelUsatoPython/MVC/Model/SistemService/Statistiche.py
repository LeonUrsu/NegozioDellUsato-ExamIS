import datetime

from dateutil.relativedelta import relativedelta

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
        self.numeroClienti = self.getNumeroClienti()
        self.prodottiVenduti = listProdotti.len()
        self.prodottiVendutiInData = listProdottiInData.len()
        self.tendenzaCategorie = self.tendenzaCategorie(listProdotti)
        self.guadagnoTotale = self.calcolaGuadagnoTotale(listProdotti)
        self.guadagnoInData = self.calcolaGuadagnoInData(listProdottiInData)


    # Metodo per vedere quanti clienti proprietari sono registrati
    def getNumeroClienti(self):
        fileName = "Database\Clienti\Clienti.txt"
        listClienti = File.deserializza(fileName)
        numeroClienti = listClienti.len()
        return numeroClienti


    # Metodo che prende la lista dei prodotti venduti
    def getListProdottiVenduti(self):
        fileName = "Database\Prodotti\Venduti.txt"
        listVenduti = File.deserializza()
        return listVenduti


    # Metodo che prende la lista dei prodotti venduti nelle 24 ore anticedenti
    def getProdottiVendutiInData(self, listProdotti):
        list = []
        dataFiltro = datetime.datetime.today() - relativedelta(days=1)
        for x in listProdotti:
            if x.data >= dataFiltro:
                list.append(x)
        return list

    # Metodo che prende le categorie con tendenza maggiore e le restituisce come un dizionario
    # listProdotti = lista di prodotti da cui calcolare la repitizione delle loro categorie(tendenza)
    def tendenzaCategorie(self, listProdotti):
        dict = {}
        numeroDiChiavi = 3
        for prodotto in listProdotti:
            try:
                dict[prodotto.nome]
                dict[prodotto.nome] += 1
            except KeyError:
                dict[prodotto.nome] = 1
        return self.topKeysInDict(dict, numeroDiChiavi)



    # Metodo che prende il numeroDiChiavi con valore piu alto
    # return dizionario con le categorie di tendenenza
    def topKeysInDict(self, dict, numeroDiChiavi):
        my_keys = sorted(dict, key=dict.get, reverse=True)[:numeroDiChiavi]
        return my_keys