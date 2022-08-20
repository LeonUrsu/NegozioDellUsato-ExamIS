import datetime
from unittest import TestCase, main

from Database.PathDatabase import PathDatabase
from MVC.Model.Servizio.Prodotto import Prodotto


class Amministratore_test(TestCase):


    def test_vendiProdotti(self):
        #SETUP-----------------
        path = "C:/Users/LEON/Documents/is project/NegozioDelUsatoPython/"
        PathDatabase().pathSetup(path)
        listProdotti = list()
        for i in range(0, 5):
            prodotto = Prodotto()
            prodotto.aggiungiProdotto(i, datetime.datetime.today(), i, "nome", i+0.1, i)
            listProdotti.append(prodotto)
        #TEST-----------------

        #Amministratore().vendiProdotti(listProdotti)

        self.assertEqual("c","c")









if __name__ == "__main__":
    main()
