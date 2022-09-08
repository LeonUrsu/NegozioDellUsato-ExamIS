import datetime
import os
import pathlib
import random
import shutil
import time
from builtins import print
from unittest import TestCase, main

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.File import File


class Amministratore_test(TestCase):

    #Metodo che crea una copia del database prima di eseguire i test
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

    # Metodo che crea ripristina il database dopo il test
    def tearDown(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", '')
        from_path = os.path.join(mainPath, "Database_temp")
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


    # test che inserisce nel database dei prodotti casuali per poi eseguire la loro vendita per verificare
    # se sono stati effettivamente venduti
    def test_vendiProdotti(self):
        # SETUP-----------------
        path = pathlib.Path().resolve().__str__().replace("tests", '')
        PathDatabase().setup(path)
        listProdotti = list()
        contatore = 5
        for i in range(0, contatore):
            prodotto = Amministratore().inserisciProdotto(i, datetime.datetime.today(), i, "nome", i + 0.1, i)
            listProdotti.append(prodotto)
        # TEST-----------------
        Amministratore().vendiProdotti(listProdotti)
        listProdottiVenduti = File().deserializza(PathDatabase.vendutiTxt)
        segnalino = 0
        for venduto in listProdottiVenduti:
            for prodotto in listProdotti:
                if prodotto.idProdotto == venduto.idProdotto:
                    segnalino += 1
        self.assertEqual(segnalino, contatore)

    # test che inserisce un prodotto nel database con valori casuali e verifica se è stato effettivamente inserito
    def test_inserisciProdotto(self):
        # setup---------------------------------------------
        path = pathlib.Path().resolve().__str__().replace("tests", '')
        PathDatabase().setup(path)
        min = 1
        max = 10000
        i = random.randint(min, max)
        prodotto = Amministratore().inserisciProdotto(i, datetime.datetime.today(), i, "nome", i + 0.1, i)
        idProdotto = prodotto.idProdotto
        # test----------------------------------------------
        listProdotti = Prodotto().recuperaListaOggetti(PathDatabase.inVenditaTxt)
        prodottotest = None
        for prodotto in listProdotti:
            if prodotto.idProdotto == idProdotto:
                prodottotest = prodotto
        self.assertEqual(idProdotto, prodottotest.idProdotto)



if __name__ == "__main__":
    main()
