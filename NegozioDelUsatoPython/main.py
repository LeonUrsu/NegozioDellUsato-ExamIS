import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore , QtGui, QtWidgets

from MVC.View.AmministratoreView import AmministratoreView1
from MVC.View.ui_AmministratoreView import Ui_MainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = AmministratoreView1()
    sys.exit(app.exec())


