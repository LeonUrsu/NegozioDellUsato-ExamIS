import pathlib
import sys

from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
from Database.PathDatabase import PathDatabase
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.SistemService.Statistiche import Statistiche
from MVC.View.CentralWindow import CentralWindow

if __name__ == '__main__':

    # Path setup
    mainPath = pathlib.Path().resolve().__str__()
    PathDatabase().setup(mainPath)

    # Window setup
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("UsatoBeato")
    centralWindow = CentralWindow()
    centralWindow.apriCentralWindowView(pathlib.Path().resolve().__str__())
    centralWindow.finestra.show()

    # exit app setup
    try:
        sys.exit(app.exec())
    except:
        print(">>>>exiting")

    # Sconta i prodotti alla chiusura
    try:
        Prodotto().scontaProdotti()
        print(">>>>prodotti scontati")
    except:
        print(">>>>errore sconto prodotti")

    # Generatore statistiche
    try:
        Statistiche().aggiungiStatistiche()
        print(">>>>stats generate")
    except:
        print(">>>>errore generazione statistiche")

    # backup del database
    # chiusura dell'app in questo punto del codice
    try:
        Backup().effettuaBackup()
        print(">>>>backup effettuato")
    except:
        print(">>>>errore generazione backup")
