import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlternativeTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)
        self.altern_name_column = 1;        #Columns containing alternative names
        
    def load(self, alternative_recs):
        """Loads the table with alternatives, given an array of records
        """
        self.clearContents()
        self.setRowCount(len(alternative_recs))
        
        for i in range(len(alternative_recs)):
            item = QTableWidgetItem()
            item.setText(str(alternative_recs[i][self.altern_name_column]))
            self.setItem(i, 0, item)
        self.resizeColumnsToContents()

    def get_selected_ids(self):
        return []

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            return selected_row[0]
        else:
            raise DelphosError, "You must first select an alternative"
        