import os
import pathlib
import random
import shutil
from datetime import datetime
from unittest import TestCase
from dateutil.relativedelta import relativedelta
from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Attività.ClienteProprietario import ClienteProprietario
from MVC.Model.Attività.User import User
from MVC.Model.Servizio.Prodotto import Prodotto


class ClienteProprietario_test(TestCase):

    # Metodo che crea una copia del database prima di eseguire i test
    def setUp(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", '')
        PathDatabase().setup(mainPath)
        from_path = os.path.join(mainPath, "BackupFiles")  # path per cartella di backup
        to_path = os.path.join(mainPath, "Database")
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)
        account = self.setUp_2()
        self.setUp_3(account)
        self.setUp_4()

    # Inserimento degli account di prova
    def setUp_2(self):
        for iter in range(3):
            Amministratore().inserisciAccount("Regina", "Elisabetta", "21/04/1926", "regiElisabetta26@mail.com".__add__(iter.__str__()),
                                              "password", "0000000001", "62100", "Elisabetta", "Crathie", None, None,
                                              None)
        account = Amministratore().inserisciAccount("User", "User", "21/04/1926", "user@mail.com", "userPassword",
                                          "0000000001", "62100", "User", "Macerata", None, None, None)
        return account

    # Inserimento di prodotti nel database e associazione dei prodotti al cliente di prova
    def setUp_3(self, account):
        # def inserisciProdotto(self, idCategoria, dataEsposizione, idAccount, nomeProdotto, prezzoOriginale, idScaffale):
        min = 1
        max = 180
        dateToday = datetime.today()
        # inserimento oggett iassociati all'account User
        for iter in range(10):
            Amministratore().inserisciProdotto(iter, dateToday - relativedelta(days=random.randint(min, max)),
                                               account.idAccount, dateToday.__str__(), iter + 0.25, iter)
        # vendita di oggetti
        listaInVendita = Prodotto().recuperaListaProdottiInVendita()
        listTemp = list()
        for x in range(3):
            listTemp.append(listaInVendita.pop(x))
        Amministratore().vendiProdotti(listTemp)

    def setUp_4(self):
        email = "user@mail.com"
        password = "userPassword"
        User().login(email, password)


    # Metodo che crea ripristina il database dopo il test
    def tearDown(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", '')
        PathDatabase().setup(mainPath)
        from_path = os.path.join(mainPath, "BackupFiles")  # path per cartella di backup
        to_path = os.path.join(mainPath, "Database")
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)


    # passed
    def test_controllaStatoProdotti(self):
        account = Account().trovaOggettoTramiteEmail("user@mail.com")
        inVendita, venduti, scaduti = ClienteProprietario().controllaStatoProdotti()
        self.assertEqual(len(venduti), 3)
        self.assertEqual(len(scaduti), 0)
        self.assertEqual(len(inVendita), 7)



    def test_visualizzaDatiPersonali(self):
        email = "user@mail.com"
        password = "userPassword"
        User().login(email, password)
        account = ClienteProprietario().visualizzaDatiPersonali()
        self.assertEqual(account.email, email)
        self.assertEqual(account.password, password)

    def test_recuperaProdottiClienteProprietario(self):
        email = "user@mail.com"
        account = Account().trovaOggettoTramiteEmail(email)
        listOggetti = None
        listOggetti = ClienteProprietario().recuperaProdottiClienteProprietario(account.idAccount, PathDatabase.inVenditaTxt)
        self.assertEqual(len(listOggetti), 7)