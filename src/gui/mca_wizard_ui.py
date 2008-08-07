# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mca_wizard.ui'
#
# Created: Sat Jun 28 23:53:35 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_McaWizard(object):
    def setupUi(self, McaWizard):
        McaWizard.setObjectName("McaWizard")
        McaWizard.setWindowModality(QtCore.Qt.ApplicationModal)
        McaWizard.resize(765,580)
        font = QtGui.QFont()
        font.setFamily("arial")
        McaWizard.setFont(font)
        McaWizard.setStyleSheet(""".QWidget {
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
        self.vboxlayout = QtGui.QVBoxLayout(McaWizard)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.mca_stack = QtGui.QStackedWidget(McaWizard)
        self.mca_stack.setObjectName("mca_stack")
        self.select_altern_page = QtGui.QWidget()
        self.select_altern_page.setGeometry(QtCore.QRect(0,0,747,562))
        self.select_altern_page.setObjectName("select_altern_page")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.select_altern_page)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.label_13 = QtGui.QLabel(self.select_altern_page)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.hboxlayout.addWidget(self.label_13)
        self.help_select_alternatives = HelpButton(self.select_altern_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_select_alternatives.setIcon(icon)
        self.help_select_alternatives.setIconSize(QtCore.QSize(24,24))
        self.help_select_alternatives.setFlat(True)
        self.help_select_alternatives.setObjectName("help_select_alternatives")
        self.hboxlayout.addWidget(self.help_select_alternatives)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.check_all_altern_button = QtGui.QPushButton(self.select_altern_page)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.check_all_altern_button.setFont(font)
        self.check_all_altern_button.setObjectName("check_all_altern_button")
        self.hboxlayout1.addWidget(self.check_all_altern_button)
        self.uncheck_all_altern_button = QtGui.QPushButton(self.select_altern_page)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.uncheck_all_altern_button.setFont(font)
        self.uncheck_all_altern_button.setObjectName("uncheck_all_altern_button")
        self.hboxlayout1.addWidget(self.uncheck_all_altern_button)
        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.altern_table = AlternativeMcaTableWidget(self.select_altern_page)
        self.altern_table.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.altern_table.setFont(font)
        self.altern_table.setMouseTracking(False)
        self.altern_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.altern_table.setAlternatingRowColors(True)
        self.altern_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.altern_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.altern_table.setObjectName("altern_table")
        self.hboxlayout2.addWidget(self.altern_table)
        spacerItem2 = QtGui.QSpacerItem(111,245,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        spacerItem3 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem3)
        self.groupBox_8 = QtGui.QGroupBox(self.select_altern_page)
        self.groupBox_8.setObjectName("groupBox_8")
        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_8)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.altern_next_button = QtGui.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.altern_next_button.setFont(font)
        self.altern_next_button.setObjectName("altern_next_button")
        self.vboxlayout3.addWidget(self.altern_next_button)
        self.altern_cancel_button = QtGui.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.altern_cancel_button.setFont(font)
        self.altern_cancel_button.setObjectName("altern_cancel_button")
        self.vboxlayout3.addWidget(self.altern_cancel_button)
        self.vboxlayout2.addWidget(self.groupBox_8)
        self.hboxlayout2.addLayout(self.vboxlayout2)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.mca_stack.addWidget(self.select_altern_page)
        self.select_criteria_page = QtGui.QWidget()
        self.select_criteria_page.setGeometry(QtCore.QRect(0,0,100,30))
        self.select_criteria_page.setObjectName("select_criteria_page")
        self.vboxlayout4 = QtGui.QVBoxLayout(self.select_criteria_page)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.label_14 = QtGui.QLabel(self.select_criteria_page)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.hboxlayout3.addWidget(self.label_14)
        self.help_select_criteria = HelpButton(self.select_criteria_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_select_criteria.setIcon(icon)
        self.help_select_criteria.setIconSize(QtCore.QSize(24,24))
        self.help_select_criteria.setFlat(True)
        self.help_select_criteria.setObjectName("help_select_criteria")
        self.hboxlayout3.addWidget(self.help_select_criteria)
        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem4)
        self.vboxlayout4.addLayout(self.hboxlayout3)
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.check_all_criteria_button = QtGui.QPushButton(self.select_criteria_page)
        self.check_all_criteria_button.setObjectName("check_all_criteria_button")
        self.hboxlayout4.addWidget(self.check_all_criteria_button)
        self.uncheck_all_criteria_button = QtGui.QPushButton(self.select_criteria_page)
        self.uncheck_all_criteria_button.setObjectName("uncheck_all_criteria_button")
        self.hboxlayout4.addWidget(self.uncheck_all_criteria_button)
        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem5)
        self.vboxlayout4.addLayout(self.hboxlayout4)
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.crit_table = CriteriaMcaTableWidget(self.select_criteria_page)
        self.crit_table.setEnabled(True)
        self.crit_table.setMouseTracking(False)
        self.crit_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.crit_table.setAlternatingRowColors(True)
        self.crit_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.crit_table.setObjectName("crit_table")
        self.hboxlayout5.addWidget(self.crit_table)
        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName("vboxlayout5")
        spacerItem6 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout5.addItem(spacerItem6)
        self.groupBox_9 = QtGui.QGroupBox(self.select_criteria_page)
        self.groupBox_9.setObjectName("groupBox_9")
        self.vboxlayout6 = QtGui.QVBoxLayout(self.groupBox_9)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.crit_next_button = QtGui.QPushButton(self.groupBox_9)
        self.crit_next_button.setObjectName("crit_next_button")
        self.vboxlayout6.addWidget(self.crit_next_button)
        self.crit_prev_button = QtGui.QPushButton(self.groupBox_9)
        self.crit_prev_button.setObjectName("crit_prev_button")
        self.vboxlayout6.addWidget(self.crit_prev_button)
        self.crit_cancel_button = QtGui.QPushButton(self.groupBox_9)
        self.crit_cancel_button.setObjectName("crit_cancel_button")
        self.vboxlayout6.addWidget(self.crit_cancel_button)
        self.vboxlayout5.addWidget(self.groupBox_9)
        self.hboxlayout5.addLayout(self.vboxlayout5)
        self.vboxlayout4.addLayout(self.hboxlayout5)
        self.mca_stack.addWidget(self.select_criteria_page)
        self.input_data_page = QtGui.QWidget()
        self.input_data_page.setGeometry(QtCore.QRect(0,0,100,30))
        self.input_data_page.setObjectName("input_data_page")
        self.vboxlayout7 = QtGui.QVBoxLayout(self.input_data_page)
        self.vboxlayout7.setObjectName("vboxlayout7")
        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")
        self.label_15 = QtGui.QLabel(self.input_data_page)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.hboxlayout6.addWidget(self.label_15)
        self.help_input_mca_data = HelpButton(self.input_data_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_input_mca_data.setIcon(icon)
        self.help_input_mca_data.setIconSize(QtCore.QSize(24,24))
        self.help_input_mca_data.setFlat(True)
        self.help_input_mca_data.setObjectName("help_input_mca_data")
        self.hboxlayout6.addWidget(self.help_input_mca_data)
        spacerItem7 = QtGui.QSpacerItem(551,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem7)
        self.vboxlayout7.addLayout(self.hboxlayout6)
        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setObjectName("vboxlayout8")
        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")
        self.input_table = InputMcaTableWidget(self.input_data_page)
        self.input_table.setEnabled(True)
        self.input_table.setMouseTracking(False)
        self.input_table.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.input_table.setDragDropOverwriteMode(False)
        self.input_table.setAlternatingRowColors(True)
        self.input_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.input_table.setObjectName("input_table")
        self.hboxlayout7.addWidget(self.input_table)
        self.vboxlayout9 = QtGui.QVBoxLayout()
        self.vboxlayout9.setObjectName("vboxlayout9")
        spacerItem8 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout9.addItem(spacerItem8)
        self.groupBox_15 = QtGui.QGroupBox(self.input_data_page)
        self.groupBox_15.setObjectName("groupBox_15")
        self.vboxlayout10 = QtGui.QVBoxLayout(self.groupBox_15)
        self.vboxlayout10.setObjectName("vboxlayout10")
        self.input_next_button = QtGui.QPushButton(self.groupBox_15)
        self.input_next_button.setObjectName("input_next_button")
        self.vboxlayout10.addWidget(self.input_next_button)
        self.input_prev_button = QtGui.QPushButton(self.groupBox_15)
        self.input_prev_button.setObjectName("input_prev_button")
        self.vboxlayout10.addWidget(self.input_prev_button)
        self.input_cancel_button = QtGui.QPushButton(self.groupBox_15)
        self.input_cancel_button.setObjectName("input_cancel_button")
        self.vboxlayout10.addWidget(self.input_cancel_button)
        self.vboxlayout9.addWidget(self.groupBox_15)
        self.hboxlayout7.addLayout(self.vboxlayout9)
        self.vboxlayout8.addLayout(self.hboxlayout7)
        self.vboxlayout7.addLayout(self.vboxlayout8)
        self.mca_stack.addWidget(self.input_data_page)
        self.weight_page = QtGui.QWidget()
        self.weight_page.setGeometry(QtCore.QRect(0,0,100,30))
        self.weight_page.setObjectName("weight_page")
        self.vboxlayout11 = QtGui.QVBoxLayout(self.weight_page)
        self.vboxlayout11.setObjectName("vboxlayout11")
        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")
        self.label_17 = QtGui.QLabel(self.weight_page)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.hboxlayout8.addWidget(self.label_17)
        self.help_weight_criteria = HelpButton(self.weight_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_weight_criteria.setIcon(icon)
        self.help_weight_criteria.setIconSize(QtCore.QSize(24,24))
        self.help_weight_criteria.setFlat(True)
        self.help_weight_criteria.setObjectName("help_weight_criteria")
        self.hboxlayout8.addWidget(self.help_weight_criteria)
        spacerItem9 = QtGui.QSpacerItem(501,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem9)
        self.vboxlayout11.addLayout(self.hboxlayout8)
        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")
        self.equal_weight_button = QtGui.QPushButton(self.weight_page)
        self.equal_weight_button.setObjectName("equal_weight_button")
        self.hboxlayout9.addWidget(self.equal_weight_button)
        spacerItem10 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem10)
        self.vboxlayout11.addLayout(self.hboxlayout9)
        self.hboxlayout10 = QtGui.QHBoxLayout()
        self.hboxlayout10.setObjectName("hboxlayout10")
        self.weight_table = WeightMcaTableWidget(self.weight_page)
        self.weight_table.setEnabled(True)
        self.weight_table.setMinimumSize(QtCore.QSize(400,0))
        self.weight_table.setMouseTracking(False)
        self.weight_table.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.weight_table.setAlternatingRowColors(True)
        self.weight_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.weight_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.weight_table.setObjectName("weight_table")
        self.hboxlayout10.addWidget(self.weight_table)
        spacerItem11 = QtGui.QSpacerItem(111,245,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout10.addItem(spacerItem11)
        self.vboxlayout12 = QtGui.QVBoxLayout()
        self.vboxlayout12.setObjectName("vboxlayout12")
        spacerItem12 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout12.addItem(spacerItem12)
        self.groupBox_12 = QtGui.QGroupBox(self.weight_page)
        self.groupBox_12.setObjectName("groupBox_12")
        self.vboxlayout13 = QtGui.QVBoxLayout(self.groupBox_12)
        self.vboxlayout13.setObjectName("vboxlayout13")
        self.run_analysis_button = QtGui.QPushButton(self.groupBox_12)
        self.run_analysis_button.setObjectName("run_analysis_button")
        self.vboxlayout13.addWidget(self.run_analysis_button)
        self.weight_prev_button = QtGui.QPushButton(self.groupBox_12)
        self.weight_prev_button.setObjectName("weight_prev_button")
        self.vboxlayout13.addWidget(self.weight_prev_button)
        self.weight_cancel_button = QtGui.QPushButton(self.groupBox_12)
        self.weight_cancel_button.setObjectName("weight_cancel_button")
        self.vboxlayout13.addWidget(self.weight_cancel_button)
        self.vboxlayout12.addWidget(self.groupBox_12)
        self.hboxlayout10.addLayout(self.vboxlayout12)
        self.vboxlayout11.addLayout(self.hboxlayout10)
        self.mca_stack.addWidget(self.weight_page)
        self.vboxlayout.addWidget(self.mca_stack)
        self.actionHelp_button2 = QtGui.QAction(McaWizard)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionHelp_button2.setIcon(icon)
        self.actionHelp_button2.setObjectName("actionHelp_button2")

        self.retranslateUi(McaWizard)
        self.mca_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(McaWizard)

    def retranslateUi(self, McaWizard):
        McaWizard.setWindowTitle(QtGui.QApplication.translate("McaWizard", "Multicriteria Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.mca_stack.setAccessibleDescription(QtGui.QApplication.translate("McaWizard", "help_seleccionar_criterios", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("McaWizard", "Step 1: Select Alternatives", None, QtGui.QApplication.UnicodeUTF8))
        self.help_select_alternatives.setAccessibleDescription(QtGui.QApplication.translate("McaWizard", "help_seleccionar_alternativas", None, QtGui.QApplication.UnicodeUTF8))
        self.check_all_altern_button.setText(QtGui.QApplication.translate("McaWizard", "Check All", None, QtGui.QApplication.UnicodeUTF8))
        self.uncheck_all_altern_button.setText(QtGui.QApplication.translate("McaWizard", "Uncheck All", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setRowCount(0)
        self.altern_table.setColumnCount(3)
        self.altern_table.clear()
        self.altern_table.setColumnCount(3)
        self.altern_table.setRowCount(0)
        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("McaWizard", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(0,headerItem)
        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("McaWizard", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(1,headerItem1)
        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("McaWizard", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(2,headerItem2)
        self.altern_next_button.setText(QtGui.QApplication.translate("McaWizard", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_cancel_button.setText(QtGui.QApplication.translate("McaWizard", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("McaWizard", "Step 2: Select Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.help_select_criteria.setAccessibleDescription(QtGui.QApplication.translate("McaWizard", "help_seleccionar_criterios", None, QtGui.QApplication.UnicodeUTF8))
        self.check_all_criteria_button.setText(QtGui.QApplication.translate("McaWizard", "Check All", None, QtGui.QApplication.UnicodeUTF8))
        self.uncheck_all_criteria_button.setText(QtGui.QApplication.translate("McaWizard", "Uncheck All", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setRowCount(0)
        self.crit_table.setColumnCount(5)
        self.crit_table.clear()
        self.crit_table.setColumnCount(5)
        self.crit_table.setRowCount(0)
        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("McaWizard", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(0,headerItem3)
        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(QtGui.QApplication.translate("McaWizard", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(1,headerItem4)
        headerItem5 = QtGui.QTableWidgetItem()
        headerItem5.setText(QtGui.QApplication.translate("McaWizard", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(2,headerItem5)
        headerItem6 = QtGui.QTableWidgetItem()
        headerItem6.setText(QtGui.QApplication.translate("McaWizard", "Options/Units", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(3,headerItem6)
        headerItem7 = QtGui.QTableWidgetItem()
        headerItem7.setText(QtGui.QApplication.translate("McaWizard", "Cost/Benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(4,headerItem7)
        self.crit_next_button.setText(QtGui.QApplication.translate("McaWizard", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_prev_button.setText(QtGui.QApplication.translate("McaWizard", "Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_cancel_button.setText(QtGui.QApplication.translate("McaWizard", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("McaWizard", "Step 3: Input Data", None, QtGui.QApplication.UnicodeUTF8))
        self.help_input_mca_data.setAccessibleDescription(QtGui.QApplication.translate("McaWizard", "help_ingresar_datos", None, QtGui.QApplication.UnicodeUTF8))
        self.input_table.setRowCount(0)
        self.input_table.setColumnCount(0)
        self.input_table.clear()
        self.input_table.setColumnCount(0)
        self.input_table.setRowCount(0)
        self.input_next_button.setText(QtGui.QApplication.translate("McaWizard", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.input_prev_button.setText(QtGui.QApplication.translate("McaWizard", "Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.input_cancel_button.setText(QtGui.QApplication.translate("McaWizard", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("McaWizard", "Step 4: Assign Weights", None, QtGui.QApplication.UnicodeUTF8))
        self.help_weight_criteria.setAccessibleDescription(QtGui.QApplication.translate("McaWizard", "help_ponderar_criterios", None, QtGui.QApplication.UnicodeUTF8))
        self.equal_weight_button.setText(QtGui.QApplication.translate("McaWizard", "Assign Equal Weighting", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_table.setRowCount(0)
        self.weight_table.setColumnCount(1)
        self.weight_table.clear()
        self.weight_table.setColumnCount(1)
        self.weight_table.setRowCount(0)
        headerItem8 = QtGui.QTableWidgetItem()
        headerItem8.setText(QtGui.QApplication.translate("McaWizard", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_table.setHorizontalHeaderItem(0,headerItem8)
        self.run_analysis_button.setText(QtGui.QApplication.translate("McaWizard", "Run Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_prev_button.setText(QtGui.QApplication.translate("McaWizard", "Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_cancel_button.setText(QtGui.QApplication.translate("McaWizard", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_button2.setText(QtGui.QApplication.translate("McaWizard", "help_button2", None, QtGui.QApplication.UnicodeUTF8))

from AlternativeMcaTableWidget import AlternativeMcaTableWidget
from InputMcaTableWidget import InputMcaTableWidget
from HelpButton import HelpButton
from CriteriaMcaTableWidget import CriteriaMcaTableWidget
from WeightMcaTableWidget import WeightMcaTableWidget
import resources_rc
