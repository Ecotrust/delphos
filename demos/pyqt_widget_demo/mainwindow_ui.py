# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jun 30 15:43:53 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,1079,619).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabProject = QtGui.QTabWidget(self.centralwidget)
        self.tabProject.setGeometry(QtCore.QRect(10,10,1051,566))
        self.tabProject.setObjectName("tabProject")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10,10,111,56))
        self.groupBox.setObjectName("groupBox")

        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(0,0,113,32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(0,25,113,32))
        self.pushButton_5.setObjectName("pushButton_5")

        self.tableWidget_3 = QtGui.QTableWidget(self.tab)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(130,10,206,331))
        self.tableWidget_3.setMouseTracking(False)
        self.tableWidget_3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tabProject.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10,10,113,32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10,60,113,32))
        self.pushButton_4.setObjectName("pushButton_4")

        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10,10,111,81))
        self.groupBox_2.setObjectName("groupBox_2")

        self.pushButton_7 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(0,25,113,32))
        self.pushButton_7.setObjectName("pushButton_7")

        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(130,10,901,306))
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tabProject.addTab(self.tab_2,"")

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.tabWidget = QtGui.QTabWidget(self.tab_4)
        self.tabWidget.setGeometry(QtCore.QRect(50,40,711,396))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")

        self.tableWidget_4 = QtGui.QTableWidget(self.tab_7)
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setGeometry(QtCore.QRect(15,10,206,331))
        self.tableWidget_4.setMouseTracking(False)
        self.tableWidget_4.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tabWidget.addTab(self.tab_7,"")

        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8,"")

        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.FisheryDataTable_2 = QtGui.QTableWidget(self.tab_5)
        self.FisheryDataTable_2.setGeometry(QtCore.QRect(5,20,751,119))
        self.FisheryDataTable_2.setObjectName("FisheryDataTable_2")
        self.tabWidget.addTab(self.tab_5,"")

        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6,"")

        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9,"")
        self.tabProject.addTab(self.tab_4,"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1079,22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
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

        self.actionExit_Delphos = QtGui.QAction(MainWindow)
        self.actionExit_Delphos.setObjectName("actionExit_Delphos")

        self.actionAbout_Delphos = QtGui.QAction(MainWindow)
        self.actionAbout_Delphos.setObjectName("actionAbout_Delphos")

        self.actionDelphos_Help = QtGui.QAction(MainWindow)
        self.actionDelphos_Help.setObjectName("actionDelphos_Help")

        self.actionExit_Delphos_2 = QtGui.QAction(MainWindow)
        self.actionExit_Delphos_2.setObjectName("actionExit_Delphos_2")
        self.menuFile.addAction(self.MenuOpenProject)
        self.menuFile.addAction(self.actionExit_Delphos)
        self.menuFile.addAction(self.actionExit_Delphos_2)
        self.menuHelp.addAction(self.actionDelphos_Help)
        self.menuAbout.addAction(self.actionAbout_Delphos)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabProject.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.clear()
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(10)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setVerticalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setVerticalHeaderItem(1,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setVerticalHeaderItem(2,headerItem2)

        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setVerticalHeaderItem(3,headerItem3)

        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setHorizontalHeaderItem(0,headerItem4)

        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Hilsa Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setItem(0,0,item)

        item1 = QtGui.QTableWidgetItem()
        item1.setText(QtGui.QApplication.translate("MainWindow", "Shark Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setItem(1,0,item1)

        item2 = QtGui.QTableWidgetItem()
        item2.setText(QtGui.QApplication.translate("MainWindow", "Kerala Mussels", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setItem(2,0,item2)

        item3 = QtGui.QTableWidgetItem()
        item3.setText(QtGui.QApplication.translate("MainWindow", "Babylonia Snail", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_3.setItem(3,0,item3)
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Alternatives", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.clear()
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(10)

        headerItem5 = QtGui.QTableWidgetItem()
        headerItem5.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setVerticalHeaderItem(0,headerItem5)

        headerItem6 = QtGui.QTableWidgetItem()
        headerItem6.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setVerticalHeaderItem(1,headerItem6)

        headerItem7 = QtGui.QTableWidgetItem()
        headerItem7.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setVerticalHeaderItem(2,headerItem7)

        headerItem8 = QtGui.QTableWidgetItem()
        headerItem8.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setVerticalHeaderItem(3,headerItem8)

        headerItem9 = QtGui.QTableWidgetItem()
        headerItem9.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setVerticalHeaderItem(4,headerItem9)

        headerItem10 = QtGui.QTableWidgetItem()
        headerItem10.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setVerticalHeaderItem(5,headerItem10)

        headerItem11 = QtGui.QTableWidgetItem()
        headerItem11.setText(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setHorizontalHeaderItem(0,headerItem11)

        headerItem12 = QtGui.QTableWidgetItem()
        headerItem12.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setHorizontalHeaderItem(1,headerItem12)

        headerItem13 = QtGui.QTableWidgetItem()
        headerItem13.setText(QtGui.QApplication.translate("MainWindow", "Cost/Benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setHorizontalHeaderItem(2,headerItem13)

        item4 = QtGui.QTableWidgetItem()
        item4.setText(QtGui.QApplication.translate("MainWindow", "ordinal", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(0,0,item4)

        item5 = QtGui.QTableWidgetItem()
        item5.setText(QtGui.QApplication.translate("MainWindow", "Fisher\'s current interest to start a certification program", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(0,1,item5)

        item6 = QtGui.QTableWidgetItem()
        item6.setText(QtGui.QApplication.translate("MainWindow", "benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(0,2,item6)

        item7 = QtGui.QTableWidgetItem()
        item7.setText(QtGui.QApplication.translate("MainWindow", "ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(1,0,item7)

        item8 = QtGui.QTableWidgetItem()
        item8.setText(QtGui.QApplication.translate("MainWindow", "Years for which catch per unit effort data are available", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(1,1,item8)

        item9 = QtGui.QTableWidgetItem()
        item9.setText(QtGui.QApplication.translate("MainWindow", "benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(1,2,item9)

        item10 = QtGui.QTableWidgetItem()
        item10.setText(QtGui.QApplication.translate("MainWindow", "ordinal", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(2,0,item10)

        item11 = QtGui.QTableWidgetItem()
        item11.setText(QtGui.QApplication.translate("MainWindow", "Level of understanding of population dynamics", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(2,1,item11)

        item12 = QtGui.QTableWidgetItem()
        item12.setText(QtGui.QApplication.translate("MainWindow", "benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(2,2,item12)

        item13 = QtGui.QTableWidgetItem()
        item13.setText(QtGui.QApplication.translate("MainWindow", "ordinal", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(3,0,item13)

        item14 = QtGui.QTableWidgetItem()
        item14.setText(QtGui.QApplication.translate("MainWindow", "Level of community participation in fishery management", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(3,1,item14)

        item15 = QtGui.QTableWidgetItem()
        item15.setText(QtGui.QApplication.translate("MainWindow", "benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(3,2,item15)

        item16 = QtGui.QTableWidgetItem()
        item16.setText(QtGui.QApplication.translate("MainWindow", "ordinal", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(4,0,item16)

        item17 = QtGui.QTableWidgetItem()
        item17.setText(QtGui.QApplication.translate("MainWindow", "By catch level", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(4,1,item17)

        item18 = QtGui.QTableWidgetItem()
        item18.setText(QtGui.QApplication.translate("MainWindow", "benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(4,2,item18)

        item19 = QtGui.QTableWidgetItem()
        item19.setText(QtGui.QApplication.translate("MainWindow", "ordinal", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(5,0,item19)

        item20 = QtGui.QTableWidgetItem()
        item20.setText(QtGui.QApplication.translate("MainWindow", "Gear ecosystem interactions", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(5,1,item20)

        item21 = QtGui.QTableWidgetItem()
        item21.setText(QtGui.QApplication.translate("MainWindow", "benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setItem(5,2,item21)
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setRowCount(10)
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.clear()
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(10)

        headerItem14 = QtGui.QTableWidgetItem()
        headerItem14.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setVerticalHeaderItem(0,headerItem14)

        headerItem15 = QtGui.QTableWidgetItem()
        headerItem15.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setVerticalHeaderItem(1,headerItem15)

        headerItem16 = QtGui.QTableWidgetItem()
        headerItem16.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setVerticalHeaderItem(2,headerItem16)

        headerItem17 = QtGui.QTableWidgetItem()
        headerItem17.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setVerticalHeaderItem(3,headerItem17)

        headerItem18 = QtGui.QTableWidgetItem()
        headerItem18.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setHorizontalHeaderItem(0,headerItem18)

        item22 = QtGui.QTableWidgetItem()
        item22.setText(QtGui.QApplication.translate("MainWindow", "Hilsa Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setItem(0,0,item22)

        item23 = QtGui.QTableWidgetItem()
        item23.setText(QtGui.QApplication.translate("MainWindow", "Shark Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setItem(1,0,item23)

        item24 = QtGui.QTableWidgetItem()
        item24.setText(QtGui.QApplication.translate("MainWindow", "Kerala Mussels", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setItem(2,0,item24)

        item25 = QtGui.QTableWidgetItem()
        item25.setText(QtGui.QApplication.translate("MainWindow", "Babylonia Snail", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_4.setItem(3,0,item25)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("MainWindow", "Select Alternatives", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtGui.QApplication.translate("MainWindow", "Select Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.clear()
        self.FisheryDataTable_2.setColumnCount(4)
        self.FisheryDataTable_2.setRowCount(3)

        headerItem19 = QtGui.QTableWidgetItem()
        headerItem19.setText(QtGui.QApplication.translate("MainWindow", "Fisher\'s current interest to start a certificate program", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setVerticalHeaderItem(0,headerItem19)

        headerItem20 = QtGui.QTableWidgetItem()
        headerItem20.setText(QtGui.QApplication.translate("MainWindow", "Level of understanding of population dynamics", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setVerticalHeaderItem(1,headerItem20)

        headerItem21 = QtGui.QTableWidgetItem()
        headerItem21.setText(QtGui.QApplication.translate("MainWindow", "Level of communication in fishery management", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setVerticalHeaderItem(2,headerItem21)

        headerItem22 = QtGui.QTableWidgetItem()
        headerItem22.setText(QtGui.QApplication.translate("MainWindow", "Hilsa Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setHorizontalHeaderItem(0,headerItem22)

        headerItem23 = QtGui.QTableWidgetItem()
        headerItem23.setText(QtGui.QApplication.translate("MainWindow", "Shark Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setHorizontalHeaderItem(1,headerItem23)

        headerItem24 = QtGui.QTableWidgetItem()
        headerItem24.setText(QtGui.QApplication.translate("MainWindow", "Kerala Mussels", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setHorizontalHeaderItem(2,headerItem24)

        headerItem25 = QtGui.QTableWidgetItem()
        headerItem25.setText(QtGui.QApplication.translate("MainWindow", "Babylonia Snail", None, QtGui.QApplication.UnicodeUTF8))
        self.FisheryDataTable_2.setHorizontalHeaderItem(3,headerItem25)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Assign Weighting", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QtGui.QApplication.translate("MainWindow", "Run Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "MCA", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.MenuOpenProject.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_Delphos.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Delphos.setText(QtGui.QApplication.translate("MainWindow", "About Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelphos_Help.setText(QtGui.QApplication.translate("MainWindow", "Delphos Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_Delphos_2.setText(QtGui.QApplication.translate("MainWindow", "Exit Delphos", None, QtGui.QApplication.UnicodeUTF8))

