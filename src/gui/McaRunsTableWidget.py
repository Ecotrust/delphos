import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class McaRunsTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.name_column = 0
        self.description_column = 1
        self.date_column = 2

    def load(self, recs):
        """Loads the table with info on past analysis runs
        """
        
        print recs
        if recs:
            self.clearContents()
            self.num_rows = len(recs)
            self.setRowCount(self.num_rows)
        
            for i in range(self.num_rows):
                print recs[i][0]
                name_item = QTableWidgetItem()
                name_item.setText(recs[i][0])
                self.setItem(i, 0, name_item)
                desc_item = QTableWidgetItem()
                desc_item.setText(recs[i][1])
                self.setItem(i, 1, desc_item)
                date_item = QTableWidgetItem()
                date_item.setText(unicode(recs[i][2]))
                self.setItem(i, 2, date_item)
            self.resizeColumnsToContents()

    def check_all(self):
        for i in range(self.num_rows):
            check_box = self.cellWidget(i, self.check_column)
            check_box.setCheckState(Qt.Checked)
        
    def uncheck_all(self):
        for i in range(self.num_rows):
            check_box = self.cellWidget(i, self.check_column)
            check_box.setCheckState(Qt.Unchecked)

    def get_selected_indexes(self):
        selected_indexes = []
        for row in range(self.num_rows):
            check_widget = self.cellWidget(row, 0)
            check_state = check_widget.checkState()
            if check_state == Qt.Checked:
                selected_indexes.append(row)
        return selected_indexes

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            #Return the unique criteria description
            return selected_row[0]
        else:
            raise DelphosError, "You must first select a criterion"
        