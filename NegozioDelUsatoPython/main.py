import os
import pathlib
from builtins import print
from datetime import datetime

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto


def test_aggiornaProdotto():
    # SETUP--------------

    primoId = 1
    Amministratore().inserisciProdotto(primoId, datetime.today(), primoId, "cognome", primoId, primoId)
    secondoId = 2
    Amministratore().aggiornaProdotto(secondoId, datetime.today(), secondoId, "cognome", secondoId, secondoId,
                                      secondoId)
    primoProdotto = Prodotto().trovaOggettoTramiteId(primoId)
    secondoProdotto = Prodotto().trovaOggettoTramiteId(secondoId)
    print(primoProdotto.nome)
    print(secondoProdotto.nome)




#PathDatabase().setup()
print(PathDatabase.vendutiTxt)
#test_aggiornaProdotto()
