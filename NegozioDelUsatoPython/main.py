import sys

from PySide2 import *
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QSize, Qt
from Database.PathDatabase import PathDatabase
from MVC.View.AmministratoreView import AmministratoreView

# esegui app
if __name__ == "__main__":
    PathDatabase().setup()
    app = QApplication(sys.argv)
    window = AmministratoreView()
    sys.exit(app.exec_())
    #end






