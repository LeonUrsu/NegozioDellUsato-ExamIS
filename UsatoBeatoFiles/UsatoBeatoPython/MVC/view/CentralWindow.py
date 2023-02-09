import os

from PySide6 import QtGui
from PySide6.QtCore import QFile, QPropertyAnimation
from PySide6.QtUiTools import QUiLoader

from Database.PathDatabase import PathDatabase
from MVC.controller.Controller import Controller
from MVC.model.SistemService.Logging import Logging
from MVC.view.AmministratoreView import AmministratoreView
from MVC.view.ClienteProprietarioView import ClienteProprietarioView
from MVC.view.LoginView import LoginView
from MVC.view.UserView import UserView
from MVC.view.resources import *


class CentralWindow():

    def __init__(self):
        pass

    def apriCentralWindowView(self, mainPath):
        loader = QUiLoader()
        path = os.path.join(PathDatabase().mainDirPath, "resourcesForUsatoBeato", "CentralWindow.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        self.finestra.setWindowTitle("")
        path = os.path.join(PathDatabase().mainDirPath,
                            "resourcesForUsatoBeato", "assets", "LOGO", "usatobeato-website-favicon-color.svg.png")
        icon = QtGui.QIcon(path)
        self.finestra.setWindowIcon(icon)
        file.close()
        # self.apriAmministratoreView(pathlib.Path().resolve().__str__())
        # self.apriClienteProprietarioView (pathlib.Path().resolve().__str__(), None)
        self.apriUserView(mainPath)

    # Metodo per aprire la finestra dell'cliente proprietario
    def apriClienteProprietarioView(self, mainPath, account):
        self.removeItem(self.finestra.verticalLayout)
        view = ClienteProprietarioView(mainPath)
        self.finestra.verticalLayout.addWidget(view.finestra)
        view.finestra.quitBtn.clicked.connect(lambda: self.apriUserView(mainPath))
        view.finestra.openRightMenu.clicked.connect(lambda: self.slideRightMenu(view))
        view.finestra.openLeftMenu.clicked.connect(lambda: self.slideLeftMenu(view))
        view.finestra.quitBtn.clicked.connect(lambda: self.apriUserView(mainPath))

    # Metodo per aprire la finestra dell'user
    def apriUserView(self, mainPath):
        Controller().logout()
        self.removeItem(self.finestra.verticalLayout)
        user = UserView(mainPath)
        self.finestra.verticalLayout.addWidget(user.finestra)
        user.finestra.loginBtn.clicked.connect(lambda: self.apriLoginView(mainPath))
        user.finestra.openRightMenu.clicked.connect(lambda: self.slideRightMenu(user))

    # Metodo per aprire la finestra dell'admin
    def apriAmministratoreView(self, mainPath):
        amministratore = AmministratoreView()
        self.removeAndAdd(amministratore)
        amministratore.finestra.quitBtn.clicked.connect(lambda: self.apriUserView(mainPath))
        amministratore.finestra.openRightMenu.clicked.connect(lambda: self.slideRightMenu(amministratore))
        amministratore.finestra.openLeftMenu.clicked.connect(lambda: self.slideLeftMenu(amministratore))
        amministratore.prodottiBtnClicked(mainPath, amministratore, None)
        amministratore.finestra.statisticheBtn.clicked.connect(
            lambda: amministratore.statisticheBtnClicked(mainPath, amministratore))
        amministratore.finestra.prodottiBtn.clicked.connect(
            lambda: amministratore.prodottiBtnClicked(mainPath, amministratore, None))
        amministratore.finestra.accountsBtn.clicked.connect(
            lambda: amministratore.accountsBtnClicked(mainPath, amministratore, None))
        amministratore.finestra.backupBtn.clicked.connect(
            lambda: amministratore.backupBtnClicked(mainPath, amministratore))

    # Metodo che apre la finestra del login
    def apriLoginView(self, mainPath):
        self.removeItem(self.finestra.verticalLayout)
        login = LoginView(mainPath)
        self.finestra.verticalLayout.addWidget(login.finestra)
        login.finestra.indietroBtn.clicked.connect(lambda: self.apriUserView(mainPath))
        login.finestra.confermaBtn.clicked.connect(lambda: self.loginViewConfermaView(mainPath, login))
        login.finestra.toggleEchoBtn.clicked.connect(lambda: login.toggleVisibility(login))

    # Metodo che rimuove un widget da un layout e ne mette un altro
    def removeAndAdd(self, item):
        for i in range(self.finestra.verticalLayout.count()): self.finestra.verticalLayout.itemAt(
            i).widget().deleteLater()
        self.finestra.verticalLayout.addWidget(item.finestra)

    # Metodo che tenta di rimuovere la finestra precedentemente aggiunta al layout
    def removeItem(self, layout):
        if layout.itemAt(0) == None:
            return
        try:
            layout.removeItem(self.finestra.verticalLayout.itemAt(0))
        except:
            pass

    # Metodo che gestisce l'interazioone con il pulsante conferma della loginView, apre una nuova finestra se
    # le credenziali sono errate
    # login = widget del login
    def loginViewConfermaView(self, mainPath, login):
        account = login.confermaBtn(login.finestra)
        if Logging.TypeClienteProprietario:
            self.apriClienteProprietarioView(mainPath, account)
        elif Logging.TypeAmministratore:
            self.apriAmministratoreView(mainPath)
        elif not Logging.TypeAmministratore and not Logging.TypeClienteProprietario:
            self.apriLoginView(mainPath)

    # Metodo per animare lo scorrimento del menu
    def slideRightMenu(self, login):
        # Get current left menu width
        width = login.finestra.rightMenu.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            # login.finestra.openRightMenu.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))

        # If maximized
        else:
            # Restore menu
            newWidth = 0
            # login.finestra.openRightMenu.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(login.finestra.rightMenu, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # Metodo per animare lo scorrimento del menu
    def slideLeftMenu(self, login):
        # Get current left menu width
        width = login.finestra.leftMenu.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            # login.finestra.openLeftMenu.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            # login.finestra.openLeftMenu.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(login.finestra.leftMenu, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
