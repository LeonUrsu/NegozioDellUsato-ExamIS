import json

from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Servizio.Prodotto import Prodotto
from datetime import date

from MVC.Model.SistemService.File import File

for x in range(5):
    Amministratore().inserisciProdotto(x, date.today(), x, "ciao"+x.__str__(), x, 0)
print("@@@")
prodotto = Prodotto()
prodottoList = (Amministratore().visualizzaProdotti())

for prodotti in prodottoList:
    print(prodotti.nomeProdotto)
    print(prodotti.idProdotto)
    print(prodotti.idAccount)


