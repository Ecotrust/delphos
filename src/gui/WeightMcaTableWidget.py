#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
# @license		GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id$
#
# @summary - 
#===============================================================================

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
        
    def load(self, input_weight_set):
        """Loads the table with criteria, given a set of input weight data
        """
        weight_recs = input_weight_set.get_weight_data()
        self.hide()
        self.clearContents()
        self.num_rows = len(weight_recs)    
        self.setRowCount(self.num_rows)
        
        for i in range(self.num_rows):
            (crit_id, crit_name, crit_weight) = weight_recs[i]
            #Add criteria name header 
            header_item = QTableWidgetItem()
            header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
            header_item.setText(crit_name)
            header_item.setToolTip(crit_name)
            self.setVerticalHeaderItem(i, header_item)
            weight_item = QTableWidgetItem()
            if crit_weight:
                weight_item.setText(str(crit_weight))
            self.setItem(i, 0, weight_item)
            
        #self.resizeColumnsToContents()
        self.show()
    
    def assign_equal_weight(self):
        for i in range(self.num_rows):
            table_item = self.item(i, 0)
            if not table_item:
                QMessageBox.critical(self,"Error", "Error reading from row "+str(i+1))
                return None 
            table_item.setText("1")
    
    def get_input_weights(self, input_required):
        """Returns list of indexes of criterias selected in table
        
        Can be used for lookup in list structure containing criterias data
        """
        input_weights = initialize_int_array(self.num_rows, 1)
        for i in range(self.num_rows):
            #Get value from table item
            table_item = self.item(i,0) 
            if not table_item:
                QMessageBox.critical(self,"Error", "Error reading from row "+str(i+1))
                return None  
            #print table_item
            value = table_item.text()
            #Check for no value
            if not value and input_required:
                QMessageBox.critical(self,"Error", "Missing input in row "+str(i+1))
                return None                
            #Check for non-integer
            if value and not strIsInt(value):
                QMessageBox.critical(self,"Error", "Invalid input in row "+str(i+1)+"\nExpected an integer, received "+str(value))
                return None                
            #print "value: "+str(value)
            #print "from i:"+str(i)+" j:"+str(j)
            #Save the value from i,j to j,i
            #print "into: i:"+str(j)+", j:"+str(i)
            if value:
                input_weights[i] = int(value)
            else:
                input_weights[i] = None
        return input_weights
        