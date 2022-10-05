import sys

<<<<<<< HEAD
from PySide2 import *
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QSize, Qt
=======
from PySide2.QtWidgets import *
>>>>>>> a1c425fe1dcedcd08c6db57fde24aa82f06a01ec
from Database.PathDatabase import PathDatabase
from MVC.View.AmministratoreView import AmministratoreView

# esegui app
if __name__ == "__main__":
    PathDatabase().setup()
    app = QApplication(sys.argv)
    window = AmministratoreView()
    sys.exit(app.exec_())
    #end






