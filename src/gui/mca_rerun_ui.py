# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mca_rerun.ui'
#
# Created: Sat Jun 28 23:53:37 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_McaRerunDialog(object):
    def setupUi(self, McaRerunDialog):
        McaRerunDialog.setObjectName("McaRerunDialog")
        McaRerunDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        McaRerunDialog.resize(296,151)
        McaRerunDialog.setStyleSheet(""".QWidget {
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
        self.vboxlayout = QtGui.QVBoxLayout(McaRerunDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox_4 = QtGui.QGroupBox(McaRerunDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setSpacing(2)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.vboxlayout2.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.vboxlayout2.addWidget(self.label_9)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setSpacing(2)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.analysis_name_edit = QtGui.QLineEdit(self.groupBox_4)
        self.analysis_name_edit.setMinimumSize(QtCore.QSize(150,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.analysis_name_edit.setFont(font)
        self.analysis_name_edit.setObjectName("analysis_name_edit")
        self.vboxlayout3.addWidget(self.analysis_name_edit)
        self.analysis_description_edit = QtGui.QLineEdit(self.groupBox_4)
        self.analysis_description_edit.setMinimumSize(QtCore.QSize(150,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.analysis_description_edit.setFont(font)
        self.analysis_description_edit.setObjectName("analysis_description_edit")
        self.vboxlayout3.addWidget(self.analysis_description_edit)
        self.hboxlayout.addLayout(self.vboxlayout3)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.restart_analysis_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.restart_analysis_button.setFont(font)
        self.restart_analysis_button.setObjectName("restart_analysis_button")
        self.hboxlayout1.addWidget(self.restart_analysis_button)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addWidget(self.groupBox_4)

        self.retranslateUi(McaRerunDialog)
        QtCore.QMetaObject.connectSlotsByName(McaRerunDialog)

    def retranslateUi(self, McaRerunDialog):
        McaRerunDialog.setWindowTitle(QtGui.QApplication.translate("McaRerunDialog", "Rerun Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("McaRerunDialog", "Please enter new information:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("McaRerunDialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("McaRerunDialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.restart_analysis_button.setText(QtGui.QApplication.translate("McaRerunDialog", "Restart Analysis", None, QtGui.QApplication.UnicodeUTF8))

