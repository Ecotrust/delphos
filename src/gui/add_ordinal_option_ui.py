# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_ordinal_option.ui'
#
# Created: Sat Jun 28 23:53:34 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddOrdinalOptionDialog(object):
    def setupUi(self, AddOrdinalOptionDialog):
        AddOrdinalOptionDialog.setObjectName("AddOrdinalOptionDialog")
        AddOrdinalOptionDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddOrdinalOptionDialog.resize(277,172)
        font = QtGui.QFont()
        font.setFamily("arial")
        AddOrdinalOptionDialog.setFont(font)
        AddOrdinalOptionDialog.setStyleSheet(""".QWidget {
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
        self.vboxlayout = QtGui.QVBoxLayout(AddOrdinalOptionDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox_4 = QtGui.QGroupBox(AddOrdinalOptionDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setSpacing(0)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.vboxlayout2.addWidget(self.label_4)
        self.option_description_edit = QtGui.QLineEdit(self.groupBox_4)
        self.option_description_edit.setMinimumSize(QtCore.QSize(200,0))
        self.option_description_edit.setMaximumSize(QtCore.QSize(200,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.option_description_edit.setFont(font)
        self.option_description_edit.setObjectName("option_description_edit")
        self.vboxlayout2.addWidget(self.option_description_edit)
        self.vboxlayout1.addLayout(self.vboxlayout2)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setSpacing(0)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.vboxlayout3.addWidget(self.label_6)
        self.option_value_edit = QtGui.QLineEdit(self.groupBox_4)
        self.option_value_edit.setMinimumSize(QtCore.QSize(100,0))
        self.option_value_edit.setMaximumSize(QtCore.QSize(100,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.option_value_edit.setFont(font)
        self.option_value_edit.setObjectName("option_value_edit")
        self.vboxlayout3.addWidget(self.option_value_edit)
        self.vboxlayout1.addLayout(self.vboxlayout3)
        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setObjectName("vboxlayout4")
        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout4.addItem(spacerItem)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem1 = QtGui.QSpacerItem(81,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.add_ordinal_option_box = QtGui.QDialogButtonBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.add_ordinal_option_box.setFont(font)
        self.add_ordinal_option_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.add_ordinal_option_box.setObjectName("add_ordinal_option_box")
        self.hboxlayout.addWidget(self.add_ordinal_option_box)
        self.vboxlayout4.addLayout(self.hboxlayout)
        self.vboxlayout1.addLayout(self.vboxlayout4)
        self.vboxlayout.addWidget(self.groupBox_4)

        self.retranslateUi(AddOrdinalOptionDialog)
        QtCore.QObject.connect(self.add_ordinal_option_box,QtCore.SIGNAL("rejected()"),AddOrdinalOptionDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(AddOrdinalOptionDialog)

    def retranslateUi(self, AddOrdinalOptionDialog):
        AddOrdinalOptionDialog.setWindowTitle(QtGui.QApplication.translate("AddOrdinalOptionDialog", "Add Ordinal Option", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddOrdinalOptionDialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddOrdinalOptionDialog", "Rank:", None, QtGui.QApplication.UnicodeUTF8))

