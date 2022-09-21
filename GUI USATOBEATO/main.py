import sys

from products_interface import *
from Custom_Widgets.Widgets import *
from ui_interface import *
from gui import *
from ui_interface_vuota import *



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_InterfaceVuota()
        self.ui.setupUi(self)
        self.ux = Ui_ProductsFrame()
        self.ux.setupUi(self)

        self.ui.prodottiBtn.clicked.connect(self.ui.frameVuoto)
        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        #Mostra finestra
        self.show()



# esegui app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    #end






