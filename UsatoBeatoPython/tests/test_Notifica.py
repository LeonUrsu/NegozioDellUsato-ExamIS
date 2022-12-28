import os
import pathlib
import shutil
from datetime import datetime
from unittest import TestCase

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Notifica import Notifica


class Notifica_test(TestCase):

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
        Amministratore().inserisciAccount("mario", "rossi", "16/05/1999", "test@gmail.com",
                                          "password", "000000", None, None,
                                          None, None, None, None)
        for x in range(3):
            Categoria().aggiungiCategoria(x)

        Amministratore().inserisciProdotto(1, datetime.today(), 1, "pera", 17, None)

    def test_gestioneEmailDiRegistrazione(self):
        Notifica().gestioneEmailDIRegistrazione("test@gmail.com", "password")

    def test_gestioneEmailDiVendita(self):
        carrello = list()
        carrello.append(Prodotto().trovaOggettoTramiteId(1))
        Amministratore().vendiProdotti(carrello)
        Notifica().gestioneEmailDiVendita(carrello)

    def test_gestioneEmailDiEliminazione(self):
        Notifica().gestioneEmailDiEliminazione(1)
