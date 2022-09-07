import os
import pathlib
from datetime import datetime
from shutil import copytree
from unittest import TestCase, main

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto


class File_test(TestCase):
    """
    def pytest_configure(config):
        try:
            path = pathlib.Path().resolve().__str__().replace("tests", '')
            PathDatabase().setup(path)
        except:
            pass
        from_path = pathlib.Path().resolve().__str__().replace("tests", "Database")
        to_path = pathlib.Path().resolve().__str__().replace("tests", "Database_temp")
        os.mkdir(to_path)
        copytree(from_path, to_path)

    def pytest_unconfigure(config):
        to_path = pathlib.Path().resolve().__str__().replace("tests", "Database")
        os.remove(to_path)
        os.mkdir(to_path)
        from_path = pathlib.Path().resolve().__str__().replace("tests", 'Database_temp')
        copytree(from_path, to_path)
        os.remove(from_patsh)
    """
    def test_aggiornaProdotto(self):
        # SETUP--------------
        PathDatabase().setup(pathlib.Path().resolve().__str__().replace("tests", ""))
        primoId = 1
        Amministratore().inserisciProdotto(primoId, datetime.today(), primoId, "cognome", primoId, primoId)
        secondoId = 2
        Amministratore().aggiornaProdotto(secondoId, datetime.today(), secondoId, "cognome", secondoId, primoId)
        primoProdotto = Prodotto().trovaOggettoTramiteId(primoId)
        secondoProdotto = Prodotto().trovaOggettoTramiteId(secondoId)
