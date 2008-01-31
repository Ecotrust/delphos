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
# $Id: InputMcaTableWidget.py 87 2007-10-12 22:56:41Z timw $
#
# @summary - 
#===============================================================================

import sys
import copy
#from util.log import *

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *
from delphos_exceptions import *

class InputResultViewTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 300 #criteria descriptions are so freaking long!
        #self.log = DelphosLog()

    def load(self, input_data_set):
        """Given list of alternative/criteria pair info and an input value for that 
        pair, loads a table widget with combo boxes and current value, if it exists.
        
        input values are qualitative (current option) or quantitative. Input is expected 
        to be legal, eg. drop down value given matches one of possible 
        [[altern_data][crit_data][row][col][value]]
        """ 
         
        self.clear()
        self.hide()    #Force size recalculation and layout when shown again
        self.num_cols = input_data_set.get_num_alterns()
        self.num_rows = input_data_set.get_num_crits()
        self.setColumnCount(self.num_cols)
        self.setRowCount(self.num_rows)
        
        #Create input widgets for every combination of alternative and criteria given
        crit_id = crit_name = crit_type = crit_options_units = cost_benefits = None
        altern_id = altern_name = None
        self.input_data = input_data_set
        #self.cell_data = input_data_set.get_cell_data()
                  
        for i in range(self.input_data.get_num_cells()):
            #Unpack input data set row
            (altern_data, crit_data, row, column, input_value) = self.input_data.get_cell_contents(i)
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
                    for option in crit_options_units:
                        option_name = option[0]
                        option_val = option[1]
                        if option_val == input_value:
                            #combo_box.addItem(option_name, QVariant(option_val))
                            self.set_cell_value(row, column, option_name)
                    #self.set_combo_value(row, column, crit_options_units, input_value)
                except InputError, e:
                    QMessageBox.critical(self, "Combo Box Error", unicode(e)+" Row"+unicode(row+1)+" '"+unicode(crit_name)+"', Column "+unicode(column+1)+" '"+unicode(altern_name)+"'")
                    return False
                
            elif crit_type == "Ratio":
                try:
                    self.set_cell_value(row, column, input_value)
                except InputError, e:
                    QMessageBox.critical(self, "Input Error", unicode(e)+" Row "+unicode(row+1)+" '"+unicode(crit_name)+"', Column "+unicode(column+1)+" '"+unicode(altern_name)+"'")
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
                    raise DelphosError, unicode(e)+" Row"+unicode(row+1)+": "+unicode(crit_name)+", Column "+unicode(column+1)+": "+unicode(altern_name)
                    return False
                
            elif crit_type == "Ratio":
                try:                    
                    value = self.get_cell_value(row, column)
                except InputError, e:
                    raise DelphosError, unicode(e)+" Row"+unicode(row+1)+": "+unicode(crit_name)+", Column "+unicode(column+1)+": "+unicode(altern_name)
                    return False
                
            if value == None and input_required:
                raise DelphosError, "Missing input for row "+unicode(row)+" '"+unicode(crit_name)+"', column "+unicode(column)+" '"+unicode(altern_name)+"'"

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
            raise InputError, "Unable to read input. Expected an integer, received: "+unicode(value)+"."
        #print "value: "+unicode(value)
        #print "ok: "+unicode(ok)   
        #Save the value from i,j to j,i
        return value
    
    def set_combo_value(self, row, column, crit_options_units, input_value):
        combo_box = QComboBox(self)
        for option in crit_options_units:
            option_name = option[0]
            option_val = option[1]
            combo_box.addItem(option_name, QVariant(option_val))
 
        if input_value:
            #print "input value: "+unicode(input_value)
            option_num = combo_box.findData(QVariant(input_value))
            #print "option num: "+unicode(option_num)
            if option_num < 0:
                raise InputError, "Invalid option ("+unicode(input_value)+")."
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
            raise InputError, "Invalid input. Expected an integer, received '"+unicode(value)+"'."           
        #print "value: "+unicode(value)
        #print "from i:"+unicode(i)+" j:"+unicode(j)
        #Save the value from i,j to j,i
        #print "into: i:"+unicode(j)+", j:"+unicode(i)
        return int(value)

    def set_cell_value(self, row, column, value=None):
        table_item = QTableWidgetItem("")
        table_item.setText(unicode(value))
        self.setItem(row, column, table_item)

if __name__ == "__main__":
    arr = initialize_int_array(2,4)
    print "blort"
    print arr