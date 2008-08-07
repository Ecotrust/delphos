# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_project.ui'
#
# Created: Tue Jun 17 10:39:16 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_OpenProjectDialog(object):
    def setupUi(self, OpenProjectDialog):
        OpenProjectDialog.setObjectName("OpenProjectDialog")
        OpenProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        OpenProjectDialog.resize(458,139)
        font = QtGui.QFont()
        font.setFamily("arial")
        OpenProjectDialog.setFont(font)
        self.hboxlayout = QtGui.QHBoxLayout(OpenProjectDialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.groupBox_4 = QtGui.QGroupBox(OpenProjectDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.project_browse_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.project_browse_button.setFont(font)
        self.project_browse_button.setObjectName("project_browse_button")
        self.hboxlayout1.addWidget(self.project_browse_button)
        self.project_path_edit = QtGui.QLineEdit(self.groupBox_4)
        self.project_path_edit.setMinimumSize(QtCore.QSize(300,0))
        self.project_path_edit.setReadOnly(True)
        self.project_path_edit.setObjectName("project_path_edit")
        self.hboxlayout1.addWidget(self.project_path_edit)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem)
        self.open_button_box = QtGui.QDialogButtonBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.open_button_box.setFont(font)
        self.open_button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.open_button_box.setObjectName("open_button_box")
        self.hboxlayout2.addWidget(self.open_button_box)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.hboxlayout.addWidget(self.groupBox_4)

        self.retranslateUi(OpenProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(OpenProjectDialog)

    def retranslateUi(self, OpenProjectDialog):
        OpenProjectDialog.setWindowTitle(QtGui.QApplication.translate("OpenProjectDialog", "Open Existing Project", None, QtGui.QApplication.UnicodeUTF8))
        OpenProjectDialog.setStyleSheet(QtGui.QApplication.translate("OpenProjectDialog", ".QWidget {\n"
"background-color: #E1EDF5;\n"
"}\n"
"\n"
"/*Non-main window popup widgets\n"
"QWidget {\n"
"background-color: #f0f0f5;\n"
"}\n"
"*/\n"
"\n"
"\n"
"QWidget {\n"
"background-color: #f0f0f5;\n"
"font-family: arial;\n"
"color: #333333;    \n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"padding-left: 6px;\n"
"padding-right: 4px;\n"
"background-color: #FFF7DB;\n"
"border-width: 1px;\n"
"border-color: darkkhaki;\n"
"border-style: solid;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"background-color: #FFDF94;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"pressed. */\n"
"QHeaderView::section:pressed {\n"
"padding-left: 4px;\n"
"padding-top: 4px;\n"
"background-color: #E6A84C;\n"
"}\n"
"\n"
"QMainWindow {\n"
"background-color: gainsboro;\n"
"background-position: top right;\n"
"background-repeat: no-repeat\n"
"}\n"
"\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"background-color: #FFF2C9;\n"
"border-width: 1px;\n"
"border-color: darkkhaki;\n"
"border-style: solid;\n"
"border-radius: 5;\n"
"padding: 2px;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"min-width: 9ex;\n"
"min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #FFDF94;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"pressed. */\n"
"QPushButton:pressed {\n"
"padding-left: 4px;\n"
"padding-top: 4px;\n"
"background-color: #E6A84C;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"font: normal;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"border-width: 1;\n"
"border-color: darkkhaki;\n"
"border-style: solid;\n"
"border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"background-color: #fafbfc;\n"
"selection-color: #0a214c;\n"
"selection-background-color: #FFF2C9;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"we kill the padding and enlarge the border. This makes the items\n"
"glow. */\n"
"QLineEdit {\n"
"border-width: 1px;\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border-color: #5f66a1;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"border-width: 2px;\n"
"padding: 0px;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"background-color: #FFDF94;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"button-layout: 0;\n"
"}\n"
"\n"
"QToolTip {\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"opacity: 200;\n"
"}\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("OpenProjectDialog", "Select Project:", None, QtGui.QApplication.UnicodeUTF8))
        self.project_browse_button.setText(QtGui.QApplication.translate("OpenProjectDialog", "&Browse...", None, QtGui.QApplication.UnicodeUTF8))

