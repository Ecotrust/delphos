# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_view.ui'
#
# Created: Sun Jun 29 00:16:38 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProjectView(object):
    def setupUi(self, ProjectView):
        ProjectView.setObjectName("ProjectView")
        ProjectView.setWindowModality(QtCore.Qt.NonModal)
        ProjectView.resize(746,430)
        ProjectView.setMinimumSize(QtCore.QSize(650,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        ProjectView.setFont(font)
        ProjectView.setStyleSheet(""".QWidget {
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
.QWidget {
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
        self.hboxlayout = QtGui.QHBoxLayout(ProjectView)
        self.hboxlayout.setObjectName("hboxlayout")
        self.tabProject = QtGui.QTabWidget(ProjectView)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.tabProject.setFont(font)
        self.tabProject.setObjectName("tabProject")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setGeometry(QtCore.QRect(0,0,722,384))
        self.tab_3.setObjectName("tab_3")
        self.vboxlayout = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.hboxlayout2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.label = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.vboxlayout1.addWidget(self.label_3)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.vboxlayout1.addWidget(self.label_6)
        self.hboxlayout2.addLayout(self.vboxlayout1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.project_name = QtGui.QLabel(self.groupBox_3)
        self.project_name.setMinimumSize(QtCore.QSize(200,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.project_name.setFont(font)
        self.project_name.setObjectName("project_name")
        self.vboxlayout2.addWidget(self.project_name)
        self.project_type = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.project_type.setFont(font)
        self.project_type.setObjectName("project_type")
        self.vboxlayout2.addWidget(self.project_type)
        self.project_created = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.project_created.setFont(font)
        self.project_created.setObjectName("project_created")
        self.vboxlayout2.addWidget(self.project_created)
        self.num_runs_label = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.num_runs_label.setFont(font)
        self.num_runs_label.setObjectName("num_runs_label")
        self.vboxlayout2.addWidget(self.num_runs_label)
        self.hboxlayout2.addLayout(self.vboxlayout2)
        self.hboxlayout1.addWidget(self.groupBox_3)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setMinimumSize(QtCore.QSize(150,0))
        self.groupBox_6.setObjectName("groupBox_6")
        self.hboxlayout3 = QtGui.QHBoxLayout(self.groupBox_6)
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.label_7 = QtGui.QLabel(self.groupBox_6)
        self.label_7.setMinimumSize(QtCore.QSize(140,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.hboxlayout4.addWidget(self.label_7)
        self.help_test = HelpButton(self.groupBox_6)
        self.help_test.setMaximumSize(QtCore.QSize(40,16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_test.setIcon(icon)
        self.help_test.setIconSize(QtCore.QSize(24,24))
        self.help_test.setFlat(True)
        self.help_test.setObjectName("help_test")
        self.hboxlayout4.addWidget(self.help_test)
        self.hboxlayout3.addLayout(self.hboxlayout4)
        self.hboxlayout1.addWidget(self.groupBox_6)
        self.vboxlayout.addLayout(self.hboxlayout1)
        spacerItem = QtGui.QSpacerItem(348,71,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.tabProject.addTab(self.tab_3,"")
        self.tab = QtGui.QWidget()
        self.tab.setGeometry(QtCore.QRect(0,0,722,384))
        self.tab.setObjectName("tab")
        self.hboxlayout5 = QtGui.QHBoxLayout(self.tab)
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(0,0))
        self.groupBox.setMaximumSize(QtCore.QSize(120,16777215))
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.add_altern_button = QtGui.QPushButton(self.groupBox)
        self.add_altern_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.add_altern_button.setFont(font)
        self.add_altern_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.add_altern_button.setObjectName("add_altern_button")
        self.vboxlayout4.addWidget(self.add_altern_button)
        self.remove_altern_button = QtGui.QPushButton(self.groupBox)
        self.remove_altern_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.remove_altern_button.setFont(font)
        self.remove_altern_button.setObjectName("remove_altern_button")
        self.vboxlayout4.addWidget(self.remove_altern_button)
        self.vboxlayout3.addWidget(self.groupBox)
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setMaximumSize(QtCore.QSize(120,16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hboxlayout6 = QtGui.QHBoxLayout(self.frame)
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setObjectName("hboxlayout6")
        spacerItem1 = QtGui.QSpacerItem(61,16,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem1)
        self.help_define_alternatives = HelpButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_define_alternatives.setIcon(icon)
        self.help_define_alternatives.setIconSize(QtCore.QSize(24,24))
        self.help_define_alternatives.setFlat(True)
        self.help_define_alternatives.setObjectName("help_define_alternatives")
        self.hboxlayout6.addWidget(self.help_define_alternatives)
        self.vboxlayout3.addWidget(self.frame)
        spacerItem2 = QtGui.QSpacerItem(40,101,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem2)
        self.hboxlayout5.addLayout(self.vboxlayout3)
        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName("vboxlayout5")
        self.altern_table = AlternativeTableWidget(self.tab)
        self.altern_table.setEnabled(True)
        self.altern_table.setMinimumSize(QtCore.QSize(180,300))
        self.altern_table.setMaximumSize(QtCore.QSize(16777215,300))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.altern_table.setFont(font)
        self.altern_table.setMouseTracking(False)
        self.altern_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.altern_table.setDragDropOverwriteMode(False)
        self.altern_table.setAlternatingRowColors(True)
        self.altern_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.altern_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.altern_table.setObjectName("altern_table")
        self.vboxlayout5.addWidget(self.altern_table)
        spacerItem3 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout5.addItem(spacerItem3)
        self.hboxlayout5.addLayout(self.vboxlayout5)
        spacerItem4 = QtGui.QSpacerItem(200,316,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem4)
        self.tabProject.addTab(self.tab,"")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setGeometry(QtCore.QRect(0,0,722,384))
        self.tab_2.setObjectName("tab_2")
        self.hboxlayout7 = QtGui.QHBoxLayout(self.tab_2)
        self.hboxlayout7.setObjectName("hboxlayout7")
        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setObjectName("vboxlayout7")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setMaximumSize(QtCore.QSize(120,16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout8 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout8.setObjectName("vboxlayout8")
        self.add_criteria_button = QtGui.QPushButton(self.groupBox_2)
        self.add_criteria_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.add_criteria_button.setFont(font)
        self.add_criteria_button.setObjectName("add_criteria_button")
        self.vboxlayout8.addWidget(self.add_criteria_button)
        self.edit_criteria_button = QtGui.QPushButton(self.groupBox_2)
        self.edit_criteria_button.setObjectName("edit_criteria_button")
        self.vboxlayout8.addWidget(self.edit_criteria_button)
        self.remove_criteria_button = QtGui.QPushButton(self.groupBox_2)
        self.remove_criteria_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.remove_criteria_button.setFont(font)
        self.remove_criteria_button.setObjectName("remove_criteria_button")
        self.vboxlayout8.addWidget(self.remove_criteria_button)
        self.vboxlayout7.addWidget(self.groupBox_2)
        self.frame_2 = QtGui.QFrame(self.tab_2)
        self.frame_2.setMaximumSize(QtCore.QSize(120,16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hboxlayout8 = QtGui.QHBoxLayout(self.frame_2)
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setObjectName("hboxlayout8")
        spacerItem5 = QtGui.QSpacerItem(21,16,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem5)
        self.help_define_criteria = HelpButton(self.frame_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_define_criteria.setIcon(icon)
        self.help_define_criteria.setIconSize(QtCore.QSize(24,24))
        self.help_define_criteria.setFlat(True)
        self.help_define_criteria.setObjectName("help_define_criteria")
        self.hboxlayout8.addWidget(self.help_define_criteria)
        self.vboxlayout7.addWidget(self.frame_2)
        self.vboxlayout6.addLayout(self.vboxlayout7)
        spacerItem6 = QtGui.QSpacerItem(95,111,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout6.addItem(spacerItem6)
        self.hboxlayout7.addLayout(self.vboxlayout6)
        self.crit_table = CriteriaTableWidget(self.tab_2)
        self.crit_table.setMinimumSize(QtCore.QSize(0,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.crit_table.setFont(font)
        self.crit_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.crit_table.setDragDropOverwriteMode(False)
        self.crit_table.setAlternatingRowColors(True)
        self.crit_table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.crit_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.crit_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.crit_table.setObjectName("crit_table")
        self.hboxlayout7.addWidget(self.crit_table)
        self.tabProject.addTab(self.tab_2,"")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setGeometry(QtCore.QRect(0,0,722,384))
        self.tab_5.setObjectName("tab_5")
        self.vboxlayout9 = QtGui.QVBoxLayout(self.tab_5)
        self.vboxlayout9.setObjectName("vboxlayout9")
        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")
        self.groupBox_11 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_11.setObjectName("groupBox_11")
        self.hboxlayout10 = QtGui.QHBoxLayout(self.groupBox_11)
        self.hboxlayout10.setObjectName("hboxlayout10")
        self.save_button = QtGui.QPushButton(self.groupBox_11)
        self.save_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.hboxlayout10.addWidget(self.save_button)
        self.reset_button = QtGui.QPushButton(self.groupBox_11)
        self.reset_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.hboxlayout10.addWidget(self.reset_button)
        self.export_button = QtGui.QPushButton(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.hboxlayout10.addWidget(self.export_button)
        self.import_button = QtGui.QPushButton(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.hboxlayout10.addWidget(self.import_button)
        self.hboxlayout9.addWidget(self.groupBox_11)
        self.help_input_data = HelpButton(self.tab_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_input_data.setIcon(icon)
        self.help_input_data.setIconSize(QtCore.QSize(24,24))
        self.help_input_data.setFlat(True)
        self.help_input_data.setObjectName("help_input_data")
        self.hboxlayout9.addWidget(self.help_input_data)
        spacerItem7 = QtGui.QSpacerItem(361,44,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem7)
        self.vboxlayout9.addLayout(self.hboxlayout9)
        self.hboxlayout11 = QtGui.QHBoxLayout()
        self.hboxlayout11.setObjectName("hboxlayout11")
        self.input_table = InputGlobalTableWidget(self.tab_5)
        self.input_table.setEnabled(True)
        self.input_table.setMouseTracking(False)
        self.input_table.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.input_table.setDragDropOverwriteMode(False)
        self.input_table.setAlternatingRowColors(False)
        self.input_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.input_table.setObjectName("input_table")
        self.hboxlayout11.addWidget(self.input_table)
        self.vboxlayout9.addLayout(self.hboxlayout11)
        self.tabProject.addTab(self.tab_5,"")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setGeometry(QtCore.QRect(0,0,722,384))
        self.tab_4.setObjectName("tab_4")
        self.hboxlayout12 = QtGui.QHBoxLayout(self.tab_4)
        self.hboxlayout12.setObjectName("hboxlayout12")
        self.vboxlayout10 = QtGui.QVBoxLayout()
        self.vboxlayout10.setObjectName("vboxlayout10")
        self.groupBox_4 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_4.setMaximumSize(QtCore.QSize(250,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout11 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout11.setObjectName("vboxlayout11")
        self.hboxlayout13 = QtGui.QHBoxLayout()
        self.hboxlayout13.setObjectName("hboxlayout13")
        self.vboxlayout12 = QtGui.QVBoxLayout()
        self.vboxlayout12.setSpacing(2)
        self.vboxlayout12.setObjectName("vboxlayout12")
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.vboxlayout12.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.vboxlayout12.addWidget(self.label_4)
        self.hboxlayout13.addLayout(self.vboxlayout12)
        self.vboxlayout13 = QtGui.QVBoxLayout()
        self.vboxlayout13.setSpacing(2)
        self.vboxlayout13.setObjectName("vboxlayout13")
        self.analysis_name_edit = QtGui.QLineEdit(self.groupBox_4)
        self.analysis_name_edit.setMinimumSize(QtCore.QSize(100,0))
        self.analysis_name_edit.setMaximumSize(QtCore.QSize(150,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.analysis_name_edit.setFont(font)
        self.analysis_name_edit.setObjectName("analysis_name_edit")
        self.vboxlayout13.addWidget(self.analysis_name_edit)
        self.analysis_description_edit = QtGui.QLineEdit(self.groupBox_4)
        self.analysis_description_edit.setMinimumSize(QtCore.QSize(100,0))
        self.analysis_description_edit.setMaximumSize(QtCore.QSize(150,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.analysis_description_edit.setFont(font)
        self.analysis_description_edit.setObjectName("analysis_description_edit")
        self.vboxlayout13.addWidget(self.analysis_description_edit)
        self.hboxlayout13.addLayout(self.vboxlayout13)
        self.vboxlayout11.addLayout(self.hboxlayout13)
        self.hboxlayout14 = QtGui.QHBoxLayout()
        self.hboxlayout14.setObjectName("hboxlayout14")
        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout14.addItem(spacerItem8)
        self.new_analysis_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.new_analysis_button.setFont(font)
        self.new_analysis_button.setObjectName("new_analysis_button")
        self.hboxlayout14.addWidget(self.new_analysis_button)
        self.help_8_run_analysis = HelpButton(self.groupBox_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_8_run_analysis.setIcon(icon)
        self.help_8_run_analysis.setIconSize(QtCore.QSize(24,24))
        self.help_8_run_analysis.setFlat(True)
        self.help_8_run_analysis.setObjectName("help_8_run_analysis")
        self.hboxlayout14.addWidget(self.help_8_run_analysis)
        self.vboxlayout11.addLayout(self.hboxlayout14)
        self.vboxlayout10.addWidget(self.groupBox_4)
        spacerItem9 = QtGui.QSpacerItem(251,161,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout10.addItem(spacerItem9)
        self.hboxlayout12.addLayout(self.vboxlayout10)
        self.groupBox_5 = QtGui.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.vboxlayout14 = QtGui.QVBoxLayout(self.groupBox_5)
        self.vboxlayout14.setObjectName("vboxlayout14")
        self.mca_runs_table = McaRunsTableWidget(self.groupBox_5)
        self.mca_runs_table.setMinimumSize(QtCore.QSize(200,200))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.mca_runs_table.setFont(font)
        self.mca_runs_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.mca_runs_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.mca_runs_table.setObjectName("mca_runs_table")
        self.vboxlayout14.addWidget(self.mca_runs_table)
        self.hboxlayout15 = QtGui.QHBoxLayout()
        self.hboxlayout15.setObjectName("hboxlayout15")
        self.hboxlayout16 = QtGui.QHBoxLayout()
        self.hboxlayout16.setObjectName("hboxlayout16")
        self.view_analysis_button = QtGui.QPushButton(self.groupBox_5)
        self.view_analysis_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.view_analysis_button.setFont(font)
        self.view_analysis_button.setObjectName("view_analysis_button")
        self.hboxlayout16.addWidget(self.view_analysis_button)
        self.rerun_analysis_button = QtGui.QPushButton(self.groupBox_5)
        self.rerun_analysis_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.rerun_analysis_button.setFont(font)
        self.rerun_analysis_button.setObjectName("rerun_analysis_button")
        self.hboxlayout16.addWidget(self.rerun_analysis_button)
        self.export_analysis_button = QtGui.QPushButton(self.groupBox_5)
        self.export_analysis_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.export_analysis_button.setFont(font)
        self.export_analysis_button.setObjectName("export_analysis_button")
        self.hboxlayout16.addWidget(self.export_analysis_button)
        self.delete_analysis_button = QtGui.QPushButton(self.groupBox_5)
        self.delete_analysis_button.setMinimumSize(QtCore.QSize(37,14))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.delete_analysis_button.setFont(font)
        self.delete_analysis_button.setObjectName("delete_analysis_button")
        self.hboxlayout16.addWidget(self.delete_analysis_button)
        self.help_run_the_program = HelpButton(self.groupBox_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.help_run_the_program.setIcon(icon)
        self.help_run_the_program.setIconSize(QtCore.QSize(24,24))
        self.help_run_the_program.setFlat(True)
        self.help_run_the_program.setObjectName("help_run_the_program")
        self.hboxlayout16.addWidget(self.help_run_the_program)
        self.hboxlayout15.addLayout(self.hboxlayout16)
        spacerItem10 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout15.addItem(spacerItem10)
        self.vboxlayout14.addLayout(self.hboxlayout15)
        self.hboxlayout12.addWidget(self.groupBox_5)
        self.tabProject.addTab(self.tab_4,"")
        self.hboxlayout.addWidget(self.tabProject)

        self.retranslateUi(ProjectView)
        self.tabProject.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectView)

    def retranslateUi(self, ProjectView):
        ProjectView.setWindowTitle(QtGui.QApplication.translate("ProjectView", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectView", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProjectView", "Project Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProjectView", "Date Created:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProjectView", "Saved Analysis Runs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ProjectView", "Click buttons, like the one to the right, to get detailed help.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_3), QtGui.QApplication.translate("ProjectView", "Project Info", None, QtGui.QApplication.UnicodeUTF8))
        self.add_altern_button.setText(QtGui.QApplication.translate("ProjectView", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_altern_button.setText(QtGui.QApplication.translate("ProjectView", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.help_define_alternatives.setAccessibleDescription(QtGui.QApplication.translate("ProjectView", "help_definir_las_alternativas", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setRowCount(1)
        self.altern_table.setColumnCount(2)
        self.altern_table.clear()
        self.altern_table.setColumnCount(2)
        self.altern_table.setRowCount(1)
        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("ProjectView", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(0,headerItem)
        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("ProjectView", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(1,headerItem1)
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab), QtGui.QApplication.translate("ProjectView", "Alternatives", None, QtGui.QApplication.UnicodeUTF8))
        self.add_criteria_button.setText(QtGui.QApplication.translate("ProjectView", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_criteria_button.setText(QtGui.QApplication.translate("ProjectView", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_criteria_button.setText(QtGui.QApplication.translate("ProjectView", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.help_define_criteria.setAccessibleDescription(QtGui.QApplication.translate("ProjectView", "help_definir_los_criterios", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setRowCount(0)
        self.crit_table.setColumnCount(4)
        self.crit_table.clear()
        self.crit_table.setColumnCount(4)
        self.crit_table.setRowCount(0)
        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("ProjectView", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(0,headerItem2)
        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("ProjectView", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(1,headerItem3)
        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(QtGui.QApplication.translate("ProjectView", "Options or Units", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(2,headerItem4)
        headerItem5 = QtGui.QTableWidgetItem()
        headerItem5.setText(QtGui.QApplication.translate("ProjectView", "Cost/Benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(3,headerItem5)
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_2), QtGui.QApplication.translate("ProjectView", "Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate("ProjectView", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_button.setText(QtGui.QApplication.translate("ProjectView", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.export_button.setText(QtGui.QApplication.translate("ProjectView", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.import_button.setText(QtGui.QApplication.translate("ProjectView", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.help_input_data.setAccessibleDescription(QtGui.QApplication.translate("ProjectView", "help_ingresar_datos", None, QtGui.QApplication.UnicodeUTF8))
        self.input_table.setRowCount(0)
        self.input_table.setColumnCount(0)
        self.input_table.clear()
        self.input_table.setColumnCount(0)
        self.input_table.setRowCount(0)
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_5), QtGui.QApplication.translate("ProjectView", "Input Data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ProjectView", "New Analysis:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProjectView", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ProjectView", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.new_analysis_button.setText(QtGui.QApplication.translate("ProjectView", "Start  Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.help_8_run_analysis.setAccessibleDescription(QtGui.QApplication.translate("ProjectView", "help_8_corra_el_análisis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("ProjectView", "Previous Analyses:", None, QtGui.QApplication.UnicodeUTF8))
        self.mca_runs_table.clear()
        self.mca_runs_table.setColumnCount(3)
        self.mca_runs_table.setRowCount(0)
        headerItem6 = QtGui.QTableWidgetItem()
        headerItem6.setText(QtGui.QApplication.translate("ProjectView", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.mca_runs_table.setHorizontalHeaderItem(0,headerItem6)
        headerItem7 = QtGui.QTableWidgetItem()
        headerItem7.setText(QtGui.QApplication.translate("ProjectView", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.mca_runs_table.setHorizontalHeaderItem(1,headerItem7)
        headerItem8 = QtGui.QTableWidgetItem()
        headerItem8.setText(QtGui.QApplication.translate("ProjectView", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.mca_runs_table.setHorizontalHeaderItem(2,headerItem8)
        self.view_analysis_button.setText(QtGui.QApplication.translate("ProjectView", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.rerun_analysis_button.setText(QtGui.QApplication.translate("ProjectView", "Restart", None, QtGui.QApplication.UnicodeUTF8))
        self.export_analysis_button.setText(QtGui.QApplication.translate("ProjectView", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_analysis_button.setText(QtGui.QApplication.translate("ProjectView", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.help_run_the_program.setAccessibleDescription(QtGui.QApplication.translate("ProjectView", "correr_el_programa", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_4), QtGui.QApplication.translate("ProjectView", "Analysis", None, QtGui.QApplication.UnicodeUTF8))

from AlternativeTableWidget import AlternativeTableWidget
from McaRunsTableWidget import McaRunsTableWidget
from HelpButton import HelpButton
from CriteriaTableWidget import CriteriaTableWidget
from InputGlobalTableWidget import InputGlobalTableWidget
import resources_rc
