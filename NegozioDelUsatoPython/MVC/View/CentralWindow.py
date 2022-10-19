import os
import pathlib
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Attività.ClienteProprietario import ClienteProprietario
from MVC.Model.SistemService.Logging import Logging
from MVC.View.AmministratoreView import AmministratoreView
from MVC.View.ClienteProprietarioView import ClienteProprietarioView
from MVC.View.LoginView import LoginView
from MVC.View.UserView import UserView


class CentralWindow():

    def __init__(self):
        pass

    def apriCentralWindowView(self, mainPath):
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "CentralWindow.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.apriUserView(pathlib.Path().resolve().__str__())

    # Metodo per aprire la finestra dell'cliente proprietario
    def apriClienteProprietarioView(self, mainPath):
        self.removeItem(self.finestra.verticalLayout)
        cliente = ClienteProprietarioView(mainPath)
        self.finestra.verticalLayout.addWidget(cliente.finestra)
        cliente.finestra.quitBtn.clicked.connect(lambda: self.apriUserView(mainPath))

    # Metodo per aprire la finestra dell'user
    def apriUserView(self, mainPath):
        self.removeItem(self.finestra.verticalLayout)
        user = UserView(mainPath)
        self.finestra.verticalLayout.addWidget(user.finestra)
        user.finestra.loginBtn.clicked.connect(lambda: self.apriLoginView(mainPath))

    # Metodo per aprire la finestra dell'admin
    def apriAmministratoreView(self, mainPath):
        self.removeItem(self.finestra.verticalLayout)
        amministratore = AmministratoreView(mainPath)
        self.finestra.verticalLayout.addWidget(amministratore.finestra)
        amministratore.finestra.quitBtn.clicked.connect(lambda: self.apriUserView(mainPath))

    # Metodo che apre la finestra del login
    def apriLoginView(self, mainPath):
        self.removeItem(self.finestra.verticalLayout)
        login = LoginView(mainPath)
        self.finestra.verticalLayout.addWidget(login.finestra)
        login.finestra.indietroBtn.clicked.connect(lambda: self.apriUserView(mainPath))
        login.finestra.confermaBtn.clicked.connect(lambda: self.loginViewConfermaView(mainPath, login))



    # Metodo che tenta di rimuovere la finestra precedentemente aggiunta al layout
    def removeItem(self, layout):
        if layout.itemAt(0) == None: return
        try:
            self.finestra.verticalLayout.removeItem(self.finestra.verticalLayout.itemAt(0))
        except:
            pass

    def loginViewConfermaView(self, mainPath, login):
        login.confermaBtn(login.finestra)
        if isinstance(Logging.accountLoggato, ClienteProprietario):
            self.apriClienteProprietarioView(mainPath)
        elif Logging.accountLoggato == "admin":
            self.apriAmministratoreView(mainPath)
        elif Logging.accountLoggato == None:
            self.apriLoginView(mainPath)

