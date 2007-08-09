import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from common_functions import *

class InputMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 300 #criteria descriptions are so freaking long!

    def load(self, selected_altern_data, selected_crit_data):
        self.selected_altern_data = selected_altern_data
        self.selected_crit_data = selected_crit_data  
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
                elif crit_type == "Ratio":
                    table_item = QTableWidgetItem("")
                    self.setItem(i, j, table_item)
                                        
        self.show()       
        
    def get_input_data(self):
        """Returns a 2D list of input values (integers) for use in MCA
        """ 
        input_data = initialize_int_array(self.num_rows, self.num_cols)
        for i in range(len(self.selected_crit_data)):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = self.selected_crit_data[i]
            for j in range(len(self.selected_altern_data)):
                (altern_id, altern_name) = self.selected_altern_data[j]
                #print "i:"+str(i)+" j:"+str(j)
                if crit_type == "Ordinal" or crit_type == "Binary":
                    #Get value from combo box
                    cell_widget = self.cellWidget(i,j)
                    #print cell_widget
                    (value, ok) = cell_widget.itemData(cell_widget.currentIndex()).toInt()
                    if not ok:
                        QMessageBox.critical(self,"Error", "Unable to read input in row "+str(i+1)+", column "+str(j+1)+"\nExpected an integer, received '"+value+"'")
                    #print "value: "+str(value)
                    #print "ok: "+str(ok)   
                    #Save the value                                     
                    input_data[i][j] = value
                elif crit_type == "Ratio":
                    #Get value from table item
                    table_item = self.item(i,j) 
                    #print table_item
                    value = table_item.text()
                    #Check for no value
                    if not value:
                        QMessageBox.critical(self,"Error", "Missing input. row "+str(i+1)+", column "+str(j+1))
                        return None                
                    #Check for non-integer
                    if not strIsInt(value):
                        QMessageBox.critical(self,"Error", "Invalid input in row "+str(i+1)+", column "+str(j+1)+"\nExpected an integer, received '"+value+"'")
                        return None                
                    print "value: "+str(value)
                    #Save the value
                    input_data[i][j] = int(value)
        return input_data
    
    def get_current_row_items(self):
        pass

if __name__ == "__main__":
    arr = initialize_int_array(2,4)
    print "blort"
    print arr