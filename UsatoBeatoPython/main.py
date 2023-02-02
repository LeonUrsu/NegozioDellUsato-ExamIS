import os
import pathlib
import sys

from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
from Database.PathDatabase import PathDatabase
from MVC.model.Servizio.Prodotto import Prodotto
from MVC.model.SistemService.Backup import Backup
from MVC.model.SistemService.Statistiche import Statistiche
from MVC.view.CentralWindow import CentralWindow

if __name__ == '__main__':

    # Path setup
    mainPath = sys.argv[0]
    mainDirPath = os.path.dirname(mainPath)
    pathDatabase = PathDatabase()
    print(f"...........{pathDatabase.mainDirPath}")
    try:
    # Window setup
        app = QApplication(sys.argv)
        app.setApplicationDisplayName("UsatoBeato")
        centralWindow = CentralWindow()
        centralWindow.apriCentralWindowView(pathDatabase.mainDirPath)
        centralWindow.finestra.show()
    except: pass
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
        Backup().effettuaBackup(pathDatabase)
        print(">>>>backup effettuato")
    except:
        print(">>>>errore generazione backup")
