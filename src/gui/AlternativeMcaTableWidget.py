import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlternativeMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)
        self.altern_name_column = 1;        #Columns containing alternative names

    def load(self, alternative_recs):
        """Loads the table with alternatives, given an array of records
        """
        self.clearContents()
        self.setRowCount(len(alternative_recs))
        
        for i in range(len(alternative_recs)):
            #Add checkbox widget to first column
            check_box = QtGui.QCheckBox(self)
            check_box.setCheckState(Qt.Checked)
            self.setCellWidget(i, 0, check_box)            
            
            #Add alternative name to second column
            item = QTableWidgetItem()
            item.setText(str(alternative_recs[i][self.altern_name_column]))
            self.setItem(i, 1, item)
        self.resizeColumnsToContents()
    
    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            return selected_row[0]
        else:
            raise DelphosError, "You must first select an alternative"
        