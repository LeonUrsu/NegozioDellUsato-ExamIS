import pathlib
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from Database.PathDatabase import PathDatabase
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.SistemService.Statistiche import Statistiche
from MVC.View.CentralWindow import CentralWindow


if __name__ == '__main__':

    # TODO correggere i test eliminati il 14 nov
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
        print("exiting")

    # Generatore statistiche
    try:
        Statistiche().aggiungiStatistiche()
    except:
        print("errore generazione statistiche")

    # backup del database
    # chiusura dell'app in questo punto del codice
    try:
        Backup().effettuaBackup()
    except:
        print("errore generazione backup")
