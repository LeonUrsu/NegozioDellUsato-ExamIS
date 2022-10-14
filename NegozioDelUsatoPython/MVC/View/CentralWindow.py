import os
import sys

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

from MVC.View.AmministratoreView import AmministratoreView
from MVC.View.ClienteProprietarioView import ClienteProprietarioView
from MVC.View.UserView import UserView


class CentralWindow():

    def __init__(self, mainPath):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "CentralWindow.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.apriUserView(mainPath)

    # Metodo per aprire la finestra
    def apriClienteProprietarioView(self, mainPath):
        cliente = ClienteProprietarioView(mainPath)
        self.finestra.verticalLayout.addWidget(cliente.finestra)

    # Metodo per aprire la finestra
    def apriUserView(self, mainPath):
        user = UserView(mainPath)
        self.finestra.verticalLayout.addWidget(user.finestra)

    # Metodo per aprire la finestra
    def apriAmministratoreView(self, mainPath):
        amministratore = AmministratoreView(mainPath)
        self.finestra.verticalLayout.addWidget(amministratore.finestra)
