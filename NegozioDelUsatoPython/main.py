import sys

from PySide2.QtWidgets import *
from Database.PathDatabase import PathDatabase
from MVC.View.AmministratoreView import AmministratoreView

# esegui app
if __name__ == "__main__":
    PathDatabase().setup()
    app = QApplication(sys.argv)
    window = AmministratoreView()
    window.showMaximized()
    sys.exit(app.exec_())
    #end






