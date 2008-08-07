# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Jun 17 10:39:12 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010,719)
        MainWindow.setMinimumSize(QtCore.QSize(800,600))
        font = QtGui.QFont()
        font.setFamily("arial")
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1010,22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuDocumentation = QtGui.QMenu(self.menuView)
        self.menuDocumentation.setObjectName("menuDocumentation")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_doc = QtGui.QDockWidget(MainWindow)
        self.dock_doc.setMinimumSize(QtCore.QSize(300,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.dock_doc.setFont(font)
        self.dock_doc.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dock_doc.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dock_doc.setObjectName("dock_doc")
        self.dockWidgetContents = QtGui.QWidget(self.dock_doc)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setSpacing(8)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.toc_box = QtGui.QGroupBox(self.dockWidgetContents)
        self.toc_box.setMinimumSize(QtCore.QSize(0,120))
        self.toc_box.setMaximumSize(QtCore.QSize(16777215,170))
        self.toc_box.setObjectName("toc_box")
        self.hboxlayout = QtGui.QHBoxLayout(self.toc_box)
        self.hboxlayout.setObjectName("hboxlayout")
        self.toc_tree = QtGui.QTreeWidget(self.toc_box)
        self.toc_tree.setMinimumSize(QtCore.QSize(0,0))
        self.toc_tree.setMaximumSize(QtCore.QSize(400,167775))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.toc_tree.setFont(font)
        self.toc_tree.setObjectName("toc_tree")
        self.hboxlayout.addWidget(self.toc_tree)
        self.vboxlayout1.addWidget(self.toc_box)
        self.doc_box = QtGui.QGroupBox(self.dockWidgetContents)
        self.doc_box.setObjectName("doc_box")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.doc_box)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.doc_browser = HelpTextBrowser(self.doc_box)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.doc_browser.setFont(font)
        self.doc_browser.setOpenExternalLinks(True)
        self.doc_browser.setObjectName("doc_browser")
        self.vboxlayout2.addWidget(self.doc_browser)
        self.hboxlayout1.addLayout(self.vboxlayout2)
        self.vboxlayout1.addWidget(self.doc_box)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.dock_doc.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dock_doc)
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.menu_open_project = QtGui.QAction(MainWindow)
        self.menu_open_project.setEnabled(True)
        self.menu_open_project.setVisible(True)
        self.menu_open_project.setObjectName("menu_open_project")
        self.actionExit_Delphos = QtGui.QAction(MainWindow)
        self.actionExit_Delphos.setObjectName("actionExit_Delphos")
        self.menu_credits = QtGui.QAction(MainWindow)
        self.menu_credits.setEnabled(True)
        self.menu_credits.setObjectName("menu_credits")
        self.actionDelphos_Help = QtGui.QAction(MainWindow)
        self.actionDelphos_Help.setVisible(True)
        self.actionDelphos_Help.setObjectName("actionDelphos_Help")
        self.menu_exit_delphos = QtGui.QAction(MainWindow)
        self.menu_exit_delphos.setObjectName("menu_exit_delphos")
        self.menu_open_full_doc = QtGui.QAction(MainWindow)
        self.menu_open_full_doc.setEnabled(True)
        self.menu_open_full_doc.setObjectName("menu_open_full_doc")
        self.menu_create_project = QtGui.QAction(MainWindow)
        self.menu_create_project.setEnabled(True)
        self.menu_create_project.setVisible(True)
        self.menu_create_project.setObjectName("menu_create_project")
        self.menu_file = QtGui.QAction(MainWindow)
        self.menu_file.setObjectName("menu_file")
        self.actionClose_Project = QtGui.QAction(MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionAbout_Delphos_2 = QtGui.QAction(MainWindow)
        self.actionAbout_Delphos_2.setObjectName("actionAbout_Delphos_2")
        self.menu_dock_visible = QtGui.QAction(MainWindow)
        self.menu_dock_visible.setCheckable(True)
        self.menu_dock_visible.setChecked(True)
        self.menu_dock_visible.setObjectName("menu_dock_visible")
        self.menu_dock_floating = QtGui.QAction(MainWindow)
        self.menu_dock_floating.setCheckable(True)
        self.menu_dock_floating.setChecked(True)
        self.menu_dock_floating.setObjectName("menu_dock_floating")
        self.menu_about = QtGui.QAction(MainWindow)
        self.menu_about.setObjectName("menu_about")
        self.menu_main_menu = QtGui.QAction(MainWindow)
        self.menu_main_menu.setObjectName("menu_main_menu")
        self.menuFile.addAction(self.menu_main_menu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_open_project)
        self.menuFile.addAction(self.menu_create_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_exit_delphos)
        self.menuAbout.addAction(self.menu_about)
        self.menuAbout.addAction(self.menu_credits)
        self.menuDocumentation.addAction(self.menu_dock_visible)
        self.menuDocumentation.addAction(self.menu_dock_floating)
        self.menuView.addAction(self.menuDocumentation.menuAction())
        self.menuOptions.addAction(self.menu_open_full_doc)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Delphos", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStyleSheet(QtGui.QApplication.translate("MainWindow", ".QWidget {\n"
"   background-color: #E1EDF5;\n"
"}\n"
"\n"
"/*Non-main window popup widgets\n"
"QWidget {\n"
"     background-color: #f0f0f5;\n"
"}\n"
"*/\n"
"\n"
"\n"
"    \n"
"QWidget {\n"
"    font-family: arial;\n"
"    color: #333333;    \n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    padding-left: 6px;\n"
"    padding-right: 4px;\n"
"    background-color: #FFF7DB;\n"
"    border-width: 1px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"   background-color: #FFDF94;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QHeaderView::section:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 4px;\n"
"    background-color: #E6A84C;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: gainsboro;\n"
"    background-position: top right;\n"
"    background-repeat: no-repeat\n"
"}\n"
"\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: #FFF2C9;\n"
"    border-width: 1px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 2px;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #FFDF94;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 4px;\n"
"    background-color: #E6A84C;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: normal;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: #fafbfc;\n"
"    selection-color: #0a214c;\n"
"    selection-background-color: #FFF2C9;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: #5f66a1;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 2px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: #FFDF94;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"QToolTip {\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDocumentation.setTitle(QtGui.QApplication.translate("MainWindow", "&Documentation Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.dock_doc.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Documentation Window", None, QtGui.QApplication.UnicodeUTF8))
        self.toc_tree.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "Table of Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.doc_browser.setHtml(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:9pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_open_project.setText(QtGui.QApplication.translate("MainWindow", "&Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_open_project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_Delphos.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_credits.setText(QtGui.QApplication.translate("MainWindow", "&Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_credits.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelphos_Help.setText(QtGui.QApplication.translate("MainWindow", "Show Documentation Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_exit_delphos.setText(QtGui.QApplication.translate("MainWindow", "E&xit Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_exit_delphos.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_open_full_doc.setText(QtGui.QApplication.translate("MainWindow", "&View Documentation In Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_open_full_doc.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_create_project.setText(QtGui.QApplication.translate("MainWindow", "Create &New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_create_project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file.setText(QtGui.QApplication.translate("MainWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Project.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Delphos_2.setText(QtGui.QApplication.translate("MainWindow", "About Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_dock_visible.setText(QtGui.QApplication.translate("MainWindow", "&Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_dock_visible.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_dock_floating.setText(QtGui.QApplication.translate("MainWindow", "Docked", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_about.setText(QtGui.QApplication.translate("MainWindow", "&About Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_main_menu.setText(QtGui.QApplication.translate("MainWindow", "Main Menu", None, QtGui.QApplication.UnicodeUTF8))

from help_text_browser import HelpTextBrowser
import resources_rc
