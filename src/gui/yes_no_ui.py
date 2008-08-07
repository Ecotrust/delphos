# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yes_no.ui'
#
# Created: Sat Jun 28 23:53:36 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_YesNoDialog(object):
    def setupUi(self, YesNoDialog):
        YesNoDialog.setObjectName("YesNoDialog")
        YesNoDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        YesNoDialog.resize(213,82)
        YesNoDialog.setStyleSheet(""".QWidget {
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
        self.vboxlayout = QtGui.QVBoxLayout(YesNoDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.message_label = QtGui.QLabel(YesNoDialog)
        self.message_label.setWindowModality(QtCore.Qt.NonModal)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.message_label.setFont(font)
        self.message_label.setObjectName("message_label")
        self.vboxlayout.addWidget(self.message_label)
        self.confirm_box = QtGui.QDialogButtonBox(YesNoDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.confirm_box.setFont(font)
        self.confirm_box.setOrientation(QtCore.Qt.Horizontal)
        self.confirm_box.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.confirm_box.setCenterButtons(False)
        self.confirm_box.setObjectName("confirm_box")
        self.vboxlayout.addWidget(self.confirm_box)

        self.retranslateUi(YesNoDialog)
        QtCore.QMetaObject.connectSlotsByName(YesNoDialog)

    def retranslateUi(self, YesNoDialog):
        YesNoDialog.setWindowTitle(QtGui.QApplication.translate("YesNoDialog", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.message_label.setText(QtGui.QApplication.translate("YesNoDialog", "Are you sure?", None, QtGui.QApplication.UnicodeUTF8))

