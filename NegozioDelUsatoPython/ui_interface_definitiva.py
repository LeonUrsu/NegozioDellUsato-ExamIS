# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_definitivahCOElW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 574)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color:#1a1f39;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"*{\n"
"color: #78799c;\n"
"border: none;\n"
"}\n"
"\n"
"#frame_2, #frame_5{\n"
"	background-color: #2a2c49;\n"
"}\n"
"\n"
"#mainBody,#centralwidget{\n"
"	background-color: #1a1f39;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"#searchFrame, QLineEdit{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #78799c;\n"
"}\n"
"\n"
"#appHeader{\n"
"	color:#78799c;\n"
"}\n"
"\n"
"#prodottiHeader{\n"
"	color:  #a06ce3;\n"
"}\n"
"\n"
"#avantiarw{\n"
"	border: 1px solid #a06ce3;\n"
"	background-color: #a06ce3 ;\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"\n"
"#finestreSecondarie{\n"
"	background-color: #2a2c49;\n"
"	border: solid;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:#78799c;\n"
"}\n"
"\n"
"#mainFrame{\n"
"	background-color: #2a2c49;\n"
"}\n"
"\n"
"#homeBtn{\n"
"	color:#78799c;\n"
"	background-color:#1a1f39;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	border-top-left-radius:25px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	col"
                        "or:#78799c;\n"
"	font: 10pt \"Leelawadee UI\";\n"
"}\n"
"\n"
"\n"
"#frame_3{\n"
"	background-color:#2a2c49;\n"
"	border: solid;\n"
"	border-radius: 20px;\n"
"}\n"
"QTableWidget{\n"
"	background-color:#2a2c49;\n"
"	border: solid;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(230, 0))
        self.leftMenu.setMaximumSize(QSize(230, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.leftMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 68, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.leftMenu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_6)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setFamily(u"Leelawadee UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/purpleIcons/assets/#78799c(purple) icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.statisticBtn = QPushButton(self.frame_6)
        self.statisticBtn.setObjectName(u"statisticBtn")
        self.statisticBtn.setFont(font)
        self.statisticBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/purpleIcons/assets/#78799c(purple) icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statisticBtn.setIcon(icon1)
        self.statisticBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.statisticBtn)

        self.prodottiBtn = QPushButton(self.frame_6)
        self.prodottiBtn.setObjectName(u"prodottiBtn")
        self.prodottiBtn.setFont(font)
        self.prodottiBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/purpleIcons/assets/#78799c(purple) icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prodottiBtn.setIcon(icon2)
        self.prodottiBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.prodottiBtn)

        self.accountBtn = QPushButton(self.frame_6)
        self.accountBtn.setObjectName(u"accountBtn")
        self.accountBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/purpleIcons/assets/#78799c(purple) icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.accountBtn)

        self.infoBtn = QPushButton(self.frame_6)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        self.infoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/purpleIcons/assets/#78799c(purple) icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.infoBtn, 0, Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QWidget(self.mainBody)
        self.mainFrame.setObjectName(u"mainFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.widget = QWidget(self.mainFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.widget)
        self.menuButton.setObjectName(u"menuButton")
        icon5 = QIcon()
        icon5.addFile(u":/purpleIcons/assets/#78799c(purple) icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon5)
        self.menuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuButton)

        self.applicationName = QLabel(self.widget)
        self.applicationName.setObjectName(u"applicationName")

        self.horizontalLayout_3.addWidget(self.applicationName)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_2 = QWidget(self.mainFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_3 = QWidget(self.mainFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountButton = QPushButton(self.widget_3)
        self.accountButton.setObjectName(u"accountButton")
        self.accountButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/purpleIcons/assets/#78799c(purple) icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountButton.setIcon(icon6)
        self.accountButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.accountButton)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.mainFrame, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.mainBody)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.finestreSecondarie = QStackedWidget(self.widget_4)
        self.finestreSecondarie.setObjectName(u"finestreSecondarie")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_8 = QVBoxLayout(self.home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.home)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.finestreSecondarie.addWidget(self.home)
        self.statistiche = QWidget()
        self.statistiche.setObjectName(u"statistiche")
        self.label = QLabel(self.statistiche)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 160, 55, 16))
        self.finestreSecondarie.addWidget(self.statistiche)
        self.accounts = QWidget()
        self.accounts.setObjectName(u"accounts")
        self.label_5 = QLabel(self.accounts)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 130, 55, 16))
        self.finestreSecondarie.addWidget(self.accounts)
        self.prodotti = QWidget()
        self.prodotti.setObjectName(u"prodotti")
        self.horizontalLayout_7 = QHBoxLayout(self.prodotti)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget = QTableWidget(self.prodotti)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(170, 170, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_7.addWidget(self.tableWidget)

        self.frame = QFrame(self.prodotti)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.searchFrame = QFrame(self.frame)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.searchFrame.setFont(font1)
        self.searchFrame.setCursor(QCursor(Qt.IBeamCursor))
        self.searchFrame.setFocusPolicy(Qt.NoFocus)
        self.searchFrame.setContextMenuPolicy(Qt.CustomContextMenu)
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.searchFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon7 = QIcon()
        icon7.addFile(u":/purpleIcons/assets/#78799c(purple) icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.search_le = QLineEdit(self.searchFrame)
        self.search_le.setObjectName(u"search_le")

        self.horizontalLayout_8.addWidget(self.search_le)


        self.verticalLayout_9.addWidget(self.searchFrame, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 15, 0, 0)
        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        self.vboxLayout = QVBoxLayout(self.groupBox)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/purpleIcons/assets/#78799c(purple) icons/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon8)

        self.vboxLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setIcon(icon8)

        self.vboxLayout.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setIcon(icon8)

        self.vboxLayout.addWidget(self.pushButton_2, 0, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.groupBox, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_salva_rimuovi = QFrame(self.frame)
        self.frame_salva_rimuovi.setObjectName(u"frame_salva_rimuovi")
        sizePolicy.setHeightForWidth(self.frame_salva_rimuovi.sizePolicy().hasHeightForWidth())
        self.frame_salva_rimuovi.setSizePolicy(sizePolicy)
        self.frame_salva_rimuovi.setMinimumSize(QSize(0, 30))
        self.frame_salva_rimuovi.setStyleSheet(u"QPushButton{\n"
"	color:#78799c;\n"
"	background-color:#1a1f39;\n"
"	border-radius: 15px;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	color:#78799c;\n"
"	font: 10pt \"Leelawadee UI\";\n"
"}\n"
"")
        self.frame_salva_rimuovi.setFrameShape(QFrame.StyledPanel)
        self.frame_salva_rimuovi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_salva_rimuovi)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.aggiungiBtn = QPushButton(self.frame_salva_rimuovi)
        self.aggiungiBtn.setObjectName(u"aggiungiBtn")
        self.aggiungiBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/purpleIcons/assets/#78799c(purple) icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aggiungiBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.aggiungiBtn, 0, Qt.AlignHCenter)

        self.rimuoviBtn = QPushButton(self.frame_salva_rimuovi)
        self.rimuoviBtn.setObjectName(u"rimuoviBtn")
        self.rimuoviBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/purpleIcons/assets/#78799c(purple) icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rimuoviBtn.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.rimuoviBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_salva_rimuovi, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.frame)

        self.finestreSecondarie.addWidget(self.prodotti)
        self.aggiungiProdottopg = QWidget()
        self.aggiungiProdottopg.setObjectName(u"aggiungiProdottopg")
        self.horizontalLayout_11 = QHBoxLayout(self.aggiungiProdottopg)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.addProdottoFrm = QFrame(self.aggiungiProdottopg)
        self.addProdottoFrm.setObjectName(u"addProdottoFrm")
        self.addProdottoFrm.setFrameShape(QFrame.StyledPanel)
        self.addProdottoFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.addProdottoFrm)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.nomeLe = QLineEdit(self.addProdottoFrm)
        self.nomeLe.setObjectName(u"nomeLe")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.nomeLe.setFont(font2)
        self.nomeLe.setCursorPosition(0)

        self.verticalLayout_11.addWidget(self.nomeLe)

        self.idAccountLe = QLineEdit(self.addProdottoFrm)
        self.idAccountLe.setObjectName(u"idAccountLe")
        self.idAccountLe.setFont(font2)

        self.verticalLayout_11.addWidget(self.idAccountLe)

        self.prezzoLe = QLineEdit(self.addProdottoFrm)
        self.prezzoLe.setObjectName(u"prezzoLe")
        self.prezzoLe.setFont(font2)

        self.verticalLayout_11.addWidget(self.prezzoLe)

        self.idCategoriaLe = QLineEdit(self.addProdottoFrm)
        self.idCategoriaLe.setObjectName(u"idCategoriaLe")
        self.idCategoriaLe.setFont(font2)

        self.verticalLayout_11.addWidget(self.idCategoriaLe)

        self.idScaffaleLe = QLineEdit(self.addProdottoFrm)
        self.idScaffaleLe.setObjectName(u"idScaffaleLe")
        self.idScaffaleLe.setFont(font2)

        self.verticalLayout_11.addWidget(self.idScaffaleLe)

        self.saveBtn = QPushButton(self.addProdottoFrm)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveBtn.setStyleSheet(u"QPushButton{\n"
"	color:#78799c;\n"
"	background-color:#1a1f39;\n"
"	border-radius: 15px;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	color:#78799c;\n"
"	font: 10pt \"Leelawadee UI\";\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/purpleIcons/assets/#78799c(purple) icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon11)

        self.verticalLayout_11.addWidget(self.saveBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_11.addWidget(self.addProdottoFrm)

        self.finestreSecondarie.addWidget(self.aggiungiProdottopg)

        self.verticalLayout_2.addWidget(self.finestreSecondarie)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.mainBody)

        self.profileCont = QCustomSlideMenu(self.centralwidget)
        self.profileCont.setObjectName(u"profileCont")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.profileCont.sizePolicy().hasHeightForWidth())
        self.profileCont.setSizePolicy(sizePolicy3)
        self.profileCont.setMinimumSize(QSize(115, 0))
        self.verticalLayout_6 = QVBoxLayout(self.profileCont)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.frame_3 = QFrame(self.profileCont)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setMinimumSize(QSize(30, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 11, -1)
        self.quitBtn = QPushButton(self.frame_3)
        self.quitBtn.setObjectName(u"quitBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.quitBtn.sizePolicy().hasHeightForWidth())
        self.quitBtn.setSizePolicy(sizePolicy5)
        self.quitBtn.setFont(font)
        self.quitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/purpleIcons/assets/#78799c(purple) icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quitBtn.setIcon(icon12)
        self.quitBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.quitBtn)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.profileCont)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.finestreSecondarie.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.statisticBtn.setText(QCoreApplication.translate("MainWindow", u"Statistiche", None))
        self.prodottiBtn.setText(QCoreApplication.translate("MainWindow", u"Prodotti", None))
        self.accountBtn.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menuButton.setText("")
        self.applicationName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Usato</span><span style=\" font-size:28pt; font-weight:600; color:#aaaaff;\">Beato</span></p></body></html>", None))
        self.accountButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Statistiche", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Check", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data", None));
#if QT_CONFIG(tooltip)
        self.searchFrame.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.searchFrame.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.searchFrame.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.searchFrame.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_6.setText("")
        self.search_le.setInputMask("")
        self.search_le.setText("")
        self.search_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cerca Prodotto", None))
        self.groupBox.setTitle("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filtra Per Data", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Filtra Per Nome", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Filtra Per Prezzo", None))
        self.aggiungiBtn.setText(QCoreApplication.translate("MainWindow", u"Aggiungi", None))
        self.rimuoviBtn.setText(QCoreApplication.translate("MainWindow", u"Rimuovi", None))
        self.nomeLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Prodotto", None))
        self.idAccountLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"idAccount", None))
        self.prezzoLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.idCategoriaLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"idCategoria", None))
        self.idScaffaleLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"idScaffale", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Salva", None))
        self.quitBtn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi
