from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_prima(object):
    def setupUi(self, prima):
        if not prima.objectName():
            prima.setObjectName(u"prima")
        prima.resize(400, 300)
        self.button = QPushButton(prima)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(150, 130, 93, 28))
        self.exitbtn = QPushButton(prima)
        self.exitbtn.setObjectName(u"exitbtn")
        self.exitbtn.setGeometry(QRect(150, 170, 93, 28))
        self.label = QLabel(prima)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 90, 55, 16))

        self.retranslateUi(prima)

        QMetaObject.connectSlotsByName(prima)
    # setupUi

    def retranslateUi(self, prima):
        prima.setWindowTitle(QCoreApplication.translate("prima", u"Form", None))
        self.button.setText(QCoreApplication.translate("prima", u"seconda", None))
        self.exitbtn.setText(QCoreApplication.translate("prima", u"esci", None))
        self.label.setText(QCoreApplication.translate("prima", u"prima", None))
    # retranslateUi

