import os
import pathlib
import random
import shutil
import time
from datetime import datetime
from unittest import TestCase, main

from dateutil.relativedelta import relativedelta

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Attività.User import User
from MVC.Model.SistemService.Logging import Logging


class User_test(TestCase):

    def setUp(self):
        mainPath = pathlib.Path().resolve().__str__().replace("tests", "")
        from_path = os.path.join(mainPath, "Database")
        to_path = os.path.join(mainPath, "tempDataBase")
        try:
            shutil.rmtree(to_path)
        except:
            pass
        shutil.copytree(from_path, to_path)
        self.setUp_2()
        self.setUp_3()
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

    def setUp_2(self):
        min = 1
        max = 180
        dateToday = datetime.today()
        for iter in range(50):
            Amministratore().inserisciProdotto(iter, dateToday - relativedelta(days=random.randint(min, max)), iter,
                                               dateToday.__str__(), iter + 0.25, iter)

    def setUp_3(self):
        for iter in range(20):
            Amministratore().inserisciAccount("Regina", "Elisabetta", "21/04/1926", "regiElisabetta26@mail.com",
                                              "password", "0000000001", "62100", "Elisabetta", "Crathie", None, None,
                                              None)
        Amministratore().inserisciAccount("User", "User", "21/04/1926", "user@mail.com", "userPassword",
                                          "0000000001", "62100", "User", "Macerata", None, None, None)

    def test_filtraProdottiConData(self):
        dataFine = datetime.today()
        dataInizio = dataFine - relativedelta(days=70)
        filtrati = User().filtraProdottiConDataEsposizione(dataInizio, dataFine)
        for prodotto in filtrati:
            if prodotto.dataEsposizione < dataInizio:
                raise Exception

    def test_filtraProdottiConPrezzo(self):
        prezzoMin = 25
        prezzoMax = 35
        filtrati = User().filtraProdottiConPrezzo(prezzoMin, prezzoMax)
        for prodotto in filtrati:
            if not prezzoMin < prodotto.prezzoCorrente or not prodotto.prezzoCorrente < prezzoMax:
                raise Exception

    def test_filtraProdottiConCategoria(self):
        cod = 15
        filtrati = User().filtraProdottiConCategoria(cod)
        for prodotto in filtrati:
            if prodotto.idCategoria != cod:
                raise Exception

    def test_login(self):
        email = "user@mail.com"
        password = "userPassword"
        User().login(email, password)
        self.assertEqual(Logging.accountLoggato.email, email)
        self.assertEqual(Logging.accountLoggato.password, password)
