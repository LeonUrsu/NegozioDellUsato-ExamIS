import datetime
from fileinput import filename
from unittest import TestCase, main
import Database
from MVC.Model.SistemService.File import File


class File_test(TestCase):

    def test_leggi(self):
        #SETUP-----------
        filename = "Database\parametri.txt"
        letto = File().leggi(filename)
        print(letto)