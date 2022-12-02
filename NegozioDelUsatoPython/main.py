import pathlib
import sys
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtWidgets import QApplication
from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.SistemService.Backup import Backup
from MVC.View.CentralWindow import CentralWindow

if __name__ == '__main__':

    #Path setup
    mainPath = pathlib.Path().resolve().__str__()
    PathDatabase().setup(mainPath)

    # Window setup
    app = QApplication(sys.argv)
    centralWindow = CentralWindow()
    centralWindow.apriCentralWindowView(pathlib.Path().resolve().__str__())
    centralWindow.finestra.show()

    # exit app setup
    try:
        sys.exit(app.exec())
    except:
        print("exiting")

    # Timer for backup setup # TODO meglio al posto del timer per avere meno risorse utilizzate fare il backup alla
    #  chiusura dell'app in questo punto del codice
    Backup().effettuaBackup()


