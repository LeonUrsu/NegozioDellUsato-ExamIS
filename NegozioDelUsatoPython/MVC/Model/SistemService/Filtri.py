import json
import sys
from datetime import datetime

from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
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
                    listClientiConNome.append(cliente)
                    return listClientiConNome
        return None

    # Metodo che cerca il prodotto in base al nome passato e alle opzion scelte nella tendina
    def elaboraCercaProdottoBtnClicked(self, name, textData, textPrezzo, textCategoria):
        listaCorrispondentiData = self.ifFiltraPerDataSelected(textData)
        listaCorrispondentiPrezzo = self.ifFiltraPerPrezzo(textPrezzo)
        listaCorrispondentiCategoria = self.ifFiltraPerCategoria(textCategoria)
        listaCorrispondenti = list()
        for prodottoData in listaCorrispondentiData:
            for prodottoPrezzo in listaCorrispondentiPrezzo:
                for prodottoCategoria in listaCorrispondentiCategoria:
                    if prodottoData.idProdotto == prodottoPrezzo.idProdotto == prodottoCategoria.idProdotto:
                        listaCorrispondenti.append(prodottoData)
        if name != "":
            temp = list()
            for prodotto in listaCorrispondenti:
                if prodotto.nomeProdotto == name:
                    temp.append(prodotto)
            listaCorrispondenti = temp
        return listaCorrispondenti

    # Metodo che filtra i prodotti in base al periodo scelto
    def ifFiltraPerDataSelected(self, textData):
        lista = Prodotto().recuperaListaProdottiInVendita()
        if textData == "Tutte le date":
            return lista
        elif textData == "ultima settimana":
            lista = self.filtraDataEsposizione(datetime.today() - relativedelta(days=7),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "ultimo mese":
            lista = self.filtraDataEsposizione(datetime.today() - relativedelta(months=1),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "ultimi tre mesi":
            lista = self.filtraDataEsposizione(datetime.today() - relativedelta(months=3),
                                                       datetime.today(), PathDatabase().inVenditaTxt)
        return lista

    # Metodo che filtra i prodotti in base al prezzo massimo scelto
    def ifFiltraPerPrezzo(self, textPrezzo):
        lista = Prodotto().recuperaListaProdottiInVendita()
        if textPrezzo == "tutti i prezzi":
            return lista
        elif textPrezzo == "0€ - 10€ ":
            #lista = Controller().filtraPrezzo(0, 10, PathDatabase().inVenditaTxt)
            lista = self.filtraPrezzo(0, 10, PathDatabase().inVenditaTxt)
        elif textPrezzo == "10€ - 20€":
            #lista = Controller().filtraPrezzo(10, 20, PathDatabase().inVenditaTxt)
            lista = self.filtraPrezzo(10, 20, PathDatabase().inVenditaTxt)
        elif textPrezzo == "20€ - 50€":
            #lista = Controller().filtraPrezzo(20, 50, PathDatabase().inVenditaTxt)
            lista = self.filtraPrezzo(20, 50, PathDatabase().inVenditaTxt)
        elif textPrezzo == ">50€":
            #lista = Controller().filtraPrezzo(50, sys.maxsize, PathDatabase().inVenditaTxt)
            lista = self.filtraPrezzo()(50, sys.maxsize, PathDatabase().inVenditaTxt)
        return lista

    # Metodo che filtra i prodotti in base alla categoria scelta nella tendina della view
    def ifFiltraPerCategoria(self, textCategoria):
        #listaProdotti = Controller().recuperaListaProdottiInVendita()
        listaProdotti = Prodotto().recuperaListaProdottiInVendita()
        if textCategoria == "Tutte le categorie" or textCategoria == "":
            return listaProdotti
        categoriaIdFiltro = None
        categorieList = Categoria().recuperaListaOggetti()
        for categoria in categorieList:
            if textCategoria == categoria.nome:
                categoriaIdFiltro = categoria.idCategoria
        listaProdottiTrovati = list()
        if categoriaIdFiltro == None: return None
        for prodotto in listaProdotti:
            #print(f"{prodotto.idCategoria}-{categoriaIdFiltro}")
            if prodotto.idCategoria == categoriaIdFiltro:
                listaProdottiTrovati.append(prodotto)
        if listaProdottiTrovati:
            return listaProdottiTrovati
        else:
            return list()