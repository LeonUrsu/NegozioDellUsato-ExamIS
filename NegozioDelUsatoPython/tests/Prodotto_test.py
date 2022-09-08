import json
import os
import pathlib
import shutil
from datetime import datetime
from unittest import TestCase

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto


class Prodotto_test(TestCase):
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

    def test_aggiornaProdotto(self):
        # SETUP--------------
        PathDatabase().setup(pathlib.Path().resolve().__str__().replace("tests", ""))
        primoId = 1
        Amministratore().inserisciProdotto(primoId, datetime.today(), primoId, "nome", primoId, primoId)
        secondoId = 2
        beforeProdotto = Prodotto().trovaOggettoTramiteId(primoId)
        print(beforeProdotto.__dict__)
        Amministratore().aggiornaProdotto(secondoId, datetime.today(), "ciao", secondoId, secondoId, primoId)
        afterProdotto = Prodotto().trovaOggettoTramiteId(primoId)
        print(afterProdotto.__dict__)

