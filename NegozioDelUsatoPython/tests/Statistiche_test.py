import os
import pathlib
import random
import shutil
from datetime import datetime
from unittest import TestCase

from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Statistiche import Statistiche


class Statistiche_test(TestCase):
    # Metodo che crea una copia del database prima di eseguire i test
    def setUp(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", '')
        path = os.path.join(mainPath, "Database_temp")  # path per cartella di backup
        try:
            shutil.rmtree(path)
        except:
            pass
        PathDatabase().setup(mainPath)
        from_path = os.path.join(mainPath, "Database")
        to_path = os.path.join(mainPath, "Database_temp")
        shutil.copytree(from_path, to_path)
        self.setUp_1()
        self.setUp_2()

    # Metodo che crea ripristina il database dopo il test
    def tearDown(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", '')
        from_path = os.path.join(mainPath, "Database_temp")
        #from_path = os.path.join(mainPath, "BackupFiles")
        to_path = os.path.join(mainPath, "Database")
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)
        try:
            shutil.rmtree(from_path)
        except:
            pass

    # Metodo che inserisce dei prodotti nel database e ne vende una parte
    def setUp_1(self):
        # def inserisciProdotto(self, idCategoria, dataEsposizione, idAccount, nomeProdotto, prezzoOriginale, idScaffale):
        min = 1
        max = 180
        dateToday = datetime.today()
        # inserimento oggett iassociati all'account User
        for iter in range(10):
            Amministratore().inserisciProdotto(iter, dateToday - relativedelta(hours=7),
                                               iter, dateToday.__str__(), iter, iter)
        # vendita di oggetti
        listaInVendita = Prodotto().recuperaListaProdottiInVendita()
        listTemp = list()
        for x in range(3):
            listTemp.append(listaInVendita.pop(x))
        lista = Amministratore().vendiProdotti(listTemp)

    def setUp_2(self):
        for iter in range(3):
            Amministratore().inserisciAccount("Regina", "Elisabetta", "21/04/1926", "regiElisabetta26@mail.com".__add__(iter.__str__()),
                                              "password", "0000000001", "62100", "Elisabetta", "Crathie", None, None,
                                              None)



    def setUp_3(self):
        listNomi = ("Informatica", "Motori", "Sport")
        dateToday = datetime.today()
        for name in listNomi:
            categoria = Categoria()
            categoria.aggiungiCategoria(name)
            for iter in range(3):
                Amministratore().inserisciProdotto(categoria.idCategoria, dateToday - relativedelta(hours=7),
                                                   iter, dateToday.__str__(), iter, iter)
        categoria = Categoria()
        categoria.aggiungiCategoria("Casa")
        Amministratore().inserisciProdotto(categoria.idCategoria, dateToday, 1, dateToday.__str__(), 1, 1)

    def test_calcoloGuadagno(self):
        listVenduti = Prodotto().recuperaListaProdottiVenduti()
        somma = 0
        for prodotto in listVenduti:
            somma += prodotto.prezzoCorrente
        totale = Statistiche().calcolaGuadagno(listVenduti)
        self.assertEqual(somma, totale)


    def test_getProdottiVendutiInData(self):
        listVenduti = Statistiche().getProdottiVendutiInData()
        numeroVenduti = len(listVenduti)
        self.assertEqual(3, numeroVenduti)

    def test_tendenzaCategorie(self):
        self.setUp_3()
        lista = Statistiche().tendenzaCategorie()
        print(lista)

    def test_aggiungistatistiche(self):
        Statistiche().aggiungiStatistiche()
        return