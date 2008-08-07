# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mca_result_view.ui'
#
# Created: Sun Jun 29 02:53:32 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_McaResultView(object):
    def setupUi(self, McaResultView):
        McaResultView.setObjectName("McaResultView")
        McaResultView.setWindowModality(QtCore.Qt.NonModal)
        McaResultView.resize(500,387)
        McaResultView.setMinimumSize(QtCore.QSize(500,350))
        font = QtGui.QFont()
        font.setFamily("arial")
        McaResultView.setFont(font)
        McaResultView.setStyleSheet(""".QWidget {
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
        self.hboxlayout = QtGui.QHBoxLayout(McaResultView)
        self.hboxlayout.setObjectName("hboxlayout")
        self.summary_tab = QtGui.QTabWidget(McaResultView)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.summary_tab.setFont(font)
        self.summary_tab.setObjectName("summary_tab")
        self.chart = QtGui.QWidget()
        self.chart.setGeometry(QtCore.QRect(0,0,476,340))
        self.chart.setObjectName("chart")
        self.vboxlayout = QtGui.QVBoxLayout(self.chart)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.chart)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.hboxlayout1.addLayout(self.vboxlayout1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.mca_plot_canvas = McaMplCanvas(self.chart)
        self.mca_plot_canvas.setMinimumSize(QtCore.QSize(380,250))
        self.mca_plot_canvas.setMaximumSize(QtCore.QSize(980,800))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.mca_plot_canvas.setFont(font)
        self.mca_plot_canvas.setObjectName("mca_plot_canvas")
        self.vboxlayout2.addWidget(self.mca_plot_canvas)
        self.hboxlayout1.addLayout(self.vboxlayout2)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.chart)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.hboxlayout2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem3)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.summary_tab.addTab(self.chart,"")
        self.alternatives = QtGui.QWidget()
        self.alternatives.setGeometry(QtCore.QRect(0,0,476,340))
        self.alternatives.setObjectName("alternatives")
        self.hboxlayout3 = QtGui.QHBoxLayout(self.alternatives)
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.altern_table = AlternativeTableWidget(self.alternatives)
        self.altern_table.setEnabled(True)
        self.altern_table.setMinimumSize(QtCore.QSize(120,60))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.altern_table.setFont(font)
        self.altern_table.setMouseTracking(False)
        self.altern_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.altern_table.setDragDropOverwriteMode(False)
        self.altern_table.setAlternatingRowColors(True)
        self.altern_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.altern_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.altern_table.setObjectName("altern_table")
        self.hboxlayout3.addWidget(self.altern_table)
        self.summary_tab.addTab(self.alternatives,"")
        self.criteria = QtGui.QWidget()
        self.criteria.setGeometry(QtCore.QRect(0,0,476,340))
        self.criteria.setObjectName("criteria")
        self.hboxlayout4 = QtGui.QHBoxLayout(self.criteria)
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.crit_table = CriteriaTableWidget(self.criteria)
        self.crit_table.setMinimumSize(QtCore.QSize(300,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.crit_table.setFont(font)
        self.crit_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.crit_table.setDragDropOverwriteMode(False)
        self.crit_table.setAlternatingRowColors(True)
        self.crit_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.crit_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.crit_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.crit_table.setObjectName("crit_table")
        self.hboxlayout4.addWidget(self.crit_table)
        self.summary_tab.addTab(self.criteria,"")
        self.input = QtGui.QWidget()
        self.input.setGeometry(QtCore.QRect(0,0,476,340))
        self.input.setObjectName("input")
        self.hboxlayout5 = QtGui.QHBoxLayout(self.input)
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.input_table = InputResultViewTableWidget(self.input)
        self.input_table.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("arial")
        self.input_table.setFont(font)
        self.input_table.setMouseTracking(False)
        self.input_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.input_table.setDragDropOverwriteMode(False)
        self.input_table.setAlternatingRowColors(True)
        self.input_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.input_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.input_table.setObjectName("input_table")
        self.hboxlayout5.addWidget(self.input_table)
        self.summary_tab.addTab(self.input,"")
        self.weights = QtGui.QWidget()
        self.weights.setGeometry(QtCore.QRect(0,0,476,340))
        self.weights.setObjectName("weights")
        self.hboxlayout6 = QtGui.QHBoxLayout(self.weights)
        self.hboxlayout6.setObjectName("hboxlayout6")
        self.weight_table = WeightMcaTableWidget(self.weights)
        self.weight_table.setEnabled(True)
        self.weight_table.setMinimumSize(QtCore.QSize(400,0))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.weight_table.setFont(font)
        self.weight_table.setMouseTracking(False)
        self.weight_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.weight_table.setAlternatingRowColors(True)
        self.weight_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.weight_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.weight_table.setObjectName("weight_table")
        self.hboxlayout6.addWidget(self.weight_table)
        self.summary_tab.addTab(self.weights,"")
        self.results = QtGui.QWidget()
        self.results.setGeometry(QtCore.QRect(0,0,476,340))
        self.results.setObjectName("results")
        self.hboxlayout7 = QtGui.QHBoxLayout(self.results)
        self.hboxlayout7.setObjectName("hboxlayout7")
        self.final_table = FinalScoreTableWidget(self.results)
        self.final_table.setMinimumSize(QtCore.QSize(250,0))
        self.final_table.setMaximumSize(QtCore.QSize(1677777,16777215))
        font = QtGui.QFont()
        font.setFamily("arial")
        self.final_table.setFont(font)
        self.final_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.final_table.setAlternatingRowColors(True)
        self.final_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.final_table.setSortingEnabled(False)
        self.final_table.setObjectName("final_table")
        self.hboxlayout7.addWidget(self.final_table)
        self.summary_tab.addTab(self.results,"")
        self.hboxlayout.addWidget(self.summary_tab)

        self.retranslateUi(McaResultView)
        self.summary_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(McaResultView)

    def retranslateUi(self, McaResultView):
        McaResultView.setWindowTitle(QtGui.QApplication.translate("McaResultView", "MCA Run Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("McaResultView", "Normalized\n"
" Score", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("McaResultView", "Rank", None, QtGui.QApplication.UnicodeUTF8))
        self.summary_tab.setTabText(self.summary_tab.indexOf(self.chart), QtGui.QApplication.translate("McaResultView", "Chart", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setRowCount(1)
        self.altern_table.setColumnCount(2)
        self.altern_table.clear()
        self.altern_table.setColumnCount(2)
        self.altern_table.setRowCount(1)
        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("McaResultView", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setVerticalHeaderItem(0,headerItem)
        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("McaResultView", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(0,headerItem1)
        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("McaResultView", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.altern_table.setHorizontalHeaderItem(1,headerItem2)
        self.summary_tab.setTabText(self.summary_tab.indexOf(self.alternatives), QtGui.QApplication.translate("McaResultView", "Alternatives", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setRowCount(0)
        self.crit_table.setColumnCount(4)
        self.crit_table.clear()
        self.crit_table.setColumnCount(4)
        self.crit_table.setRowCount(0)
        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("McaResultView", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(0,headerItem3)
        headerItem4 = QtGui.QTableWidgetItem()
        headerItem4.setText(QtGui.QApplication.translate("McaResultView", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(1,headerItem4)
        headerItem5 = QtGui.QTableWidgetItem()
        headerItem5.setText(QtGui.QApplication.translate("McaResultView", "Options/Units", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(2,headerItem5)
        headerItem6 = QtGui.QTableWidgetItem()
        headerItem6.setText(QtGui.QApplication.translate("McaResultView", "Cost/Benefit", None, QtGui.QApplication.UnicodeUTF8))
        self.crit_table.setHorizontalHeaderItem(3,headerItem6)
        self.summary_tab.setTabText(self.summary_tab.indexOf(self.criteria), QtGui.QApplication.translate("McaResultView", "Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.input_table.setRowCount(0)
        self.input_table.setColumnCount(0)
        self.input_table.clear()
        self.input_table.setColumnCount(0)
        self.input_table.setRowCount(0)
        self.summary_tab.setTabText(self.summary_tab.indexOf(self.input), QtGui.QApplication.translate("McaResultView", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_table.setRowCount(0)
        self.weight_table.setColumnCount(1)
        self.weight_table.clear()
        self.weight_table.setColumnCount(1)
        self.weight_table.setRowCount(0)
        headerItem7 = QtGui.QTableWidgetItem()
        headerItem7.setText(QtGui.QApplication.translate("McaResultView", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_table.setHorizontalHeaderItem(0,headerItem7)
        self.summary_tab.setTabText(self.summary_tab.indexOf(self.weights), QtGui.QApplication.translate("McaResultView", "Weights", None, QtGui.QApplication.UnicodeUTF8))
        self.final_table.clear()
        self.final_table.setColumnCount(3)
        self.final_table.setRowCount(0)
        headerItem8 = QtGui.QTableWidgetItem()
        headerItem8.setText(QtGui.QApplication.translate("McaResultView", "Final Score", None, QtGui.QApplication.UnicodeUTF8))
        self.final_table.setHorizontalHeaderItem(0,headerItem8)
        headerItem9 = QtGui.QTableWidgetItem()
        headerItem9.setText(QtGui.QApplication.translate("McaResultView", "Rank", None, QtGui.QApplication.UnicodeUTF8))
        self.final_table.setHorizontalHeaderItem(1,headerItem9)
        headerItem10 = QtGui.QTableWidgetItem()
        headerItem10.setText(QtGui.QApplication.translate("McaResultView", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.final_table.setHorizontalHeaderItem(2,headerItem10)
        self.summary_tab.setTabText(self.summary_tab.indexOf(self.results), QtGui.QApplication.translate("McaResultView", "Results", None, QtGui.QApplication.UnicodeUTF8))

from CriteriaTableWidget import CriteriaTableWidget
from McaMplCanvas import McaMplCanvas
from WeightMcaTableWidget import WeightMcaTableWidget
from AlternativeTableWidget import AlternativeTableWidget
from InputResultViewTableWidget import InputResultViewTableWidget
from FinalScoreTableWidget import FinalScoreTableWidget
