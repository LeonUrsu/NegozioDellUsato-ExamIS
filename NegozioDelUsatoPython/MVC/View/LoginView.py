import os

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget

from MVC.Controller.Controller import Controller


class LoginView(QWidget):
    def __init__(self, mainPath):
        super().__init__()
        loader = QUiLoader()
        path = os.path.join(mainPath, "MVC", "View", "LoginView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()
        self.finestra.confermaBtn.clicked.connect(lambda: self.confermaBtn(self.finestra))


    def confermaBtn(self, finestra):
        email = finestra.emailEd.text()
        password = finestra.passwordEd.text()
        risultato = Controller().userLoginController(email, password)
        print(risultato)