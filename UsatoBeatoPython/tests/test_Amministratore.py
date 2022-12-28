import unittest
from datetime import datetime
import os
import pathlib
import random
import shutil
from unittest import TestCase
from tests.Database_test.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.File import File





class Amministratore_test(TestCase):

    def setUp(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", "")
        from_path = os.path.join(mainPath, "Database")
        to_path = os.path.join(mainPath,)
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)
        print("SETUP DONE---------")

    # Metodo che crea ripristina il database dopo il test
    def tearDown(self):
        mainPath = pathlib.Path().resolve().__str__()
        from_path = os.path.join(mainPath, "EmptyDatabase")
        to_path = os.path.join(mainPath, "Database_test")
        #PathDatabase().setup(mainPath)
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)
        print("TEARDOWN DONE---------")




    # test che inserisce nel database dei prodotti casuali per poi eseguire la loro vendita per verificare
    # se sono stati effettivamente venduti
    def test_vendiProdotti(self):
        listProdotti = list()
        contatore = 5
        for i in range(0, contatore):
            prodotto = Amministratore().inserisciProdotto(i, datetime.today(), i, "nome", i + 0.1, i)
            listProdotti.append(prodotto)
        # TEST-----------------
        Amministratore().vendiProdotti(listProdotti)
        listProdottiVenduti = File().deserializza(self.pathDatabaseObj.vendutiTxt)
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
        prodotto = Amministratore().inserisciProdotto(i, datetime.today(), i, "nome", i + 0.1, i)
        idProdotto = prodotto.idProdotto
        # test----------------------------------------------
        listProdotti = Prodotto().recuperaListaProdottiInVendita()
        prodottotest = None
        for prodotto in listProdotti:
            if prodotto.idProdotto == idProdotto:
                prodottotest = prodotto
        self.assertEqual(idProdotto, prodottotest.idProdotto)

    def test_inserisciAccount(self):
        # setup -------------
        path = pathlib.Path().resolve().__str__().replace('tests', '')
        PathDatabase().setup(path)
        account1 = Amministratore().inserisciAccount("leo", "peraz", '29/05/00', "leoperaz2000@gmail.com", "ciao", '3883667271',
                                          '63066', 'ciao', 'sbt', '9', 'nessuna', ' ciao1')
        # test---------------
        account2 = Account().trovaOggettoTramiteEmail(account1.email)
        self.assertEqual(account1.idAccount, account2.idAccount)




    def test_eliminaAccount(self):
        # setup-------
        path = pathlib.Path().resolve().__str__().replace('tests', '')
        PathDatabase().setup(path)
        Amministratore().inserisciAccount("prova", "prova", "prova", "prova", "prova", "prova", "prova", "prova",
                                          "prova", "prova", "prova", "prova")
        accountInserito = Account().trovaOggettoTramiteEmail("prova")
        Amministratore().eliminaAccount(accountInserito.idAccount)
        accountCercato = Account().trovaOggettoTramiteId(accountInserito.idAccount)
        if accountCercato is not None:
            raise FileNotFoundError
        else:
            pass

    def test_eliminaProdotto(self):
        # SETUP--------------
        min = 1
        max = 10000
        i = random.randint(min, max)
        Amministratore().inserisciProdotto(i, datetime.today(), i, "nome", i + 0.1, i)
        prodottoInserito = Prodotto().trovaOggettoTramiteId(1)
        Amministratore().eliminaProdotto(prodottoInserito.idProdotto)
        prodottoCercato = Prodotto().trovaOggettoTramiteId(prodottoInserito.idProdotto)
        if prodottoCercato is None:
            raise FileNotFoundError
        else:
            pass

    def test_aggiornaProdotto(self):
        # SETUP--------------
        PathDatabase().setup(pathlib.Path().resolve().__str__().replace("tests", ""))
        primoId = 1
        Amministratore().inserisciProdotto(primoId, datetime.today(), primoId, "nome", primoId, primoId)
        secondoId = 2
        beforeProdotto = Prodotto().trovaOggettoTramiteId(primoId)
        #print(beforeProdotto.__dict__)
        Amministratore().aggiornaProdotto(secondoId, datetime.today(), "ciao", secondoId, secondoId, primoId)
        afterProdotto = Prodotto().trovaOggettoTramiteId(primoId)
        #print(afterProdotto.__dict__)

    def test_aggiornaAccount(self):
        account1 = Amministratore().inserisciAccount("leo", "peraz", '29/05/2000', "leoperaz2000@gmail.com", "ciao",
                                                     '3883667271', '63066', 'ciao', 'sbt', '9', 'nessuna', ' ciao1')
        account2 = Amministratore().aggiornaAccount("leon", "leon", "00/00/2000", "email@gmai.com", account1.idAccount,
                                                    "0000000000", None)
        self.assertEqual(account1.idAccount, account2.idAccount)
        self.assertNotEqual(account1.nome, account2.nome)
        self.assertNotEqual(account1.cognome, account2.cognome)
        self.assertNotEqual(account1.dataDiNascita, account2.dataDiNascita)
        self.assertNotEqual(account1.email, account2.email)
        self.assertNotEqual(account1.numeroTelefonico, account2.numeroTelefonico)


if __name__ == "__main__":
    unittest.main()
