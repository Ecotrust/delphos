# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_project.ui'
#
# Created: Tue Jun 17 10:39:15 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CreateProjectDialog(object):
    def setupUi(self, CreateProjectDialog):
        CreateProjectDialog.setObjectName("CreateProjectDialog")
        CreateProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CreateProjectDialog.resize(438,262)
        font = QtGui.QFont()
        font.setFamily("arial")
        CreateProjectDialog.setFont(font)
        self.hboxlayout = QtGui.QHBoxLayout(CreateProjectDialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.groupBox_2 = QtGui.QGroupBox(CreateProjectDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.fisheries_type_button = QtGui.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.fisheries_type_button.setFont(font)
        self.fisheries_type_button.setObjectName("fisheries_type_button")
        self.vboxlayout2.addWidget(self.fisheries_type_button)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setSpacing(0)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.mpa_type_button = QtGui.QRadioButton(self.groupBox_2)
        self.mpa_type_button.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.mpa_type_button.setFont(font)
        self.mpa_type_button.setCheckable(True)
        self.mpa_type_button.setObjectName("mpa_type_button")
        self.vboxlayout3.addWidget(self.mpa_type_button)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        spacerItem = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem)
        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setSpacing(0)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.communities_sub_type_button = QtGui.QRadioButton(self.groupBox_2)
        self.communities_sub_type_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.communities_sub_type_button.setFont(font)
        self.communities_sub_type_button.setCheckable(True)
        self.communities_sub_type_button.setObjectName("communities_sub_type_button")
        self.vboxlayout4.addWidget(self.communities_sub_type_button)
        self.sites_sub_type_button = QtGui.QRadioButton(self.groupBox_2)
        self.sites_sub_type_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.sites_sub_type_button.setFont(font)
        self.sites_sub_type_button.setCheckable(True)
        self.sites_sub_type_button.setObjectName("sites_sub_type_button")
        self.vboxlayout4.addWidget(self.sites_sub_type_button)
        self.hboxlayout3.addLayout(self.vboxlayout4)
        self.hboxlayout2.addLayout(self.hboxlayout3)
        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)
        self.vboxlayout3.addLayout(self.hboxlayout2)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.vboxlayout1.addLayout(self.vboxlayout2)
        self.hboxlayout1.addWidget(self.groupBox_2)
        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName("vboxlayout5")
        self.groupBox_3 = QtGui.QGroupBox(CreateProjectDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.vboxlayout6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.default_crit_check = QtGui.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.default_crit_check.setFont(font)
        self.default_crit_check.setChecked(True)
        self.default_crit_check.setObjectName("default_crit_check")
        self.vboxlayout6.addWidget(self.default_crit_check)
        self.default_altern_check = QtGui.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.default_altern_check.setFont(font)
        self.default_altern_check.setChecked(False)
        self.default_altern_check.setObjectName("default_altern_check")
        self.vboxlayout6.addWidget(self.default_altern_check)
        spacerItem2 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout6.addItem(spacerItem2)
        self.vboxlayout5.addWidget(self.groupBox_3)
        self.hboxlayout1.addLayout(self.vboxlayout5)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.groupBox_4 = QtGui.QGroupBox(CreateProjectDialog)
        self.groupBox_4.setWindowModality(QtCore.Qt.NonModal)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.hboxlayout4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.project_browse_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.project_browse_button.setFont(font)
        self.project_browse_button.setObjectName("project_browse_button")
        self.hboxlayout4.addWidget(self.project_browse_button)
        self.project_path_edit = QtGui.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.project_path_edit.setFont(font)
        self.project_path_edit.setReadOnly(True)
        self.project_path_edit.setObjectName("project_path_edit")
        self.hboxlayout4.addWidget(self.project_path_edit)
        self.vboxlayout.addWidget(self.groupBox_4)
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")
        spacerItem3 = QtGui.QSpacerItem(246,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem3)
        self.create_button_box = QtGui.QDialogButtonBox(CreateProjectDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.create_button_box.setFont(font)
        self.create_button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.create_button_box.setObjectName("create_button_box")
        self.hboxlayout5.addWidget(self.create_button_box)
        self.vboxlayout.addLayout(self.hboxlayout5)
        spacerItem4 = QtGui.QSpacerItem(412,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem4)
        self.hboxlayout.addLayout(self.vboxlayout)
        spacerItem5 = QtGui.QSpacerItem(40,230,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem5)

        self.retranslateUi(CreateProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateProjectDialog)

    def retranslateUi(self, CreateProjectDialog):
        CreateProjectDialog.setWindowTitle(QtGui.QApplication.translate("CreateProjectDialog", "Create New Project", None, QtGui.QApplication.UnicodeUTF8))
        CreateProjectDialog.setStyleSheet(QtGui.QApplication.translate("CreateProjectDialog", ".QWidget {\n"
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
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CreateProjectDialog", "Select Project Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.fisheries_type_button.setText(QtGui.QApplication.translate("CreateProjectDialog", "Fisheries", None, QtGui.QApplication.UnicodeUTF8))
        self.mpa_type_button.setText(QtGui.QApplication.translate("CreateProjectDialog", "Marine Reserves", None, QtGui.QApplication.UnicodeUTF8))
        self.communities_sub_type_button.setText(QtGui.QApplication.translate("CreateProjectDialog", "Communities", None, QtGui.QApplication.UnicodeUTF8))
        self.sites_sub_type_button.setText(QtGui.QApplication.translate("CreateProjectDialog", "Sites", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("CreateProjectDialog", "Project Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.default_crit_check.setText(QtGui.QApplication.translate("CreateProjectDialog", "Load Suggested Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.default_altern_check.setText(QtGui.QApplication.translate("CreateProjectDialog", "Load Sample Alternatives", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("CreateProjectDialog", "Save Project As:", None, QtGui.QApplication.UnicodeUTF8))
        self.project_browse_button.setText(QtGui.QApplication.translate("CreateProjectDialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))

