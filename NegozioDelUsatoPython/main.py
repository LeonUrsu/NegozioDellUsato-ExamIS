import pathlib
import sys
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtWidgets import QApplication
from Database.PathDatabase import PathDatabase
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

    # Timer for backup setup
    #TODO
#setStyleSheet
"#homeBtn{\n"
"	color:#78799c;\n"
"	background-color:#1a1f39;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	border-top-left-radius:25px;\n""}\n"


