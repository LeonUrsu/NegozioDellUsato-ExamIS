import pathlib
from datetime import datetime

from MVC.Model.Attività.Amministratore import Amministratore
from Database import PathDatabase

mainPath = pathlib.Path().resolve().__str__()
PathDatabase.PathDatabase().setup(mainPath)

for iter in range(3):
        prodotto = Amministratore().inserisciProdotto(0,datetime.today(),1,"nome",15,0)


