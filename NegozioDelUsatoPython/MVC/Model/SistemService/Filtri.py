from datetime import datetime

from MVC.Model.Attività.Account import Account
from MVC.Model.SistemService.File import File


class Filtri:


    # Costruttore della classe
    def __init__(self):
        self.filtrati = None


    # Metodo di filtraggio dei prodotti in base all prezzo
    # prezzoMin = prezzo minimo di filtraggio
    # prezzoMax = prezzo massimo di filtraggio
    def filtraPrezzo(self, prezzoMin, prezzoMax, fileName):
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if prezzoMin <= int(prodotto.prezzoCorrente) and int(prodotto.prezzoCorrente) <= prezzoMax:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList


    # Metodo di filtraggio dei prodotti in base alla data di esposione
    # dataInizio = data di inizio filtraggio
    # dataFine = data di fine filtraggio
    def filtraDataEsposizione(self, dataInizio, dataFine, fileName):
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = list()
        for prodotto in prodottiList:
            if dataInizio <= prodotto.dataEsposizione and prodotto.dataEsposizione <= dataFine:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList


    # Metodo di filtraggio dei prodotti in base alla categoria
    # idCategoria = codice della categoria su cui fare la selezione
    # file =
    def filtraCategoria(self, idCategoria, fileName):
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if idCategoria == prodotto.idCategoria:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList

    def filtraClienti(self, nome, cognome):
        listClientiConNome = list()
        listClienti = Account().recuperaListaOggetti()
        if nome != "" or cognome != "":
            for cliente in listClienti:
                if cliente.nome == nome or cliente.cognome == cognome:
                    listClienti.append(cliente)
                    return listClienti
        return None