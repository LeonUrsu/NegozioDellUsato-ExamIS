import sys

from Custom_Widgets.Widgets import *
from ui_interface_vuota import *



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.mainpage = Ui_MainWindow()
        self.mainpage.setupUi(self)

        self.mainpage.homeBtn.clicked.connect(lambda: self.mainpage.finestreSecondarie.setCurrentWidget(
        self.mainpage.home))
        self.mainpage.homeBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.homeBtn.objectName()))


        self.mainpage.prodottiBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.prodotti))
        self.mainpage.prodottiBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.prodottiBtn.objectName()))

        #self.mainpage.prodottiBtn.clicked.connect(self.on_clicked1)
        #self.mainpage.prodottiBtn.clicked.connect(self.on_clicked2)
        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.mainpage)
        ########################################################################

        #Mostra finestra
        self.show()

    def changeStyleSheet(self,bottone):
        self.mainpage.leftMenu.setStyleSheet(f"#{bottone}"
                                             "\n{"
"background-color:#1a1f39;\n"
"padding : 10px 5px;\n"
"text-align:left;\n"
"border-top-left-radius:25px;\n}\nQPushButton\n{\nbackground-color:#2a2c49;\n"
"border = 0px;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	color:#78799c;\n}")


# esegui app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    #end






