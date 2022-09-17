# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_interfacedrjAAe.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
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
"#searchFrame{\n"
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
"#productsFrame{\n"
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
"	border: 2px solid #1a1f39;\n"
"	background-color:#1a1f39;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	border-top-left-radius:25px;\n"
"}\n"
"\n"
"#prodottiBtn, #statisticBtn, #infoBtn, QPushButton{\n"
""
                        "	padding : 10px 5px;\n"
"	text-align:left;\n"
"	color:#78799c;\n"
"	font: 75 10pt \"Leelawadee UI\";\n"
"}\n"
"\n"
"\n"
"#frame_3{\n"
"	background-color:#2a2c49;\n"
"	border: solid;\n"
"	border-radius: 20px;\n"
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
        self.verticalLayout_3.setContentsMargins(0, 0, 4, 0)
        self.frame_5 = QFrame(self.leftMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 60, 9, 0)

        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignTop)

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
        font.setWeight(9)
        self.homeBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/purpleIcons/assets/#78799c(purple) icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.statisticBtn = QPushButton(self.frame_6)
        self.statisticBtn.setObjectName(u"statisticBtn")
        self.statisticBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/purpleIcons/assets/#78799c(purple) icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statisticBtn.setIcon(icon1)
        self.statisticBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.statisticBtn)

        self.prodottiBtn = QPushButton(self.frame_6)
        self.prodottiBtn.setObjectName(u"prodottiBtn")
        self.prodottiBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/purpleIcons/assets/#78799c(purple) icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prodottiBtn.setIcon(icon2)
        self.prodottiBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.prodottiBtn)

        self.infoBtn = QPushButton(self.frame_6)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/purpleIcons/assets/#78799c(purple) icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon3)
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
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
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
        icon4 = QIcon()
        icon4.addFile(u":/purpleIcons/assets/#78799c(purple) icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon4)
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
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/purpleIcons/assets/#78799c(purple) icons/search.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEdit.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_4.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_3 = QWidget(self.mainFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountButton = QPushButton(self.widget_3)
        self.accountButton.setObjectName(u"accountButton")
        icon5 = QIcon()
        icon5.addFile(u":/purpleIcons/assets/#78799c(purple) icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountButton.setIcon(icon5)
        self.accountButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.accountButton)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.mainFrame, 0, Qt.AlignTop)

        self.productsFrame = QWidget(self.mainBody)
        self.productsFrame.setObjectName(u"productsFrame")
        sizePolicy.setHeightForWidth(self.productsFrame.sizePolicy().hasHeightForWidth())
        self.productsFrame.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.productsFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.widget_4 = QWidget(self.productsFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.prodottiHeader = QLabel(self.frame)
        self.prodottiHeader.setObjectName(u"prodottiHeader")
        sizePolicy.setHeightForWidth(self.prodottiHeader.sizePolicy().hasHeightForWidth())
        self.prodottiHeader.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Leelawadee UI")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.prodottiHeader.setFont(font2)

        self.horizontalLayout_8.addWidget(self.prodottiHeader)

        self.avantiarw = QPushButton(self.frame)
        self.avantiarw.setObjectName(u"avantiarw")
        self.avantiarw.setMinimumSize(QSize(24, 24))
        self.avantiarw.setMaximumSize(QSize(24, 24))
        icon6 = QIcon()
        icon6.addFile(u":/blackIcons/assets/#000(black) icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.avantiarw.setIcon(icon6)
        self.avantiarw.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.avantiarw)


        self.horizontalLayout_7.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.productsContainer = QFrame(self.productsFrame)
        self.productsContainer.setObjectName(u"productsContainer")
        sizePolicy.setHeightForWidth(self.productsContainer.sizePolicy().hasHeightForWidth())
        self.productsContainer.setSizePolicy(sizePolicy)
        self.productsContainer.setFrameShape(QFrame.StyledPanel)
        self.productsContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.productsContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.productsContainer)
        self.label_36.setObjectName(u"label_36")
        font3 = QFont()
        font3.setFamily(u"Leelawadee UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_36.setFont(font3)

        self.gridLayout.addWidget(self.label_36, 2, 3, 1, 1)

        self.label_43 = QLabel(self.productsContainer)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)

        self.gridLayout.addWidget(self.label_43, 9, 3, 1, 1)

        self.label_48 = QLabel(self.productsContainer)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)

        self.gridLayout.addWidget(self.label_48, 5, 4, 1, 1)

        self.label_25 = QLabel(self.productsContainer)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.gridLayout.addWidget(self.label_25, 9, 1, 1, 1)

        self.label_38 = QLabel(self.productsContainer)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.gridLayout.addWidget(self.label_38, 4, 3, 1, 1)

        self.label_41 = QLabel(self.productsContainer)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.gridLayout.addWidget(self.label_41, 7, 3, 1, 1)

        self.label_32 = QLabel(self.productsContainer)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.gridLayout.addWidget(self.label_32, 1, 3, 1, 1)

        self.label_46 = QLabel(self.productsContainer)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.gridLayout.addWidget(self.label_46, 3, 4, 1, 1)

        self.label_56 = QLabel(self.productsContainer)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)

        self.gridLayout.addWidget(self.label_56, 4, 5, 1, 1)

        self.label_28 = QLabel(self.productsContainer)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout.addWidget(self.label_28, 3, 2, 1, 1)

        self.label_45 = QLabel(self.productsContainer)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)

        self.gridLayout.addWidget(self.label_45, 2, 4, 1, 1)

        self.label_24 = QLabel(self.productsContainer)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.gridLayout.addWidget(self.label_24, 8, 1, 1, 1)

        self.label_11 = QLabel(self.productsContainer)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.label = QLabel(self.productsContainer)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_61 = QLabel(self.productsContainer)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font3)

        self.gridLayout.addWidget(self.label_61, 9, 5, 1, 1)

        self.label_29 = QLabel(self.productsContainer)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.gridLayout.addWidget(self.label_29, 4, 2, 1, 1)

        self.label_22 = QLabel(self.productsContainer)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.gridLayout.addWidget(self.label_22, 6, 1, 1, 1)

        self.label_16 = QLabel(self.productsContainer)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)

        self.label_52 = QLabel(self.productsContainer)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)

        self.gridLayout.addWidget(self.label_52, 9, 4, 1, 1)

        self.label_30 = QLabel(self.productsContainer)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.gridLayout.addWidget(self.label_30, 5, 2, 1, 1)

        self.label_23 = QLabel(self.productsContainer)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.gridLayout.addWidget(self.label_23, 7, 1, 1, 1)

        self.label_9 = QLabel(self.productsContainer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_14 = QLabel(self.productsContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)

        self.label_34 = QLabel(self.productsContainer)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.gridLayout.addWidget(self.label_34, 8, 2, 1, 1)

        self.label_27 = QLabel(self.productsContainer)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout.addWidget(self.label_27, 2, 2, 1, 1)

        self.label_47 = QLabel(self.productsContainer)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font3)

        self.gridLayout.addWidget(self.label_47, 4, 4, 1, 1)

        self.label_37 = QLabel(self.productsContainer)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.gridLayout.addWidget(self.label_37, 3, 3, 1, 1)

        self.label_8 = QLabel(self.productsContainer)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_33 = QLabel(self.productsContainer)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.gridLayout.addWidget(self.label_33, 7, 2, 1, 1)

        self.label_5 = QLabel(self.productsContainer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_31 = QLabel(self.productsContainer)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.gridLayout.addWidget(self.label_31, 6, 2, 1, 1)

        self.label_59 = QLabel(self.productsContainer)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)

        self.gridLayout.addWidget(self.label_59, 7, 5, 1, 1)

        self.label_40 = QLabel(self.productsContainer)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.gridLayout.addWidget(self.label_40, 6, 3, 1, 1)

        self.label_60 = QLabel(self.productsContainer)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)

        self.gridLayout.addWidget(self.label_60, 8, 5, 1, 1)

        self.label_44 = QLabel(self.productsContainer)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.gridLayout.addWidget(self.label_44, 1, 4, 1, 1)

        self.label_39 = QLabel(self.productsContainer)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)

        self.gridLayout.addWidget(self.label_39, 5, 3, 1, 1)

        self.label_17 = QLabel(self.productsContainer)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)

        self.label_50 = QLabel(self.productsContainer)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)

        self.gridLayout.addWidget(self.label_50, 7, 4, 1, 1)

        self.label_53 = QLabel(self.productsContainer)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)

        self.gridLayout.addWidget(self.label_53, 1, 5, 1, 1)

        self.label_55 = QLabel(self.productsContainer)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)

        self.gridLayout.addWidget(self.label_55, 3, 5, 1, 1)

        self.label_58 = QLabel(self.productsContainer)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)

        self.gridLayout.addWidget(self.label_58, 6, 5, 1, 1)

        self.label_6 = QLabel(self.productsContainer)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_7 = QLabel(self.productsContainer)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)

        self.label_35 = QLabel(self.productsContainer)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.gridLayout.addWidget(self.label_35, 9, 2, 1, 1)

        self.label_10 = QLabel(self.productsContainer)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_54 = QLabel(self.productsContainer)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.gridLayout.addWidget(self.label_54, 2, 5, 1, 1)

        self.label_57 = QLabel(self.productsContainer)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)

        self.gridLayout.addWidget(self.label_57, 5, 5, 1, 1)

        self.label_49 = QLabel(self.productsContainer)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font3)

        self.gridLayout.addWidget(self.label_49, 6, 4, 1, 1)

        self.label_15 = QLabel(self.productsContainer)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)

        self.label_20 = QLabel(self.productsContainer)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.gridLayout.addWidget(self.label_20, 4, 1, 1, 1)

        self.label_26 = QLabel(self.productsContainer)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.gridLayout.addWidget(self.label_26, 1, 2, 1, 1)

        self.label_51 = QLabel(self.productsContainer)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font3)

        self.gridLayout.addWidget(self.label_51, 8, 4, 1, 1)

        self.label_4 = QLabel(self.productsContainer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_21 = QLabel(self.productsContainer)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.gridLayout.addWidget(self.label_21, 5, 1, 1, 1)

        self.label_42 = QLabel(self.productsContainer)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font3)

        self.gridLayout.addWidget(self.label_42, 8, 3, 1, 1)

        self.label_3 = QLabel(self.productsContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_13 = QLabel(self.productsContainer)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)

        self.label_19 = QLabel(self.productsContainer)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.gridLayout.addWidget(self.label_19, 3, 1, 1, 1)

        self.label_18 = QLabel(self.productsContainer)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.gridLayout.addWidget(self.label_18, 2, 1, 1, 1)

        self.label_12 = QLabel(self.productsContainer)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.productsContainer)


        self.verticalLayout.addWidget(self.productsFrame, 0, Qt.AlignTop)

        self.statisticFrame = QWidget(self.mainBody)
        self.statisticFrame.setObjectName(u"statisticFrame")
        sizePolicy.setHeightForWidth(self.statisticFrame.sizePolicy().hasHeightForWidth())
        self.statisticFrame.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.statisticFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        self.profileCont = QCustomSlideMenu(self.centralwidget)
        self.profileCont.setObjectName(u"profileCont")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profileCont.sizePolicy().hasHeightForWidth())
        self.profileCont.setSizePolicy(sizePolicy2)
        self.profileCont.setMinimumSize(QSize(100, 0))
        self.verticalLayout_6 = QVBoxLayout(self.profileCont)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 8, 0)
        self.frame_3 = QFrame(self.profileCont)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(30, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.loginBtn = QPushButton(self.frame_3)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamily(u"Leelawadee UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.loginBtn.setFont(font4)
        icon7 = QIcon()
        icon7.addFile(u":/purpleIcons/assets/#78799c(purple) icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon7)
        self.loginBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.loginBtn)

        self.quitBtn = QPushButton(self.frame_3)
        self.quitBtn.setObjectName(u"quitBtn")
        sizePolicy3.setHeightForWidth(self.quitBtn.sizePolicy().hasHeightForWidth())
        self.quitBtn.setSizePolicy(sizePolicy3)
        self.quitBtn.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/purpleIcons/assets/#78799c(purple) icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quitBtn.setIcon(icon8)
        self.quitBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.quitBtn)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.profileCont)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.statisticBtn.setText(QCoreApplication.translate("MainWindow", u"Statistiche", None))
        self.prodottiBtn.setText(QCoreApplication.translate("MainWindow", u"Prodotti", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menuButton.setText("")
        self.applicationName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Usato</span><span style=\" font-size:28pt; font-weight:600; color:#aaaaff;\">Beato</span></p></body></html>", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cerca", None))
        self.accountButton.setText("")
        self.prodottiHeader.setText(QCoreApplication.translate("MainWindow", u"Ultimi Prodotti", None))
        self.avantiarw.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Prodotto", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.quitBtn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

