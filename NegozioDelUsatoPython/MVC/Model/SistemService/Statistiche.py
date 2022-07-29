import datetime

from dateutil.relativedelta import relativedelta

from MVC.Model.SistemService.File import File


class Statistiche:

    # Costruttore della classe
    def __init__(self):
        data = None
        numeroClientiProprietari = None
        prodottiVendutiTotali = 0
        prodottiVendutiNellaData = 0
        tendenzaCategorie = None #prime tre categorie di tendenza
        guadagnoTotale = 0
        guadagnoInData = 0
        nuoviClientiProprietari = 0


    # Metodo per la defizizione di un oggetto Statistiche
    def definizioneStatistiche(self):
        listProdotti = self.getListProdottiVenduti()
        listProdottiInData = self.getProdottiVendutiInData()
        self.data = datetime.datetime.today()
        self.numeroClienti = self.getNumeroClienti()
        self.prodottiVenduti = self.getNumeroProdottiVenduti(listProdotti)
        self.prodottiVendutiInData = self.getNumeroProdottiVendutiInData(listProdotti)
        self.tendenzaCategorie = tendenzaCategorie
        self.guadagnoTotale =

    # Metodo per vedere quanti clienti proprietari sono registrati
    def getNumeroClienti(self, listProdotti):
        fileName = "Database\Clienti\Clienti.txt"
        listClienti = File.deserializza(fileName)
        numeroClienti = listClienti.len()
        return numeroClienti

    # Metodo che prende la lista dei prodotti venduti
    def getListProdottiVenduti(self):
        fileName = "Database\Prodotti\Venduti.txt"
        listVenduti = File.deserializza()
        return listVenduti


    def getNumeroProdottiVenduti(self, listVenduti):
        numeroProdottiVenduti = listVenduti.len()
        return numeroProdottiVenduti



    def getProdottiVendutiInData(listProdotti)
        list = []
        dataFiltro = datetime.datetime.today() - relativedelta(days=5)
        for x in listProdotti:
            if x.data >= dataFiltro:
                list.append(x)
        return list