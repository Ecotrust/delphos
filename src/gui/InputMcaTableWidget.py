import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class InputMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)

    def load(self, altern_data, crit_data, altern_ids, crit_ids):
        print altern_data
        print crit_data
        print altern_ids
        print crit_ids
        
        self.clear()
        self.hide()    #Force size recalculation and layout when shown again
        self.num_rows = len(crit_ids)
        self.num_cols = len(altern_ids)
        self.setRowCount(self.num_rows)
        self.setColumnCount(self.num_cols)

        #Load top headers
        horizontal_labels = []
        for i in range(len(altern_ids)):
            horizontal_labels.append("Altern "+str(i))
        self.setHorizontalHeaderLabels(horizontal_labels)

        #Load row headers
        vertical_labels = []
        for i in range(len(crit_ids)):
            vertical_labels.append("Crit "+str(i))
        self.setVerticalHeaderLabels(vertical_labels)
    
        #Load input widgets
        for i in range(len(crit_ids)):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data[i]
            for j in range(len(altern_ids)):
                if crit_type == "Ordinal":
                    combo_item = QComboBox()
                    text = crit_options_units[0]
                    print combo_item
                    print "inserting: "+text
                    combo_item.insertItem(0, text)
                    print "is it in?: "+combo_item.itemText(0)
                    self.setCellWidget(i, j, combo_item)                    
                #item = QTableWidgetItem()
                #item.setText(str(crit_id))
                #self.setItem(i, j, item)
        
        self.show()       
    
    def get_current_row_items(self):
        pass
        