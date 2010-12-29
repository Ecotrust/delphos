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
# $Id: $
#
# @summary - Table widget for viewing, inputting and editing global input data
# for a project.  Missing cell data is allowed.  The table is reloaded every time
# the tab its in is loaded, guaranteeing it matches the current state of the
# project as far as which alternatives and criteria are defined.
#===============================================================================

import sys
import copy

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *
from delphos_exceptions import *

class InputGlobalTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.vertical_header_width = 400 #criteria descriptions are so freaking long!
        self.loaded = False
        self.retranslate() #Translate the UI

    def load(self, altern_data, crit_data, input_data):
        """Given altern, crit and input table data, loads a table widget with combo boxes 
        and stored values, if they exist.
        
        input values are qualitative (current option #) or quantitative (positive integer). 
        Input is expected to be legal, eg. drop down option # given matches one of possible. 
        """ 
        
        #Store for use in retrieval process
        self.altern_data = altern_data
        self.crit_data = crit_data
        self.input_data = input_data
            
        self.clear()
        self.hide()    #Force size recalculation and layout when shown again
        self.num_cols = len(altern_data)
        self.num_rows = len(crit_data)
        self.setColumnCount(self.num_cols)
        self.setRowCount(self.num_rows)
        
        self.loaded = True
        
        #Create input widgets for every combination of alternative and criteria given
        crit_id = crit_name = crit_type = crit_options_units = cost_benefits = None
        altern_id = altern_name = None
        self.input_data = input_data

        for i in range(self.num_rows):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data[i]
            row = i
            for j in range(self.num_cols):
                (altern_id, altern_name, altern_color) = altern_data[j]
                column = j                   
                
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

                #Get input value
                input_value = ""
                for input_row in input_data:
                    cur_altern_id = input_row[0]
                    cur_crit_id = input_row[1]
                    if altern_id == cur_altern_id and crit_id == cur_crit_id:
                        input_value = input_row[2]
                         
                #Create and insert combo box
                if crit_type == "Ordinal" or crit_type == "Binary":
                    try:
                        self.set_combo_value(row, column, crit_options_units, input_value)
                    except InputError, e:
                        QMessageBox.critical(self, self.combo_error_text, unicode(e)+" "+self.combo_row+unicode(row+1)+" '"+unicode(crit_name)+"', "+self.combo_column+" "+unicode(column+1)+" '"+unicode(altern_name)+"'")
                        return False
                    
                elif crit_type == "Ratio":
                    try:
                        self.set_cell_value(row, column, input_value)
                    except InputError, e:
                        QMessageBox.critical(self, self.input_error_text, unicode(e)+" "+self.combo_row+unicode(row+1)+" '"+unicode(crit_name)+"',"+self.combo_column+" "+unicode(column+1)+" '"+unicode(altern_name)+"'")
                        return False        
        self.show()
        QObject.connect(self,QtCore.SIGNAL("itemChanged(QTableWidgetItem*)"), self.input_change)
        return True      

    def set_input_data(self, input_data):
        """Used after a save"""
        self.input_data = input_data

    def get_input_vals(self, input_required=False):
        """Get input values from table and return as 2D list"""
        new_input_vals = initialize_int_array(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = self.crit_data[i]
            row = i
            for j in range(self.num_cols):
                (altern_id, altern_name, altern_color) = self.altern_data[j]
                column = j
   
                value = 0
                if crit_type == "Ordinal" or crit_type == "Binary":
                    try:
                        value = self.get_combo_value(row, column)
                    except InputError, e:
                        raise DelphosError, unicode(e)+self.missing_invalid_text+unicode(row+1)+": "+unicode(crit_name)+", "+self.combo_column+" "+unicode(column+1)+": "+unicode(altern_name)
                        return False 
                    
                elif crit_type == "Ratio":
                    try:                    
                        value = self.get_cell_value(row, column)
                    except InputError, e:
                        raise DelphosError, unicode(e)+self.missing_invalid_text+unicode(row+1)+": "+unicode(crit_name)+", "+self.combo_column+" "+unicode(column+1)+": "+unicode(altern_name)
                        return False
                    else:
                        if value is not None and value < 0:
                            raise DelphosError, self.ratio_error_text+unicode(row+1)+": "+unicode(crit_name)+", "+self.combo_column+" "+unicode(column+1)+": "+unicode(altern_name)
                            return False
    
                if value == None and input_required:
                    raise DelphosError, self.missing_text+" "+unicode(row)+" '"+unicode(crit_name)+"', "+self.combo_column+" "+unicode(column)+" '"+unicode(altern_name)+"'"
    
                new_input_vals[row][column] = value
        return new_input_vals

    def save_input_data(self, input_required=False):
        """Validates input and signals with changed input cell values.  
        
        update_input_value signal is sent for each cell that is changed.
        """
        if not self.crit_data or not self.altern_data:
            return False

        try:
            new_input_vals = self.get_input_vals(input_required)
        except DelphosError, e:
            QMessageBox.critical(self,self.input_error_text, unicode(e.value))
            return False
        else:
            #Traverse again updating each cell value in DB and creating new input_set
            for i in range(self.num_rows):
                (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = self.crit_data[i]
                row = i
                for j in range(self.num_cols):
                    (altern_id, altern_name, altern_color) = self.altern_data[j]
                    column = j
    
                    new_value = new_input_vals[row][column]
                    self.emit(SIGNAL("update_input_value"), altern_id, crit_id, new_value)
        return True
        
    def get_combo_value(self, row, column):
        #Get value from combo box
        cell_widget = self.cellWidget(row, column)
        #print cell_widget

        if not cell_widget:
            raise InputError, self.combo_access_error
        (value, ok) = cell_widget.itemData(cell_widget.currentIndex()).toInt()
        if not value:
            return None
        if not ok:
            raise InputError, self.non_integer_error+" "+unicode(value)

        #Save the value from i,j to j,i
        return value
    
    #Insert combo in row column given, with options given, defaulting to input_value
    def set_combo_value(self, row, column, crit_options_units, input_value):
        combo_box = QComboBox(self)
        #Add blank option
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
                raise InputError, self.invalid_option_text+" "+unicode(input_value)+")."
            else:
                combo_box.setCurrentIndex(option_num)
        self.setCellWidget(row, column, combo_box)
        QObject.connect(combo_box,QtCore.SIGNAL("currentIndexChanged(int)"), self.input_change)
    
    def input_change(self):
        self.emit(SIGNAL("input_changed"))

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
            raise InputError, self.non_integer_error+" "+unicode(value)
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
        self.tool_desc = QApplication.translate("InputGlobalTableWidget", "Description:", "part of tooltip", QApplication.UnicodeUTF8)
        self.tool_crit = QApplication.translate("InputGlobalTableWidget", "Criteria Type:", "part of tooltip", QApplication.UnicodeUTF8)
        self.tool_opt = QApplication.translate("InputGlobalTableWidget", "Options/Units:", "part of tooltip", QApplication.UnicodeUTF8)
        self.combo_error_text = QApplication.translate("InputGlobalTableWidget", "Combo Error", "error name", QApplication.UnicodeUTF8)
        self.combo_row = QApplication.translate("InputGlobalTableWidget", "Row", "", QApplication.UnicodeUTF8)
        self.combo_column = QApplication.translate("InputGlobalTableWidget", "Column", "", QApplication.UnicodeUTF8)
        self.input_error_text = QApplication.translate("InputGlobalTableWidget", "Input Error", "error name", QApplication.UnicodeUTF8)
        self.missing_invalid_text = QApplication.translate("InputGlobalTableWidget", "Missing or Invalid input in Row", "", QApplication.UnicodeUTF8)
        self.ratio_error_text = QApplication.translate("InputGlobalTableWidget", "Ratio value must be greater than zero in Row", "", QApplication.UnicodeUTF8)
        self.missing_text = QApplication.translate("InputGlobalTableWidget", "Missing input for row", "", QApplication.UnicodeUTF8)
        self.combo_access_error = QApplication.translate("InputGlobalTableWidget", "Unable to access combo box", "", QApplication.UnicodeUTF8)
        self.non_integer_error = QApplication.translate("InputGlobalTableWidget", "Invalid input, expected an integer but found:", "", QApplication.UnicodeUTF8)
        self.invalid_option_text = QApplication.translate("InputGlobalTableWidget", "Invalid option:", "", QApplication.UnicodeUTF8)