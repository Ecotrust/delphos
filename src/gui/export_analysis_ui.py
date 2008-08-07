# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_analysis.ui'
#
# Created: Sat Jun 28 23:53:37 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ExportAnalysisDialog(object):
    def setupUi(self, ExportAnalysisDialog):
        ExportAnalysisDialog.setObjectName("ExportAnalysisDialog")
        ExportAnalysisDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ExportAnalysisDialog.resize(339,285)
        font = QtGui.QFont()
        font.setFamily("arial")
        ExportAnalysisDialog.setFont(font)
        ExportAnalysisDialog.setStyleSheet(""".QWidget {
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
        self.vboxlayout = QtGui.QVBoxLayout(ExportAnalysisDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox_4 = QtGui.QGroupBox(ExportAnalysisDialog)
        self.groupBox_4.setWindowModality(QtCore.Qt.NonModal)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.browse_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.hboxlayout.addWidget(self.browse_button)
        self.path_edit = QtGui.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.path_edit.setFont(font)
        self.path_edit.setReadOnly(True)
        self.path_edit.setObjectName("path_edit")
        self.hboxlayout.addWidget(self.path_edit)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
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
        self.vboxlayout.addWidget(self.groupBox_4)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem = QtGui.QSpacerItem(246,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.button_box = QtGui.QDialogButtonBox(ExportAnalysisDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.button_box.setFont(font)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.hboxlayout1.addWidget(self.button_box)
        self.vboxlayout.addLayout(self.hboxlayout1)
        spacerItem1 = QtGui.QSpacerItem(311,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)

        self.retranslateUi(ExportAnalysisDialog)
        QtCore.QMetaObject.connectSlotsByName(ExportAnalysisDialog)

    def retranslateUi(self, ExportAnalysisDialog):
        ExportAnalysisDialog.setWindowTitle(QtGui.QApplication.translate("ExportAnalysisDialog", "Export As CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ExportAnalysisDialog", "Save As:", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_button.setText(QtGui.QApplication.translate("ExportAnalysisDialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExportAnalysisDialog", "* Note, this will export a comma-separated-value (CSV) file in the \'utf-8\' encoding.  This encoding allows for non-latin characters such as (ñ, ä, 字, etc.).  When opening the file in OpenOffice Calc, Notepad, etc. be sure to specify the \'utf-8\' encoding.  If you use MS Excel you will need to open the CSV as a text file by clicking File->Open->Files of type: Text Files.  Specify the \'utf-8\' encoding and \'comma\' delimiter when asked.", None, QtGui.QApplication.UnicodeUTF8))

