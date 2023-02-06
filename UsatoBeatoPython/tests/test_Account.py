import sys
from unittest import TestCase
from Database import PathDatabase
from MVC.model.Attività.Account import Account


class Amministratore_test(TestCase):

    def test_newId(self):
        mainPath = sys.argv[0]
        print("vvvvvvvvvvvvvvvvvvvvv")
        print(mainPath)
        #Account().newId()