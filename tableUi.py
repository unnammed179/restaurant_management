# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listTable = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listTable.sizePolicy().hasHeightForWidth())
        self.listTable.setSizePolicy(sizePolicy)
        self.listTable.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listTable.setObjectName("listTable")
        self.horizontalLayout_2.addWidget(self.listTable)
        self.listPrice = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listPrice.sizePolicy().hasHeightForWidth())
        self.listPrice.setSizePolicy(sizePolicy)
        self.listPrice.setMinimumSize(QtCore.QSize(50, 0))
        self.listPrice.setMaximumSize(QtCore.QSize(500, 16777215))
        self.listPrice.setObjectName("listPrice")
        self.horizontalLayout_2.addWidget(self.listPrice)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 3, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 3, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 3, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 5, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 2, 0, 1, 1)
        self.btnDel = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnDel.setObjectName("btnDel")
        self.gridLayout.addWidget(self.btnDel, 5, 0, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 4, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 4, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 4, 2, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 10, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.btn2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 2, 1, 1, 1)
        self.btnOk = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnOk.setObjectName("btnOk")
        self.gridLayout.addWidget(self.btnOk, 5, 2, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.lcdTable = QtWidgets.QLCDNumber(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdTable.sizePolicy().hasHeightForWidth())
        self.lcdTable.setSizePolicy(sizePolicy)
        self.lcdTable.setObjectName("lcdTable")
        self.gridLayout.addWidget(self.lcdTable, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 2, 0, 1, 1)
        self.sum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sum.sizePolicy().hasHeightForWidth())
        self.sum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sum.setFont(font)
        self.sum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sum.setText("")
        self.sum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sum.setObjectName("sum")
        self.gridLayout_2.addWidget(self.sum, 0, 0, 1, 1)
        self.ongoing = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ongoing.sizePolicy().hasHeightForWidth())
        self.ongoing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ongoing.setFont(font)
        self.ongoing.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ongoing.setText("")
        self.ongoing.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ongoing.setObjectName("ongoing")
        self.gridLayout_2.addWidget(self.ongoing, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Table"))
        self.label_3.setText(_translate("MainWindow", "Price"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btnDel.setText(_translate("MainWindow", "<-"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Pick Table"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btnOk.setText(_translate("MainWindow", "OK"))
        self.btn3.setText(_translate("MainWindow", "3"))
