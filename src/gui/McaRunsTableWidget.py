import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class McaRunsTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.id_column = 0
        self.name_column = 1
        self.description_column = 2
        self.date_column = 3
        
        self.name_display_column = 0
        self.description_display_column = 1
        self.date_display_column = 2

    def load(self, mca_recs):
        """Loads the table with info on past analysis runs
        """
        if mca_recs:
            self.mca_recs = mca_recs
            self.clearContents()
            self.num_rows = len(mca_recs)
            self.setRowCount(self.num_rows)
        
            for i in range(self.num_rows):
                name_item = QTableWidgetItem()
                name_item.setText(mca_recs[i][self.name_column])
                self.setItem(i, self.name_display_column, name_item)
                desc_item = QTableWidgetItem()
                desc_item.setText(mca_recs[i][self.description_column])
                self.setItem(i, self.description_display_column, desc_item)
                date_item = QTableWidgetItem()
                date_item.setText(unicode(mca_recs[i][self.date_column]))
                self.setItem(i, self.date_display_column, date_item)
            self.resizeColumnsToContents()

    def get_selected_id(self):
        index = self.get_current_index()
        return self.mca_recs[index][self.id_column]

    def get_current_index(self):
        try:
            cur_row_item = self.get_current_row_items()
        except DelphosError, e:
            QMessageBox.critical(self,"Please select an analysis record first.")
        else:
            if cur_row_item:
                return cur_row_item.row()

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            #Return the unique criteria description
            return selected_row[0]
        else:
            raise DelphosError
        