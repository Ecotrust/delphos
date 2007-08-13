import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *

class WeightMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.weight_column = 0
        self.vertical_header_width = 300 #criteria descriptions are so freaking long!
        
    def load(self, criteria_recs):
        """Loads the table with criteria, given a list of records
        """
        self.clearContents()
        self.num_rows = len(criteria_recs)
        self.setRowCount(self.num_rows)
        
        for i in range(self.num_rows):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = criteria_recs[i]
            #Add criteria name header 
            header_item = QTableWidgetItem()
            header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
            header_item.setText(crit_name)
            header_item.setToolTip(crit_name)
            self.setVerticalHeaderItem(i, header_item)
        #self.resizeColumnsToContents()
    
    def get_input_weights(self):
        """Returns list of indexes of criterias selected in table
        
        Can be used for lookup in list structure containing criterias data
        """
        input_weights = initialize_int_array(self.num_rows, 1)
        for i in range(self.num_rows):
            #Get value from table item
            table_item = self.item(i,0) 
            #print table_item
            value = table_item.text()
            #Check for no value
            if not value:
                QMessageBox.critical(self,"Error", "Missing input in row "+str(i+1))
                return None                
            #Check for non-integer
            if not strIsInt(value):
                QMessageBox.critical(self,"Error", "Invalid input in row "+str(i+1)+"\nExpected an integer, received '")
                return None                
            #print "value: "+str(value)
            #print "from i:"+str(i)+" j:"+str(j)
            #Save the value from i,j to j,i
            #print "into: i:"+str(j)+", j:"+str(i)
            input_weights[i] = int(value)
        return input_weights
        