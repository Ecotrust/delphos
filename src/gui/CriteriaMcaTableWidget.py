import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DelphosCheckBox import *

class CriteriaMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.id_column = 0
        self.check_column = 0
        self.crit_name_column = 1
        self.crit_type_column = 2
        self.crit_options_column = 3
        self.cost_benefit_column = 4

    def load(self, criteria_recs):
        """Loads the table in the criteria tab with the existing project criteria
        """
        if criteria_recs:
            self.clearContents()
            self.num_rows = len(criteria_recs)
            self.setRowCount(self.num_rows)
        
            for i in range(self.num_rows):
                #Add checkbox widget to first column
                check_box = DelphosCheckBox(self)
                check_box.setValue(criteria_recs[i][self.id_column])
                self.setCellWidget(i, self.check_column, check_box) 
                #Add criteria description to 2nd column
                name_item = QTableWidgetItem()
                name_item.setText(str(criteria_recs[i][self.crit_name_column]))
                self.setItem(i, self.crit_name_column, name_item)
                #Add criteria type to 3rd column
                type_item = QTableWidgetItem()
                type_item.setText(str(criteria_recs[i][self.crit_type_column]))
                self.setItem(i, self.crit_type_column, type_item)
                #Add type options/units to 4th column
                type_item = QTableWidgetItem()
                type_item.setText(str(criteria_recs[i][self.crit_options_column]))
                self.setItem(i, self.crit_options_column, type_item)
                #Add cost/benefit to 5th column
                cb_item = QTableWidgetItem()
                cb_item.setText(str(criteria_recs[i][self.cost_benefit_column]))
                self.setItem(i, self.cost_benefit_column, cb_item)

                #self.resizeColumnsToContents()

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
        