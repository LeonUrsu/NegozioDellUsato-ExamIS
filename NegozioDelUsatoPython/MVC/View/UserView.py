import os
import pathlib

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class UserView():


    def __init__(self, mainPath):
        #super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "UserView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        #self.finestra.homeBtn.clicked.connect(lambda: self.homeBtnClicked(self.finestra))

        #self.finestra.iMieiProdottiBtn.clicked.connect(lambda: self.iMieiProdottiBtnClicked(self.finestra))



