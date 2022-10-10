import sys

from PySide6.QtWidgets import QApplication

from AmministratoreView import AmministratoreView1

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = AmministratoreView1()
    sys.exit(app.exec())


