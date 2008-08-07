# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_criteria.ui'
#
# Created: Sat Jun 28 23:53:33 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddCriteriaDialog(object):
    def setupUi(self, AddCriteriaDialog):
        AddCriteriaDialog.setObjectName("AddCriteriaDialog")
        AddCriteriaDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddCriteriaDialog.resize(379,417)
        font = QtGui.QFont()
        font.setFamily("arial")
        AddCriteriaDialog.setFont(font)
        AddCriteriaDialog.setStyleSheet(""".QWidget {
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
        self.vboxlayout = QtGui.QVBoxLayout(AddCriteriaDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox_2 = QtGui.QGroupBox(AddCriteriaDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.criteria_description_edit = QtGui.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.criteria_description_edit.setFont(font)
        self.criteria_description_edit.setObjectName("criteria_description_edit")
        self.hboxlayout.addWidget(self.criteria_description_edit)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.groupBox = QtGui.QGroupBox(AddCriteriaDialog)
        self.groupBox.setObjectName("groupBox")
        self.hboxlayout2 = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.benefit_button = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.benefit_button.setFont(font)
        self.benefit_button.setObjectName("benefit_button")
        self.hboxlayout2.addWidget(self.benefit_button)
        self.cost_button = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.cost_button.setFont(font)
        self.cost_button.setObjectName("cost_button")
        self.hboxlayout2.addWidget(self.cost_button)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem)
        self.hboxlayout1.addWidget(self.groupBox)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.criteria_type_tab = QtGui.QTabWidget(AddCriteriaDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.criteria_type_tab.setFont(font)
        self.criteria_type_tab.setObjectName("criteria_type_tab")
        self.tab = QtGui.QWidget()
        self.tab.setGeometry(QtCore.QRect(0,0,355,240))
        self.tab.setObjectName("tab")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setSpacing(4)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.label_2 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.vboxlayout3.addWidget(self.label_2)
        self.binary_yes_edit = QtGui.QLineEdit(self.tab)
        self.binary_yes_edit.setMaximumSize(QtCore.QSize(200,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.binary_yes_edit.setFont(font)
        self.binary_yes_edit.setObjectName("binary_yes_edit")
        self.vboxlayout3.addWidget(self.binary_yes_edit)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setSpacing(4)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.label_3 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.vboxlayout4.addWidget(self.label_3)
        self.binary_no_edit = QtGui.QLineEdit(self.tab)
        self.binary_no_edit.setMaximumSize(QtCore.QSize(200,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.binary_no_edit.setFont(font)
        self.binary_no_edit.setObjectName("binary_no_edit")
        self.vboxlayout4.addWidget(self.binary_no_edit)
        self.vboxlayout2.addLayout(self.vboxlayout4)
        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem1)
        self.criteria_type_tab.addTab(self.tab,"")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setGeometry(QtCore.QRect(70,117,952,520))
        self.tab_3.setObjectName("tab_3")
        self.vboxlayout5 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout5.setObjectName("vboxlayout5")
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.add_ordinal_option_button = QtGui.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.add_ordinal_option_button.setFont(font)
        self.add_ordinal_option_button.setObjectName("add_ordinal_option_button")
        self.hboxlayout4.addWidget(self.add_ordinal_option_button)
        self.remove_ordinal_option_button = QtGui.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.remove_ordinal_option_button.setFont(font)
        self.remove_ordinal_option_button.setObjectName("remove_ordinal_option_button")
        self.hboxlayout4.addWidget(self.remove_ordinal_option_button)
        self.hboxlayout3.addLayout(self.hboxlayout4)
        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)
        self.vboxlayout5.addLayout(self.hboxlayout3)
        self.ordinal_option_table = OrdinalOptionTableWidget(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.ordinal_option_table.setFont(font)
        self.ordinal_option_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ordinal_option_table.setDragDropOverwriteMode(False)
        self.ordinal_option_table.setAlternatingRowColors(False)
        self.ordinal_option_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ordinal_option_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ordinal_option_table.setObjectName("ordinal_option_table")
        self.vboxlayout5.addWidget(self.ordinal_option_table)
        self.criteria_type_tab.addTab(self.tab_3,"")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setGeometry(QtCore.QRect(92,146,952,520))
        self.tab_2.setObjectName("tab_2")
        self.vboxlayout6 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setSpacing(3)
        self.vboxlayout7.setObjectName("vboxlayout7")
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215,26))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.vboxlayout7.addWidget(self.label_5)
        self.ratio_description_edit = QtGui.QLineEdit(self.tab_2)
        self.ratio_description_edit.setMaximumSize(QtCore.QSize(200,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.ratio_description_edit.setFont(font)
        self.ratio_description_edit.setObjectName("ratio_description_edit")
        self.vboxlayout7.addWidget(self.ratio_description_edit)
        self.vboxlayout6.addLayout(self.vboxlayout7)
        spacerItem3 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout6.addItem(spacerItem3)
        self.criteria_type_tab.addTab(self.tab_2,"")
        self.vboxlayout.addWidget(self.criteria_type_tab)
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")
        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem4)
        self.help_define_criteria = HelpButton(AddCriteriaDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_define_criteria.setIcon(icon)
        self.help_define_criteria.setIconSize(QtCore.QSize(24,24))
        self.help_define_criteria.setFlat(True)
        self.help_define_criteria.setObjectName("help_define_criteria")
        self.hboxlayout5.addWidget(self.help_define_criteria)
        self.add_criteria_box = QtGui.QDialogButtonBox(AddCriteriaDialog)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.add_criteria_box.setFont(font)
        self.add_criteria_box.setOrientation(QtCore.Qt.Horizontal)
        self.add_criteria_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.add_criteria_box.setObjectName("add_criteria_box")
        self.hboxlayout5.addWidget(self.add_criteria_box)
        self.vboxlayout.addLayout(self.hboxlayout5)

        self.retranslateUi(AddCriteriaDialog)
        self.criteria_type_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddCriteriaDialog)

    def retranslateUi(self, AddCriteriaDialog):
        AddCriteriaDialog.setWindowTitle(QtGui.QApplication.translate("AddCriteriaDialog", "Add Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Criteria description:", None, QtGui.QApplication.UnicodeUTF8))
        self.benefit_button.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.cost_button.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Cost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Option 1: (example: \'yes\', \'true\')", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Option 2: (example: \'no\', \'false\')", None, QtGui.QApplication.UnicodeUTF8))
        self.criteria_type_tab.setTabText(self.criteria_type_tab.indexOf(self.tab), QtGui.QApplication.translate("AddCriteriaDialog", "Binary", None, QtGui.QApplication.UnicodeUTF8))
        self.add_ordinal_option_button.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Add Option", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_ordinal_option_button.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Remove Option", None, QtGui.QApplication.UnicodeUTF8))
        self.ordinal_option_table.clear()
        self.ordinal_option_table.setColumnCount(4)
        self.ordinal_option_table.setRowCount(1)
        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("AddCriteriaDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ordinal_option_table.setVerticalHeaderItem(0,headerItem)
        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.ordinal_option_table.setHorizontalHeaderItem(0,headerItem1)
        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Rank", None, QtGui.QApplication.UnicodeUTF8))
        self.ordinal_option_table.setHorizontalHeaderItem(1,headerItem2)
        headerItem3 = QtGui.QTableWidgetItem()
        self.ordinal_option_table.setHorizontalHeaderItem(2,headerItem3)
        headerItem4 = QtGui.QTableWidgetItem()
        self.ordinal_option_table.setHorizontalHeaderItem(3,headerItem4)
        self.criteria_type_tab.setTabText(self.criteria_type_tab.indexOf(self.tab_3), QtGui.QApplication.translate("AddCriteriaDialog", "Ordinal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddCriteriaDialog", "Description of quantitative value (units):", None, QtGui.QApplication.UnicodeUTF8))
        self.criteria_type_tab.setTabText(self.criteria_type_tab.indexOf(self.tab_2), QtGui.QApplication.translate("AddCriteriaDialog", "Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.help_define_criteria.setAccessibleDescription(QtGui.QApplication.translate("AddCriteriaDialog", "help_definir_los_criterios", None, QtGui.QApplication.UnicodeUTF8))

from HelpButton import HelpButton
from OrdinalOptionTableWidget import OrdinalOptionTableWidget
