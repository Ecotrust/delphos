# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'language_dialog.ui'
#
# Created: Tue Jun 17 10:39:25 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LanguageDialog(object):
    def setupUi(self, LanguageDialog):
        LanguageDialog.setObjectName("LanguageDialog")
        LanguageDialog.resize(152,111)
        self.hboxlayout = QtGui.QHBoxLayout(LanguageDialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.groupBox = QtGui.QGroupBox(LanguageDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.english_button = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.english_button.setFont(font)
        self.english_button.setObjectName("english_button")
        self.vboxlayout.addWidget(self.english_button)
        self.spanish_button = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.spanish_button.setFont(font)
        self.spanish_button.setObjectName("spanish_button")
        self.vboxlayout.addWidget(self.spanish_button)
        self.hboxlayout.addWidget(self.groupBox)

        self.retranslateUi(LanguageDialog)
        QtCore.QMetaObject.connectSlotsByName(LanguageDialog)

    def retranslateUi(self, LanguageDialog):
        LanguageDialog.setWindowTitle(QtGui.QApplication.translate("LanguageDialog", "Language", None, QtGui.QApplication.UnicodeUTF8))
        LanguageDialog.setStyleSheet(QtGui.QApplication.translate("LanguageDialog", ".QWidget {\n"
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
        self.groupBox.setTitle(QtGui.QApplication.translate("LanguageDialog", "Select a Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.english_button.setText(QtGui.QApplication.translate("LanguageDialog", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.spanish_button.setText(QtGui.QApplication.translate("LanguageDialog", "Español", None, QtGui.QApplication.UnicodeUTF8))

