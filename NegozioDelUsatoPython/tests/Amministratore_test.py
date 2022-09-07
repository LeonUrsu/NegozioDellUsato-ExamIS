import datetime
import os
import pathlib
import random
from builtins import print
from shutil import copytree
from unittest import TestCase, main



from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.File import File


class Amministratore_test(TestCase):

    def setUp(self):
        print("-------setup")
        """try:
            path = pathlib.Path().resolve().__str__().replace("tests", '')
            PathDatabase().setup(path)
        except:
            pass
        from_path = pathlib.Path().resolve().__str__().replace("tests", "Database")
        to_path = pathlib.Path().resolve().__str__().replace("tests", "Database_temp")
        os.mkdir(to_path)
        copytree(from_path, to_path)"""

    def tearDown(self):
        print("----------teardown")
        """to_path = pathlib.Path().resolve().__str__().replace("tests", "Database")
        os.remove(to_path)
        os.mkdir(to_path)
        from_path = pathlib.Path().resolve().__str__().replace("tests", 'Database_temp')
        copytree(from_path, to_path)
        os.remove(from_path)"""

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
        print(Amministratore().vendiProdotti(listProdotti))
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
