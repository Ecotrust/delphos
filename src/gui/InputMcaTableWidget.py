import sys
import copy

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *
from delphos_exceptions import *

class InputMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 300 #criteria descriptions are so freaking long!

    def load(self, input_data_set):
        """Given list of alternative/criteria pair info and an input value for that 
        pair, loads a table widget with combo boxes and current value, if it exists.
        
        input values are qualitative (current option) or quantitative. Input is expected 
        to be legal, eg. drop down value given matches one of possible 
        [[altern_data][crit_data][row][col][value]]
        """ 
         
        self.clear()
        self.hide()    #Force size recalculation and layout when shown again
        self.num_cols = input_data_set.num_alterns
        self.num_rows = input_data_set.num_crits
        self.setColumnCount(self.num_cols)
        self.setRowCount(self.num_rows)
    
        #Create input widgets for every combination of alternative and criteria given
        crit_id = crit_name = crit_type = crit_options_units = cost_benefits = None
        altern_id = altern_name = None
        self.cell_data = input_data_set.get_cell_data()
                  
        for i in range(len(self.cell_data)):
            #Unpack input data set row
            (altern_data, crit_data, row, column, input_value) = self.cell_data[i]
            #Unpack altern data
            (altern_id, altern_name, altern_color) = altern_data            
            #Unpack crit data
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data
                        
            #Insert row headers 
            if row is 0:
                header_item = QTableWidgetItem()
                #header_item.setSizeHint(QSize(self.horizontal_header_width, header_item.sizeHint().height()))        
                header_item.setText(altern_name)
                header_item.setToolTip(altern_name)
                self.setHorizontalHeaderItem(column, header_item)
            #Insert column headers
            if column is 0: 
                header_item = QTableWidgetItem()
                header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
                header_item.setText(crit_name)
                header_item.setToolTip(crit_name)
                self.setVerticalHeaderItem(row, header_item)

            #Create and insert combo box
            if crit_type == "Ordinal" or crit_type == "Binary":
                try:
                    self.set_combo_value(row, column, crit_options_units, input_value)
                except InputError, e:
                    QMessageBox.critical(self, "Combo Box Error", str(e)+" Row"+str(row+1)+" '"+str(crit_name)+"', Column "+str(column+1)+" '"+str(altern_name)+"'")
                    return False
                
            elif crit_type == "Ratio":
                try:
                    self.set_cell_value(row, column, input_value)
                except InputError, e:
                    QMessageBox.critical(self, "Input Error", str(e)+" Row "+str(row+1)+" '"+str(crit_name)+"', Column "+str(column+1)+" '"+str(altern_name)+"'")
                    return False        
        self.show()
        return True      
        
    def get_input_data(self, input_required, new_input_data=None):
        """Returns a new InputDataSet with updated values
        """
        #Get and traverse input data
        cell_data = new_input_data.get_cell_data()
        for i in range(len(cell_data)):
            #Unpack input data set row
            (altern_data, crit_data, row, column, input_value) = cell_data[i]
            #Unpack altern data
            (altern_id, altern_name, altern_color) = altern_data       
            #Unpack crit data
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data  
        
            value = 0
            if crit_type == "Ordinal" or crit_type == "Binary":
                try:
                    value = self.get_combo_value(row, column)
                except InputError, e:
                    raise DelphosError, str(e)+" Row"+str(row+1)+": "+str(crit_name)+", Column "+str(column+1)+": "+str(altern_name)
                    return False
                
            elif crit_type == "Ratio":
                try:                    
                    value = self.get_cell_value(row, column)
                except InputError, e:
                    raise DelphosError, str(e)+" Row"+str(row+1)+": "+str(crit_name)+", Column "+str(column+1)+": "+str(altern_name)
                    return False
                
            if value == None and input_required:
                raise DelphosError, "Missing input for row "+str(row)+" '"+str(crit_name)+"', column "+str(column)+" '"+str(altern_name)+"'"

            new_input_data.set_value(i, value)
        return new_input_data

    def get_combo_value(self, row, column):
        #Get value from combo box
        cell_widget = self.cellWidget(row, column)
        #print cell_widget
        if not cell_widget:
            raise InputError, "Unable to access combo box."
        (value, ok) = cell_widget.itemData(cell_widget.currentIndex()).toInt()
        if not value and input_required:
            raise InputError, "Missing input."
        if not ok:
            raise InputError, "Unable to read input. Expected an integer, received: "+str(value)+"."
        #print "value: "+str(value)
        #print "ok: "+str(ok)   
        #Save the value from i,j to j,i
        return value
    
    def set_combo_value(self, row, column, crit_options_units, input_value):
        combo_box = QComboBox(self)
        for option in crit_options_units:
            option_name = option[0]
            option_val = option[1]
            combo_box.addItem(option_name, QVariant(option_val))
 
        if input_value:
            #print "input value: "+str(input_value)
            option_num = combo_box.findData(QVariant(input_value))
            #print "option num: "+str(option_num)
            if option_num < 0:
                raise InputError, "Invalid option ("+str(input_value)+")."
            else:
                combo_box.setCurrentIndex(option_num)
        self.setCellWidget(row, column, combo_box)
    
    
    def get_cell_value(self, row, column):
        #Get value from table item
        table_item = self.item(row,column) 
        #print table_item
        value = table_item.text()
        #Check for no value
        if not value:
            #print i
            #print j
            #print crit_names
            #print altern_names
            return None       
        #Check for non-integer
        if not strIsInt(value):
            raise InputError, "Invalid input. Expected an integer, received '"+str(value)+"'."           
        #print "value: "+str(value)
        #print "from i:"+str(i)+" j:"+str(j)
        #Save the value from i,j to j,i
        #print "into: i:"+str(j)+", j:"+str(i)
        return int(value)

    def set_cell_value(self, row, column, value=None):
        table_item = QTableWidgetItem("")
        if strIsInt(value):
            table_item.setText(str(value))
        self.setItem(row, column, table_item)

if __name__ == "__main__":
    arr = initialize_int_array(2,4)
    print "blort"
    print arr