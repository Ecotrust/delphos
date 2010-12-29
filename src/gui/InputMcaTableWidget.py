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
import copy

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *
from delphos_exceptions import *

class InputMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 400 #criteria descriptions are so freaking long!
        self.retranslate() #Translate the UI

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
                
                if cost_benefit == 'C':
                    cb_text = 'Cost'
                else:
                    cb_text = 'Benefit'
                
                crit_text = ""

                for option in crit_options_units:
                    crit_text = crit_text+'"'+option[0]+'" '
                                            
                tool_text = self.tool_desc+" "+crit_name+"\n"+self.tool_crit+" "+crit_type+"\n"+self.tool_opt+" "+crit_text+"\n"+cb_text                    
                header_item.setToolTip(tool_text)
                    
                self.setVerticalHeaderItem(row, header_item)

            #Create and insert combo box
            if crit_type == "Ordinal" or crit_type == "Binary":
                try:
                    self.set_combo_value(row, column, crit_options_units, input_value)
                except InputError, e:
                    QMessageBox.critical(self, self.combo_error_text, unicode(e)+self.missing_invalid_text+" "+unicode(row+1)+" '"+unicode(crit_name)+"', "+self.combo_column+" "+unicode(column+1)+" '"+unicode(altern_name)+"'")
                    return False
                
            elif crit_type == "Ratio":
                try:
                    self.set_cell_value(row, column, input_value)
                except InputError, e:
                    QMessageBox.critical(self, self.input_error_text, unicode(e)+" "+unicode(row+1)+" '"+unicode(crit_name)+"', "+self.combo_column+" "+unicode(column+1)+" '"+unicode(altern_name)+"'")
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
                    value = self.get_combo_value(row, column, input_required)
                except InputError, e:
                    raise DelphosError, unicode(e)+self.missing_invalid_text+unicode(row+1)+": "+unicode(crit_name)+", "+self.combo_column+" "+unicode(column+1)+": "+unicode(altern_name)+". "+self.input_required_text
                    return False
                
            elif crit_type == "Ratio":
                try:                    
                    value = self.get_cell_value(row, column)
                except InputError, e:
                    raise DelphosError, unicode(e)+self.ratio_error_text+" "+unicode(row+1)+": "+unicode(crit_name)+", "+self.combo_column+" "+unicode(column+1)+": "+unicode(altern_name)+". "+self.input_required_text
                    return False
                
            if value == None and input_required:
                raise DelphosError, self.missing_invalid_text+" "+unicode(row)+" '"+unicode(crit_name)+"', "+self.combo_column+" "+unicode(column)+" '"+unicode(altern_name)+"'"

            new_input_data.set_value(i, value)
        return new_input_data

    def get_combo_value(self, row, column, input_required):
        #Get value from combo box
        cell_widget = self.cellWidget(row, column)
        #print cell_widget
        if not cell_widget:
            raise InputError, self.combo_access_error
        (value, ok) = cell_widget.itemData(cell_widget.currentIndex()).toInt()
        if not value and input_required:
            raise InputError, self.missing_text+" "+unicode(row)+", "+self.combo_column+" "+unicode(column)
        if not ok and input_required:
            raise InputError, self.non_integer_error+" "+unicode(value)
        #print "value: "+unicode(value)
        #print "ok: "+unicode(ok)   
        #Save the value from i,j to j,i
        return value
    
    def set_combo_value(self, row, column, crit_options_units, input_value):
        combo_box = QComboBox(self)
        combo_box.addItem("")
        for option in crit_options_units:
            option_name = option[0]
            option_val = option[1]
            combo_box.addItem(option_name, QVariant(option_val))
 
        if input_value:
            #print "input value: "+unicode(input_value)
            option_num = combo_box.findData(QVariant(input_value))
            #print "option num: "+unicode(option_num)
            if option_num < 0:
                raise InputError, self.invalid_option_text+unicode(input_value)
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
            raise InputError, self.non_integer_error+unicode(value)
        #print "value: "+unicode(value)
        #print "from i:"+unicode(i)+" j:"+unicode(j)
        #Save the value from i,j to j,i
        #print "into: i:"+unicode(j)+", j:"+unicode(i)
        return int(value)

    def set_cell_value(self, row, column, value=None):
        table_item = QTableWidgetItem("")
        if strIsInt(value):
            table_item.setText(unicode(value))
        self.setItem(row, column, table_item)

    def retranslate(self):
        self.tool_desc = QApplication.translate("InputMcaTableWidget", "Description:", "part of tooltip", QApplication.UnicodeUTF8)
        self.tool_crit = QApplication.translate("InputMcaTableWidget", "Criteria Type:", "part of tooltip", QApplication.UnicodeUTF8)
        self.tool_opt = QApplication.translate("InputMcaTableWidget", "Options/Units:", "part of tooltip", QApplication.UnicodeUTF8)
        self.combo_error_text = QApplication.translate("InputMcaTableWidget", "Combo Error", "error name", QApplication.UnicodeUTF8)
        self.combo_row = QApplication.translate("InputMcaTableWidget", "Row", "", QApplication.UnicodeUTF8)
        self.combo_column = QApplication.translate("InputMcaTableWidget", "Column", "", QApplication.UnicodeUTF8)
        self.input_error_text = QApplication.translate("InputMcaTableWidget", "Input Error", "error name", QApplication.UnicodeUTF8)
        self.missing_invalid_text = QApplication.translate("InputMcaTableWidget", "Missing or Invalid input in Row", "", QApplication.UnicodeUTF8)
        self.ratio_error_text = QApplication.translate("InputMcaTableWidget", "Ratio value must be greater than zero in Row", "", QApplication.UnicodeUTF8)
        self.missing_text = QApplication.translate("InputMcaTableWidget", "Missing input for row", "", QApplication.UnicodeUTF8)
        self.combo_access_error = QApplication.translate("InputMcaTableWidget", "Unable to access combo box", "", QApplication.UnicodeUTF8)
        self.non_integer_error = QApplication.translate("InputMcaTableWidget", "Invalid input, expected an integer but found:", "", QApplication.UnicodeUTF8)
        self.invalid_option_text = QApplication.translate("InputMcaTableWidget", "Invalid option:", "", QApplication.UnicodeUTF8)        
        self.input_required_text = "Input is required for each cell in order to perform analysis"
        
if __name__ == "__main__":
    arr = initialize_int_array(2,4)
    print "blort"
    print arr
    
    