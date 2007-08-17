import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *

class InputMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 300 #criteria descriptions are so freaking long!

    def load(self, selected_altern_data, selected_crit_data, input_data=None):
        """Given alternative and criteria data (w/ options), loads
        a table widget with the necessary table widget items and
        combo boxes
        
        Optionally, takes a 2D list containing values to use in setting
        up the widget (integer item value or integer drop down value).  
        Can be used after importing external data.  Input is expected to be
        legal, eg. drop down value given matches one of possible 
        """ 
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
                        
                    if input_data:
                        #set to given input val
                        input_val = input_data[i][j]
                        #print "input val: "+str(input_val)
                        option_num = combo_box.findData(QVariant(input_val))
                        #print "option num: "+str(option_num)
                        if option_num < 0:
                            QMessageBox.critical(self,"Error", "Invalid option ("+str(input_val)+") given in row "+str(i+1)+", column "+str(j+1))
                            return False
                        else:
                            combo_box.setCurrentIndex(option_num)
                    self.setCellWidget(i, j, combo_box)
                elif crit_type == "Ratio":
                    table_item = QTableWidgetItem("")
                    if input_data:
                        table_item.setText(input_data[i][j])
                    self.setItem(i, j, table_item)
                                        
        self.show()
        return True      
        
    def get_input_data(self, altern_names, crit_names):
        """Returns a 2D list of input values (integers) for use in MCA
        
        Note the resulting list is transposed as the input table is crit x altern and the
        algorithm expects altern x crit
        """ 
        #Initialize with opposite dimensions, need to load transposed for input into algorithm
        input_data = initialize_int_array(self.num_cols, self.num_rows)  #Note reversal, see note above
        for i in range(len(self.selected_crit_data)):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = self.selected_crit_data[i]
            for j in range(len(self.selected_altern_data)):
                (altern_id, altern_name) = self.selected_altern_data[j]
                if crit_type == "Ordinal" or crit_type == "Binary":
                    #Get value from combo box
                    cell_widget = self.cellWidget(i,j)
                    #print cell_widget
                    if not cell_widget:
                        QMessageBox.critical(self,"Error", "Unable to access combo box for criteria row'"+unicode(crit_names[i])+"', alternative column '"+altern_names[j]+"'")
                    (value, ok) = cell_widget.itemData(cell_widget.currentIndex()).toInt()
                    if not ok:
                        QMessageBox.critical(self,"Error", "Unable to read input for criteria row'"+unicode(crit_names[i])+"', alternative column '"+altern_names[j]+"'\nExpected an integer, received '"+value+"'")
                    #print "value: "+str(value)
                    #print "ok: "+str(ok)   
                    #Save the value from i,j to j,i
                    input_data[j][i] = value
                elif crit_type == "Ratio":
                    #Get value from table item
                    table_item = self.item(i,j) 
                    #print table_item
                    value = table_item.text()
                    #Check for no value
                    if not value:
                        print i
                        print j
                        print crit_names
                        print altern_names
                        QMessageBox.critical(self,"Error", "Missing input for alternative '"+unicode(altern_names[j])+"', criteria '"+crit_names[i]+"'")
                        return None                
                    #Check for non-integer
                    if not strIsInt(value):
                        QMessageBox.critical(self,"Error", "Invalid input for alternative '"+unicode(altern_names[j])+"', criteria '"+crit_names(i)+"'\nExpected an integer, received '"+value+"'")               
                    #print "value: "+str(value)
                    #print "from i:"+str(i)+" j:"+str(j)
                    #Save the value from i,j to j,i
                    #print "into: i:"+str(j)+", j:"+str(i)
                    input_data[j][i] = int(value)
        return input_data

if __name__ == "__main__":
    arr = initialize_int_array(2,4)
    print "blort"
    print arr