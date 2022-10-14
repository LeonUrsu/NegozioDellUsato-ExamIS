import pathlib
import sys

from PySide6.QtWidgets import QApplication
from Database.PathDatabase import PathDatabase
from MVC.View.CentralWindow import CentralWindow

if __name__ == '__main__':
    # Path setup
    mainPath = pathlib.Path().resolve().__str__()
    PathDatabase().setup(mainPath)

    # Window setup
    app = QApplication(sys.argv)
    centralWindow = CentralWindow(mainPath)
    centralWindow.finestra.show()

    # exit app setup
    try:
        sys.exit(app.exec())
    except:
        print("exiting")

    # Timer for backup setup
    #TODO


