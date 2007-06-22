# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jun 19 15:47:03 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,738,211).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.buttonClose = QtGui.QPushButton(self.centralwidget)
        self.buttonClose.setGeometry(QtCore.QRect(130,10,113,32))
        self.buttonClose.setObjectName("buttonClose")

        self.buttonOpen = QtGui.QPushButton(self.centralwidget)
        self.buttonOpen.setGeometry(QtCore.QRect(20,10,113,32))
        self.buttonOpen.setObjectName("buttonOpen")

        self.FisheryDataTable = QtGui.QTableWidget(self.centralwidget)
        self.FisheryDataTable.setGeometry(QtCore.QRect(20,50,701,121))
        self.FisheryDataTable.setObjectName("FisheryDataTable")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,738,22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")

        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")

        self.MenuOpenProject = QtGui.QAction(MainWindow)
        self.MenuOpenProject.setObjectName("MenuOpenProject")
        self.menuFile.addAction(self.MenuOpenProject)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonClose,QtCore.SIGNAL("clicked()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.clear()
        self.FisheryDataTable.setColumnCount(4)
        self.FisheryDataTable.setRowCount(3)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("MainWindow", "Fisher\'s current interest to start a certificate program", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setVerticalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("MainWindow", "Level of understanding of population dynamics", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setVerticalHeaderItem(1,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("MainWindow", "Years for which catch per unit data are available", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setVerticalHeaderItem(2,headerItem2)

        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("MainWindow", "Hilsa Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setHorizontalHeaderItem(0,headerItem3)

        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(QtGui.QApplication.translate("MainWindow", "Shark Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setHorizontalHeaderItem(1,headerItem4)

        headerItem5 = QtGui.QTableWidgetItem()
        headerItem5.setText(QtGui.QApplication.translate("MainWindow", "Kerala Mussels", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setHorizontalHeaderItem(2,headerItem5)

        headerItem6 = QtGui.QTableWidgetItem()
        headerItem6.setText(QtGui.QApplication.translate("MainWindow", "Babylonia Snail", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable.setHorizontalHeaderItem(3,headerItem6)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.MenuOpenProject.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))

