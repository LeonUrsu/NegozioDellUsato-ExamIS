import os

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QLineEdit

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

    def confermaBtn(self, finestra):
        email = finestra.emailEd.text()
        password = finestra.passwordEd.text()
        risultato = Controller().userLoginController(email, password)

    #Metodo che permette di visualizzare la password inserita
    def toggleVisibility(self,login):
        if login.finestra.passwordEd.echoMode() == QLineEdit.Normal:
            login.finestra.passwordEd.setEchoMode(QLineEdit.Password)
        else:
            login.finestra.passwordEd.setEchoMode(QLineEdit.Normal)

