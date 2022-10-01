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



