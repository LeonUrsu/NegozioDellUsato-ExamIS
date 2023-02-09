import unittest
from datetime import datetime
import os
import pathlib
import random
import shutil
from unittest import TestCase

from Database.PathDatabase import PathDatabase
from MVC.model.Attività.Account import Account
from MVC.model.Attività.Amministratore import Amministratore
from MVC.model.Servizio.Prodotto import Prodotto
from MVC.model.SistemService.File import File


class Amministratore_test(TestCase):

    def setUp(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", "")
        from_path = os.path.join(mainPath, "Database")
        to_path = os.path.join(mainPath, "tempDataBase")
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)
        PathDatabase().setup(mainPath)
        print("SETUP DONE---------")

    # Metodo che crea ripristina il database dopo il test
    def tearDown(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", "")
        from_path = os.path.join(mainPath, "tempDataBase")
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
        print("TEARDOWN DONE---------")

    # test che inserisce nel database dei prodotti casuali per poi eseguire la loro vendita per verificare
    # se sono stati effettivamente venduti
    def test_vendiProdotti(self):
        listProdotti = list()
        contatore = 5
        for i in range(contatore):
            prodotto = Amministratore().inserisciProdotto(datetime.today(), None, f"{i}", i, "s", "tecnologia")
            listProdotti.append(prodotto)
        Amministratore().vendiProdotti(listProdotti)
        listProdottiVenduti = File().deserializza(PathDatabase().vendutiTxt)
        segnalino = 0
        for venduto in listProdottiVenduti:
            for prodotto in listProdotti:
                if prodotto.idProdotto == venduto.idProdotto:
                    segnalino += 1
        self.assertEqual(segnalino, contatore)

    # test che inserisce un prodotto nel database con valori casuali e verifica se è stato effettivamente inserito
    def test_inserisciProdotto(self):
        # setup---------------------------------------------
        min = 1
        max = 10000
        idProdotti = list()
        i = random.randint(min, max)
        for x in range(5):
            prodotto = Amministratore().inserisciProdotto(datetime.today(), None, "nome", i, "s", "tecnologia")
            idProdotti.append(prodotto.idProdotto)
        # test----------------------------------------------
        listProdotti = Prodotto().recuperaListaProdottiInVendita()
        for prodotto in listProdotti:
            for idProdotto in idProdotti:
                if prodotto.idProdotto == idProdotto:
                    self.assertEqual(idProdotto, prodotto.idProdotto)

    def test_inserisciAccount(self):
        # setup -------------
        account1 = Amministratore().inserisciAccount("nuovo", "cognome", '24/05/2000', "nuovoMailodad@gmafil.com", "ciao",
                                                     '3812312271',
                                                     '63066', 'ciao', 'sbt', '9', 'nessuna', ' ciao1')
        # test---------------
        account2 = Account().trovaOggettoTramiteEmail(account1.email)
        self.assertEqual(account1.idAccount, account2.idAccount)

    def test_eliminaAccount(self):
        # setup-------
        email = "email@prova.it"
        Amministratore().inserisciAccount("nome", "cognome", "10/10/2000", email, "password", "12351324", "61200",
                                          "nome", "Macerata", "30", None, "Romaaa")
        accountInserito = Account().trovaOggettoTramiteEmail(email)
        Amministratore().eliminaAccount(accountInserito.idAccount)
        accountCercato = Account().trovaOggettoTramiteId(accountInserito.idAccount)
        if accountCercato is not None:
            raise FileNotFoundError
        else:
            pass

    def test_eliminaProdotto(self):
        Amministratore().inserisciProdotto(datetime.today(), None, "nomeProdotto", "43", "c3", "Elettronica")
        prodottoInserito = Prodotto().trovaOggettoTramiteId(1)
        Amministratore().eliminaProdotto(prodottoInserito.idProdotto)
        prodottoCercato = Prodotto().trovaOggettoTramiteId(prodottoInserito.idProdotto)
        if prodottoCercato is None:
            raise FileNotFoundError
        else:
            pass

    def test_aggiornaProdotto(self):
        prodotto = Amministratore().inserisciProdotto(datetime.today(), None, "nomeProdotto", "43", "c3", "Elettronica")
        nuovoNome = "nuovoNomeProdotto"
        Amministratore().aggiornaProdotto("Utensili", "12/10/2021", nuovoNome, "60", "d4", prodotto.idProdotto)
        afterProdotto = Prodotto().trovaOggettoTramiteId(prodotto.idProdotto)
        self.assertEqual(nuovoNome, afterProdotto.nomeProdotto)

    def test_aggiornaAccount(self):
        account1 = Amministratore().inserisciAccount("nome", "cognome", "10/10/2000", "vecchiaEmail@gmai.com",
                                                     "password", "12351324", "61200", "nome", "Macerata", "30", None,
                                                     "Romaaa")
        account2 = Amministratore().aggiornaAccount(None, "Polo", "12/12/1987", "nuovaEmial@usatobeato.it",
                                                    account1.idAccount, "121313245", None)
        self.assertEqual(account1.idAccount, account2.idAccount)
        self.assertNotEqual(account1.nome, account2.nome)
        self.assertNotEqual(account1.cognome, account2.cognome)
        self.assertNotEqual(account1.dataDiNascita, account2.dataDiNascita)
        self.assertNotEqual(account1.email, account2.email)
        self.assertNotEqual(account1.numeroTelefonico, account2.numeroTelefonico)


if __name__ == "__main__":
    unittest.main()
