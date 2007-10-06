import sys
import copy

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *

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
        self.input_data = input_data_set.get_input_data()
        
        for i in range(len(self.input_data)):
            #Unpack input data set row
            (altern_data, crit_data, row, column, input_value) = self.input_data[i]
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
                        QMessageBox.critical(self,"Error", "Invalid option ("+str(input_value)+") given in row "+str(row+1)+", column "+str(column+1))
                        return False
                    else:
                        combo_box.setCurrentIndex(option_num)
                self.setCellWidget(row, column, combo_box)
            elif crit_type == "Ratio":
                table_item = QTableWidgetItem("")
                if input_value:
                    table_item.setText(input_value)
                self.setItem(row, column, table_item)
                                        
        self.show()
        return True      
        
    def get_input_data(self, input_required, new_input_data=None):
        """Returns a new InputDataSet with updated values
        """
        #input_data = initialize_int_array(self.num_rows, self.num_cols)  #Note reversal, see note above
        input_data = new_input_data.get_input_data()
        for i in range(len(input_data)):
            #Unpack input data set row
            (altern_data, crit_data, row, column, input_value) = input_data[i]
            #Unpack altern data
            (altern_id, altern_name, altern_color) = altern_data       
            #Unpack crit data
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data  
                
            value = 0
            if crit_type == "Ordinal" or crit_type == "Binary":
                value = self.get_combo_value(row, column)
            elif crit_type == "Ratio":
                value = self.get_cell_value(row, column)
            new_input_data.set_value(i, value)
            print new_input_data
        return new_input_data

    def get_combo_value(self, row, column):
        #Get value from combo box
        cell_widget = self.cellWidget(row, column)
        #print cell_widget
        if not cell_widget:
            QMessageBox.critical(self,"Error", "Unable to access combo box for criteria row'"+unicode(crit_name)+"', alternative column '"+altern_name+"'")
        (value, ok) = cell_widget.itemData(cell_widget.currentIndex()).toInt()
        if not value and input_required:
            QMessageBox.critical(self,"Input Error", "Missing input in row "+str(row+1)+", column "+str(column+1))
            return None 
        if not ok:
            QMessageBox.critical(self,"Error", "Unable to read input for criteria row'"+unicode(crit_name)+"', alternative column '"+altern_name+"'\nExpected an integer, received '"+value+"'")
        #print "value: "+str(value)
        #print "ok: "+str(ok)   
        #Save the value from i,j to j,i
        return value
    
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
            QMessageBox.critical(self,"Error", "Missing input for alternative '"+unicode(crit_name)+"', criteria '"+crit_name+"'")
            return None                
        #Check for non-integer
        if not strIsInt(value):
            QMessageBox.critical(self,"Error", "Invalid input for alternative '"+unicode(altern_name)+"', criteria '"+crit_name+"'\nExpected an integer, received '"+value+"'")               
        #print "value: "+str(value)
        #print "from i:"+str(i)+" j:"+str(j)
        #Save the value from i,j to j,i
        #print "into: i:"+str(j)+", j:"+str(i)
        return int(value)

if __name__ == "__main__":
    arr = initialize_int_array(2,4)
    print "blort"
    print arr