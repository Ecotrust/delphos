import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class InputMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 300 #criteria descriptions are so freaking long!

    def load(self, selected_altern_data, selected_crit_data):        
        self.clear()
        self.hide()    #Force size recalculation and layout when shown again
        self.num_rows = len(selected_crit_data)
        self.num_cols = len(selected_altern_data)
        self.setRowCount(self.num_rows)
        self.setColumnCount(self.num_cols)
    
        #Create input widgets for every combination of alternative and criteria given
        crit_id = crit_name = crit_type = crit_options_units = cost_benefits = None
        altern_id = altern_name = None
        for i in range(len(selected_crit_data)):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = selected_crit_data[i]
            for j in range(len(selected_altern_data)):
                (altern_id, altern_name) = selected_altern_data[j]
                #Insert row headers 
                if i is 0:
                    header_item = QTableWidgetItem()
                    #header_item.setSizeHint(QSize(self.horizontal_header_width, header_item.sizeHint().height()))        
                    header_item.setText(altern_name)
                    header_item.setToolTip(altern_name)
                    self.setHorizontalHeaderItem(j, header_item)
                #Insert column headers
                if j is 0: 
                    header_item = QTableWidgetItem()
                    header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
                    header_item.setText(crit_name)
                    header_item.setToolTip(crit_name)
                    self.setVerticalHeaderItem(i, header_item)
                #Create and insert combo box
                if crit_type == "Ordinal" or crit_type == "Binary":
                    combo_box = QComboBox(self)
                    for option in crit_options_units:
                        option_name = option[0]
                        option_val = option[1]
                        combo_box.addItem(option_name, QVariant(option_val))
                    self.setCellWidget(i, j, combo_box)
                                        
        self.show()       
        
    def get_input(self, row, column):
        pass
    
    def get_current_row_items(self):
        pass
        