# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_mpa_type.ui'
#
# Created: Sat Jun 28 23:58:23 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectMpaTypeDialog(object):
    def setupUi(self, SelectMpaTypeDialog):
        SelectMpaTypeDialog.setObjectName("SelectMpaTypeDialog")
        SelectMpaTypeDialog.resize(199,105)
        SelectMpaTypeDialog.setStyleSheet(""".QWidget {
   background-color: #E1EDF5;
}

/*Non-main window popup widgets
QWidget {
     background-color: #f0f0f5;
}
*/


    
QWidget {
    font-family: arial;
    color: #333333;    
}


QHeaderView::section {
    padding-left: 2px;
    padding-right: 4px;
    background-color: #FFF7DB;
    border-width: 1px;
    border-color: darkkhaki;
    border-style: solid;
}

QHeaderView::section:hover {
   background-color: #FFDF94;
}

/* Increase the padding, so the text is shifted when the button is
   pressed. */
QHeaderView::section:pressed {
    padding-left: 4px;
    padding-top: 4px;
    background-color: #E6A84C;
}

QMainWindow {
    background-color: gainsboro;
    background-position: top right;
    background-repeat: no-repeat
}


/* Nice Windows-XP-style password character. */
QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}

/* We provide a min-width and min-height for push buttons
   so that they look elegant regardless of the width of the text. */
QPushButton {
    background-color: #FFF2C9;
    border-width: 1px;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 5;
    padding: 2px;
    padding-left: 4px;
    padding-right: 4px;
    min-width: 9ex;
    min-height: 2.5ex;
}

QPushButton:hover {
   background-color: #FFDF94;
}

/* Increase the padding, so the text is shifted when the button is
   pressed. */
QPushButton:pressed {
    padding-left: 4px;
    padding-top: 4px;
    background-color: #E6A84C;
}

QLabel, QAbstractButton {
    font: normal;
}

/* Mark mandatory fields with a brownish color. */
.mandatory {
    color: brown;
}

/* Bold text on status bar looks awful. */
QStatusBar QLabel {
   font: normal;
}

QStatusBar::item {
    border-width: 1;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 2;
}

QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {
    background-color: #fafbfc;
    selection-color: #0a214c;
    selection-background-color: #FFF2C9;
}

/* We reserve 1 pixel space in padding. When we get the focus,
   we kill the padding and enlarge the border. This makes the items
   glow. */
QLineEdit {
    border-width: 1px;
    padding: 1px;
    border-style: solid;
    border-color: #5f66a1;
    border-radius: 4px;
}

/* As mentioned above, eliminate the padding and increase the border. */
QLineEdit:focus, QFrame:focus {
    border-width: 2px;
    padding: 0px;
}

/* Nice to have the background color change when hovered. */
QRadioButton:hover, QCheckBox:hover {
    background-color: #FFDF94;
}

/* Force the dialog's buttons to follow the Windows guidelines. */
QDialogButtonBox {
    button-layout: 0;
}

QToolTip {
    padding: 5px;
    border-radius: 3px;
    opacity: 200;
}
""")
        self.hboxlayout = QtGui.QHBoxLayout(SelectMpaTypeDialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.groupBox = QtGui.QGroupBox(SelectMpaTypeDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.communities_type_button = QtGui.QPushButton(self.groupBox)
        self.communities_type_button.setMinimumSize(QtCore.QSize(95,20))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.communities_type_button.setFont(font)
        self.communities_type_button.setObjectName("communities_type_button")
        self.vboxlayout1.addWidget(self.communities_type_button)
        self.sites_type_button = QtGui.QPushButton(self.groupBox)
        self.sites_type_button.setMinimumSize(QtCore.QSize(95,20))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.sites_type_button.setFont(font)
        self.sites_type_button.setObjectName("sites_type_button")
        self.vboxlayout1.addWidget(self.sites_type_button)
        self.hboxlayout1.addLayout(self.vboxlayout1)
        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addWidget(self.groupBox)

        self.retranslateUi(SelectMpaTypeDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectMpaTypeDialog)

    def retranslateUi(self, SelectMpaTypeDialog):
        self.groupBox.setTitle(QtGui.QApplication.translate("SelectMpaTypeDialog", "Select Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.communities_type_button.setText(QtGui.QApplication.translate("SelectMpaTypeDialog", "Communities", None, QtGui.QApplication.UnicodeUTF8))
        self.sites_type_button.setText(QtGui.QApplication.translate("SelectMpaTypeDialog", "Sites", None, QtGui.QApplication.UnicodeUTF8))

