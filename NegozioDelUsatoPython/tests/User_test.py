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


class User_test(TestCase):

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
        self.setUp_2()

    def setUp_2(self):
        min = 1
        max = 180
        dateToday = datetime.today()
        for iter in range(50):
            Amministratore().inserisciProdotto(iter, dateToday - relativedelta(days=random.randint(min, max)), iter, dateToday.__str__(), iter+0.25, iter)


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

    def test_filtraProdottiConData(self):
        dataFine = datetime.today()
        dataInizio = dataFine - relativedelta(days=70)
        filtrati = User().filtraProdottiConDataEsposiozione(dataInizio, dataFine)
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
            if prodotto.codiceCategoria != cod:
                raise Exception
