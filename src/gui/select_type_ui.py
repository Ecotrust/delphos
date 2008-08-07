# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_type.ui'
#
# Created: Tue Jun 17 10:39:13 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectTypeDialog(object):
    def setupUi(self, SelectTypeDialog):
        SelectTypeDialog.setObjectName("SelectTypeDialog")
        SelectTypeDialog.resize(415,271)
        self.hboxlayout = QtGui.QHBoxLayout(SelectTypeDialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtGui.QGroupBox(SelectTypeDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(220,160))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.label_3 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.vboxlayout1.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(16777215,1677777))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.vboxlayout.addWidget(self.groupBox)
        self.hboxlayout.addLayout(self.vboxlayout)
        spacerItem1 = QtGui.QSpacerItem(16,16,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.groupBox_4 = QtGui.QGroupBox(SelectTypeDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.open_project_button = QtGui.QPushButton(self.groupBox_4)
        self.open_project_button.setMinimumSize(QtCore.QSize(80,0))
        self.open_project_button.setMaximumSize(QtCore.QSize(140,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.open_project_button.setFont(font)
        self.open_project_button.setObjectName("open_project_button")
        self.vboxlayout3.addWidget(self.open_project_button)
        self.create_project_button = QtGui.QPushButton(self.groupBox_4)
        self.create_project_button.setEnabled(True)
        self.create_project_button.setMaximumSize(QtCore.QSize(140,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.create_project_button.setFont(font)
        self.create_project_button.setObjectName("create_project_button")
        self.vboxlayout3.addWidget(self.create_project_button)
        self.vboxlayout2.addWidget(self.groupBox_4)
        spacerItem2 = QtGui.QSpacerItem(140,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem2)
        self.groupBox_3 = QtGui.QGroupBox(SelectTypeDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.groupBox_3)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setSpacing(2)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.fisheries_type_button = QtGui.QPushButton(self.groupBox_3)
        self.fisheries_type_button.setMaximumSize(QtCore.QSize(140,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.fisheries_type_button.setFont(font)
        self.fisheries_type_button.setObjectName("fisheries_type_button")
        self.vboxlayout4.addWidget(self.fisheries_type_button)
        self.mpa_type_button = QtGui.QPushButton(self.groupBox_3)
        self.mpa_type_button.setEnabled(True)
        self.mpa_type_button.setMaximumSize(QtCore.QSize(140,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.mpa_type_button.setFont(font)
        self.mpa_type_button.setObjectName("mpa_type_button")
        self.vboxlayout4.addWidget(self.mpa_type_button)
        self.hboxlayout1.addLayout(self.vboxlayout4)
        self.vboxlayout2.addWidget(self.groupBox_3)
        spacerItem3 = QtGui.QSpacerItem(140,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem3)
        self.groupBox_2 = QtGui.QGroupBox(SelectTypeDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.hboxlayout2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.main_close_button = QtGui.QPushButton(self.groupBox_2)
        self.main_close_button.setEnabled(True)
        self.main_close_button.setMaximumSize(QtCore.QSize(140,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.main_close_button.setFont(font)
        self.main_close_button.setObjectName("main_close_button")
        self.hboxlayout2.addWidget(self.main_close_button)
        self.vboxlayout2.addWidget(self.groupBox_2)
        spacerItem4 = QtGui.QSpacerItem(140,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem4)
        self.hboxlayout.addLayout(self.vboxlayout2)

        self.retranslateUi(SelectTypeDialog)
        QtCore.QObject.connect(self.main_close_button,QtCore.SIGNAL("clicked()"),SelectTypeDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(SelectTypeDialog)

    def retranslateUi(self, SelectTypeDialog):
        SelectTypeDialog.setStyleSheet(QtGui.QApplication.translate("SelectTypeDialog", ".QWidget {\n"
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
"     background-color: #f0f0f5;\n"
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
        self.label_3.setStyleSheet(QtGui.QApplication.translate("SelectTypeDialog", "font-size: 16px;\n"
"font-weight: bold;", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SelectTypeDialog", "Welcome To Delphos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SelectTypeDialog", "A decision-making tool for community-based marine conservation. Developed by Comunidad y Biodiversidad (COBI), World Wildlife Fund (WWF) and Ecotrust.  Released free and open source under the GPL2 license", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("SelectTypeDialog", "Get Started", None, QtGui.QApplication.UnicodeUTF8))
        self.open_project_button.setToolTip(QtGui.QApplication.translate("SelectTypeDialog", "For selecting suitable candidates for MSC certification", None, QtGui.QApplication.UnicodeUTF8))
        self.open_project_button.setWhatsThis(QtGui.QApplication.translate("SelectTypeDialog", "Open an existing project file", None, QtGui.QApplication.UnicodeUTF8))
        self.open_project_button.setText(QtGui.QApplication.translate("SelectTypeDialog", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.create_project_button.setToolTip(QtGui.QApplication.translate("SelectTypeDialog", "For selecting suitable regions as Marine Protected Areas", None, QtGui.QApplication.UnicodeUTF8))
        self.create_project_button.setWhatsThis(QtGui.QApplication.translate("SelectTypeDialog", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.create_project_button.setText(QtGui.QApplication.translate("SelectTypeDialog", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SelectTypeDialog", "View Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.fisheries_type_button.setToolTip(QtGui.QApplication.translate("SelectTypeDialog", "For selecting suitable candidates for MSC certification", None, QtGui.QApplication.UnicodeUTF8))
        self.fisheries_type_button.setWhatsThis(QtGui.QApplication.translate("SelectTypeDialog", "For selecting suitable candidates for MSC certification", None, QtGui.QApplication.UnicodeUTF8))
        self.fisheries_type_button.setText(QtGui.QApplication.translate("SelectTypeDialog", "Fisheries", None, QtGui.QApplication.UnicodeUTF8))
        self.mpa_type_button.setToolTip(QtGui.QApplication.translate("SelectTypeDialog", "For selecting suitable regions as Marine Protected Areas", None, QtGui.QApplication.UnicodeUTF8))
        self.mpa_type_button.setText(QtGui.QApplication.translate("SelectTypeDialog", "Marine Reserves", None, QtGui.QApplication.UnicodeUTF8))
        self.main_close_button.setToolTip(QtGui.QApplication.translate("SelectTypeDialog", "For selecting suitable regions as Marine Protected Areas", None, QtGui.QApplication.UnicodeUTF8))
        self.main_close_button.setText(QtGui.QApplication.translate("SelectTypeDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

