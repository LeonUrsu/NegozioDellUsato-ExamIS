import pathlib
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from Database.PathDatabase import PathDatabase

if __name__ == '__main__':
    # Path setup
    mainPath = pathlib.Path().resolve().__str__()
    PathDatabase().setup(mainPath)

    # Window setup
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    userView = UserView()
    widget.addWidget(userView)
    widget.setFixedWidth(920)
    widget.setFixedHeight(570)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")

    # Timer for backup setup
    #TODO


