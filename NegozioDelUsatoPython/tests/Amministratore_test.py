import datetime
import pathlib
import random
from unittest import TestCase, main

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.File import File


class Amministratore_test(TestCase):

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
        #setup---------------------------------------------
        path = pathlib.Path().resolve().__str__().replace("tests", '')
        PathDatabase().setup(path)
        min = 1
        max = 10000
        i = random.randint(min, max)
        prodotto = Amministratore().inserisciProdotto(i, datetime.datetime.today(), i, "nome", i + 0.1, i)
        idProdotto = prodotto.idProdotto
        # test----------------------------------------------
        listProdotti = Prodotto().recuperaListaOggettiProdotti(PathDatabase.inVenditaTxt)
        prodottotest = None
        for prodotto in listProdotti:
            if prodotto.idProdotto == idProdotto:
                prodottotest = prodotto
        self.assertEqual(idProdotto, prodottotest.idProdotto)


    def test_eliminaDatabase(self):
        pass



if __name__ == "__main__":
    main()
