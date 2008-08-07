# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_alternative.ui'
#
# Created: Sun Jun 29 00:16:39 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddAlternDialog(object):
    def setupUi(self, AddAlternDialog):
        AddAlternDialog.setObjectName("AddAlternDialog")
        AddAlternDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddAlternDialog.resize(307,213)
        font = QtGui.QFont()
        font.setFamily("arial")
        AddAlternDialog.setFont(font)
        AddAlternDialog.setStyleSheet(""".QWidget {
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout(AddAlternDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtGui.QGroupBox(AddAlternDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.name_label = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.vboxlayout.addWidget(self.name_label)
        self.color_label = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.color_label.setFont(font)
        self.color_label.setObjectName("color_label")
        self.vboxlayout.addWidget(self.color_label)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.alternative_name_edit = QtGui.QLineEdit(self.groupBox_4)
        self.alternative_name_edit.setMinimumSize(QtCore.QSize(200,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.alternative_name_edit.setFont(font)
        self.alternative_name_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.alternative_name_edit.setReadOnly(False)
        self.alternative_name_edit.setObjectName("alternative_name_edit")
        self.vboxlayout1.addWidget(self.alternative_name_edit)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.new_color_label = QtGui.QLabel(self.groupBox_4)
        self.new_color_label.setMinimumSize(QtCore.QSize(80,20))
        self.new_color_label.setMaximumSize(QtCore.QSize(80,20))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.new_color_label.setFont(font)
        self.new_color_label.setObjectName("new_color_label")
        self.hboxlayout1.addWidget(self.new_color_label)
        self.change_color_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.change_color_button.setFont(font)
        self.change_color_button.setObjectName("change_color_button")
        self.hboxlayout1.addWidget(self.change_color_button)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout1)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(58,71,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.help_define_alternatives = HelpButton(self.groupBox_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_define_alternatives.setIcon(icon)
        self.help_define_alternatives.setIconSize(QtCore.QSize(24,24))
        self.help_define_alternatives.setFlat(True)
        self.help_define_alternatives.setObjectName("help_define_alternatives")
        self.horizontalLayout.addWidget(self.help_define_alternatives)
        self.add_alternative_box = QtGui.QDialogButtonBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.add_alternative_box.setFont(font)
        self.add_alternative_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.add_alternative_box.setObjectName("add_alternative_box")
        self.horizontalLayout.addWidget(self.add_alternative_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.retranslateUi(AddAlternDialog)
        QtCore.QMetaObject.connectSlotsByName(AddAlternDialog)

    def retranslateUi(self, AddAlternDialog):
        AddAlternDialog.setWindowTitle(QtGui.QApplication.translate("AddAlternDialog", "Add Alternative", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("AddAlternDialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.color_label.setText(QtGui.QApplication.translate("AddAlternDialog", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.change_color_button.setText(QtGui.QApplication.translate("AddAlternDialog", "New Color", None, QtGui.QApplication.UnicodeUTF8))
        self.help_define_alternatives.setAccessibleDescription(QtGui.QApplication.translate("AddAlternDialog", "help_definir_las_alternativas", None, QtGui.QApplication.UnicodeUTF8))

from HelpButton import HelpButton
import resources_rc
