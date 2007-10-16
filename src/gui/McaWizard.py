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

import os
import re
import copy
from sets import Set
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from mca_wizard_ui import Ui_McaWizard
from util.common_functions import *
from util.latin_csv import *

class McaWizard(QDialog, Ui_McaWizard):
    """Manages the collection of MCA analysis input
    
    Optionally takes input from a previous MCA analysis run
    """
    def __init__(self, gui_manager, parent, project, prev_run_data=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.project = project
        self.gui_manager = gui_manager
        self.isError = False    #Error flag for form processing
        self.errorMsg = ""
        self.default_template_extension = "csv"
        self.output_encoding = 'latin-1'
        self.cur_index = 0
        
        self.input_data = None
        self.input_weights = None
        
        #Contains field data for all alternatives selected, each row is a 
        #list of [altern_id, altern_name]
        self.selected_altern_data = []
        self.selected_altern_ids = []
        self.selected_altern_names = []
        self.num_selected_alternatives = 0
        self.altern_id_column = 0 # in altern_data type list
        self.altern_name_column = 1    #in altern_data type list
        
        #Contains field data for all criteria selected, each row is a
        #list of [crit_id, crit_name, crit_type, crit_options, crit_cost_benefit]
        self.selected_crit_data = []
        self.selected_crit_ids = []
        self.selected_crit_names = []
        self.num_selected_criteria = 0
        self.crit_id_column = 0
        self.crit_name_column = 1
        self.crit_type_column = 2
        self.crit_options_column = 3
        
        #Button Signals
        QObject.connect(self.altern_next_button,QtCore.SIGNAL("clicked()"), self.process_altern_select)
        QObject.connect(self.crit_next_button,QtCore.SIGNAL("clicked()"), self.process_crit_select)
        QObject.connect(self.input_next_button,QtCore.SIGNAL("clicked()"), self.process_data_input)
        
        QObject.connect(self.crit_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
        QObject.connect(self.input_prev_button,QtCore.SIGNAL("clicked()"), self.input_prev_click)
        QObject.connect(self.weight_prev_button,QtCore.SIGNAL("clicked()"), self.weight_prev_click)
                    
        QObject.connect(self.altern_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.crit_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.input_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
        QObject.connect(self.weight_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)

        QObject.connect(self.check_all_altern_button,QtCore.SIGNAL("clicked()"), self.check_all_alternatives)
        QObject.connect(self.check_all_criteria_button,QtCore.SIGNAL("clicked()"), self.check_all_criteria)
        QObject.connect(self.uncheck_all_altern_button,QtCore.SIGNAL("clicked()"), self.uncheck_all_alternatives)
        QObject.connect(self.uncheck_all_criteria_button,QtCore.SIGNAL("clicked()"), self.uncheck_all_criteria)
        QObject.connect(self.equal_weight_button,QtCore.SIGNAL("clicked()"), self.assign_equal_weight)        
        QObject.connect(self.export_button,QtCore.SIGNAL("clicked()"), self.process_template_export)
        QObject.connect(self.import_button,QtCore.SIGNAL("clicked()"), self.process_template_import)        
        QObject.connect(self.run_analysis_button,QtCore.SIGNAL("clicked()"), self.process_run)
        
        #Other signals
        QObject.connect(self.mca_stack,QtCore.SIGNAL("currentChanged(int)"), self.process_current_change)
        
        if prev_run_data:
            (prev_run_id, prev_run_name, prev_run_description, prev_altern_data, prev_crit_data, prev_input_data, prev_input_weights, prev_results, prev_creation_date) = prev_run_data
            self.altern_data = prev_altern_data        
            self.crit_data = prev_crit_data

        self.setup_crit_select()        
        self.setup_altern_select()
        
        if prev_run_data:
        	#Load up the wizard dialogs
            self.check_all_alternatives()
            self.process_altern_select()
            
            self.check_all_criteria()
            self.process_crit_select()
            
            self.setup_data_input()
            self.input_data.load_mca_input(prev_input_data)
            self.input_table.load(self.input_data)
            self.process_data_input()
            
            self.setup_weight_input()
            self.input_weights.update_weights(prev_input_weights)
            self.weight_table.load(self.input_weights)
            self.process_weight_input()

    #################################### Alternatives #####################

    def setup_altern_select(self):
        if not self.altern_data:
            self.altern_data = self.project.get_all_alternatives()
        self.altern_table.load(self.altern_data) 
        
    def process_altern_select(self):
        selected_altern_indexes = self.altern_table.get_selected_indexes()
        self.selected_altern_data = []
        self.selected_altern_ids = []
        self.selected_altern_names = []
        
        if len(selected_altern_indexes) < 2:
            QMessageBox.critical(self,"Error", "You must select at least two alternatives")
        else:
            for index in selected_altern_indexes:
                self.selected_altern_data.append(self.altern_data[index])
                self.selected_altern_ids.append(self.altern_data[index][self.altern_id_column])
                self.selected_altern_names.append(self.altern_data[index][self.altern_name_column])
            self.next_click()
        self.num_selected_alternatives = len(self.selected_altern_data)
        
    def check_all_alternatives(self):
        self.altern_table.check_all()
    
    def uncheck_all_alternatives(self):
        self.altern_table.uncheck_all()
    
    ################################ Criteria #################################

    def setup_crit_select(self):
        if not self.crit_data:
            self.crit_data = self.project.get_all_criteria()
        self.crit_table.load(self.crit_data)

    def process_crit_select(self):
        selected_crit_indexes = self.crit_table.get_selected_indexes()
        if len(selected_crit_indexes) < 1:
            QMessageBox.critical(self,"Error", "You must select at least one criteria")
        else:
            #Build list of selected crit data
            self.selected_crit_data = []
            self.selected_crit_ids = []
            self.selected_crit_names = []
            self.selected_crit_types = []
            for index in selected_crit_indexes:
                crit = self.crit_data[index]
                self.selected_crit_data.append(crit)
                self.selected_crit_ids.append(crit[self.crit_id_column])
                self.selected_crit_names.append(crit[self.crit_name_column])
                self.selected_crit_types.append(crit[self.crit_type_column])
            self.next_click()
        self.num_selected_criteria = len(self.selected_crit_data)

    def check_all_criteria(self):
        self.crit_table.check_all()

    def uncheck_all_criteria(self):
        self.crit_table.uncheck_all()

    ################################# Input Data ##############################

    def input_prev_click(self):
        ok = self.process_data_input("backward")
        if ok:
            self.prev_click()

    def setup_data_input(self):
        if not self.input_data:
            #Create input set
            self.input_data = InputDataSet(self.selected_altern_data, self.selected_crit_data)
        else:
            #Update input set with any changes in criteria/alternatives
            self.input_data.update_headings(self.selected_altern_data, self.selected_crit_data)
        #Load the weight input table
        self.input_table.load(self.input_data)

    def process_template_export(self):
        """Creates a unicode CSV containing alternatives and criteria for quickly inputting data
        """
        fd = QtGui.QFileDialog(self)
        fd.setFileMode(QFileDialog.AnyFile)
        template_filename = fd.getSaveFileName()
        #Check if filename and if extension already added
        if template_filename:
            if not re.search('[.]'+self.default_template_extension+'$', template_filename):
                template_filename += '.'+self.default_template_extension

            export_arr = initialize_str_array(self.num_selected_criteria+1, self.num_selected_alternatives+2)
            #add alternatives to first row leaving first two cells blank
            export_arr[0] = ["",""]+self.selected_altern_names            
            #add criteria data to first two columns leaving top left cell blank
            for i in range(self.num_selected_criteria):
                (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = self.selected_crit_data[i]
                
                #Add criteria name to first column
                export_arr[i+1][0] = crit_name
                
                #Build option/unit string and add to second column
                crit_option_str = ""                
                if crit_type == "Ordinal" or crit_type == "Binary":
                    for option in crit_options_units:
                        (name, value) = option
                        crit_option_str += "("+unicode(value)+" = "+unicode(name)+")"
                elif crit_type == "Ratio":
                    crit_option_str += "(# "+unicode(crit_options_units)+")"
                    
                export_arr[i+1][1] = crit_option_str

            #Add comments to file explaining the structure
            comments =     [
                            [""],
                            [""],
                            [""],                                                                                  
                            ["*******************************************************************"],
                            ["* This file was generated by Delphos and should ONLY\n   be used to enter data."],
                            ["*"],
                            ["****** File structure ******"],
                            ["*"],
                            ["* Row 1: alternative names (starting with column C)"],
                            ["* Column A: criteria names"],
                            ["* Column B: criteria values with text description"],
                            ["*"],
                            ["****** Instructions ******"],
                            ["*"],
                            ["* - If using a spreadsheet program, resize the"],
                            ["    columns so you can see everything"],
                            ["* - The alternatives and criteria form a"],
                            ["    pair-wise matrix."],
                            ["* - Enter a value for each pair, starting in"],
                            ["    row 2, column C."],
                            ["* - For Ordinal and Binary criteria, enter an"],
                            ["    integer value from the list of possible"],
                            ["    options in column B."],
                            ["* - For Ratio criteria, enter a positive integer"],
                            ["    value, the units for that value are given"],
                            ["    in column B."],
                            ["* - DO NOT add extra criteria or alternatives"],
                            ["    they will not be read."],
                            ["* - DO NOT remove any alternatives or criteria"],                      
                            ["* - DO NOT re-arrange rows/columns as they are"],
                            ["    expected in the order they were exported."],
                            ["* - After inputting data, be sure to resave as"],
                            ["    as a CSV file"],
                            ["* - On Apple Macs you may need to save the file in"],
                            ["   'CSV (Windows)' format"],
                            [""],
                            ["* Failure to follow directions may produce unexpected results!"],
                            ["*******************************************************************"],                            
                        ]
                                
            #output list to CSV.  Use latin1 encoding
            writer = csv.writer(open(template_filename, "wb"), csv.excel)
            writer.writerows(export_arr)
            writer.writerows(comments)
            
            QMessageBox.critical(self,"Template Exported", "CSV Template successfully exported to "+template_filename+"\n\nPopulate this template with data and import it back into Delphos")

    def process_template_import(self):
        """Reads in input from a template
        """
        fd = QtGui.QFileDialog(self)
        fd.setFileMode(QFileDialog.ExistingFile)
        fd.setFilter("*."+self.default_template_extension)
        template_filename = fd.getOpenFileName()

        if template_filename:
            if not re.search('[.]'+self.default_template_extension+'$', template_filename):
                QMessageBox.critical(self,"Error", "You did not select a CSV file (."+self.default_template_extension+" file extension)")
                return None
            
            f = open(template_filename, "r")
            reader = csv.reader(f, dialect=csv.excel)
            
            #Load value into one long list
            import_list = []
            for i in range(self.num_selected_criteria+1):
                try:
                    row = reader.next()
                except csv.Error, e:
                    QMessageBox.critical(self,"Import Error", "Missing or malformed values in CSV file, check all cells where input values are expected")                    
                else:
                    if i is not 0:
                        #append all but first two columns to end of existing list
                        import_list += row[2:]
            
            #Make a copy, we don't want to overwrite the current input data 
            #until we know all the data from the CSV is kosher
            new_input_data = self.input_data.make_copy()
            
            #Load it up
            self.load_data_input_from_array(new_input_data, import_list)
            
            #Replace current input data with new known-good input data from CSV
            self.input_data = new_input_data

            #Reload the input_table
            success = self.input_table.load(self.input_data)
            if success:
                QMessageBox.information(self,"Success", "CSV loaded successfully")
            else :
                QMessageBox.critical(self,"Error", "Due to error, table may only be partially loaded")

    def load_data_input_from_array(self, input_data, input_values):
        #Check for missing or malformed data
        cell_data = input_data.get_cell_data()
        for i in range(len(input_values)):
            new_value = input_values[i]
            if not strIsInt(new_value):
                row = input_data.get_row(i)+2
                crit_name = input_data.get_crit_name(i)
                col = input_data.get_col(i)+3
                altern_name = input_data.get_altern_name(i)
                QMessageBox.critical(self,"ImportError", "Malformed input in row "+str(row)+": '"+crit_name+"', column "+str(col)+": '"+altern_name+"'")
                return None
            
            input_data.set_value(i, input_values[i])
        return input_data   

    def process_data_input(self, direction='forward'):
        input_required = True
        if direction == "backward":
            input_required = False
        
        new_input_data = self.input_data.make_copy()
        
        #print new_input_data
        #print self.input_data
        
        #Get data from table widget
        try:
            self.input_table.get_input_data(input_required, new_input_data)
        except DelphosError, e:
            QMessageBox.critical(self,"Input Error", str(e))
        else:
            #Replace old input data with latest known good input data
            self.input_data = new_input_data
        
            if direction == "forward":  
                #Get lists describing which columns (criteria) in in_matrix are quantitative and which are qualitative
                #(quant_cols, qual_cols) = self.gen_crit_type_lists(self.selected_crit_types)
                #num_qual_criteria = len(qual_cols)
                #num_quant_criteria = len(quant_cols)
                
                if self.input_data:
                        success = self.input_data_checks()
                        if success:
                            #for row in self.input_data
                            #    print row
                            self.next_click()
            else:
                return True

    def input_data_checks(self):
        try:
            self.input_data.check_quant_rows()
        except InputError, e:
            QMessageBox.critical(self,"Input Error", "Your inputs for a given quantitative criterion are all the same value.  This is a limitation of the Evamix algorithm, at least one value in a row must be difference."+str(e))
            return False
        else:
            return True

        try:
            self.input_data.check_qual_rows()
        except InputError, e:
            QMessageBox.critical(self,"Input Error", "Your inputs for all qualitative criteria (Ordinal/Binary) are the same value.  This is not valid input for the Evamix algorithm, at least one value in one qualitative criteria row must be different."+str(e))
            return False
        else:
            return True
        
    ########################## Input Weights #########################

    def weight_prev_click(self):
        ok = self.process_weight_input("backward")
        if ok:
            self.prev_click()

    def setup_weight_input(self):
        if not self.input_weights:
            #Create weight set
            self.input_weights = InputWeightSet(self.selected_crit_data)
        else:
            #Update weight set with any changes in alternatives
            self.input_weights.update_crits(self.selected_crit_data)
        #Load the weight input table
        self.weight_table.load(self.input_weights)

    def process_weight_input(self, direction="forward"):
        input_required = True
        if direction == "backward":
            input_required = False
            
        new_input_weights = self.weight_table.get_input_weights(input_required)
        self.input_weights.update_weights(new_input_weights)            
        if self.input_weights:
            return True
        else:
            return False

    def assign_equal_weight(self):
        self.weight_table.assign_equal_weight()

    ############################### Run #################################
    
    def process_run(self):
            """Processes clicking of 'Run Analysis' button
            """
            self.process_weight_input("forward")
            if self.isError:
                self.isError = False
            else:
                self.emit(SIGNAL("mca_analysis_info_collected"), self.selected_altern_data, self.selected_crit_data, self.input_data.get_mca_input(), self.input_weights.get_weights(), self.selected_crit_types)

    ############################# General ###############################

    def next_click(self):
        """Shift stack forward one
        """
        current_index = self.mca_stack.currentIndex()
        self.mca_stack.setCurrentIndex(current_index+1)

    def prev_click(self):
        """Shift stack back one
        """
        current_index = self.mca_stack.currentIndex()
        prev_widget = self.mca_stack.widget(current_index-1)
        self.mca_stack.setCurrentWidget(prev_widget)    

    def process_reject(self):
        """Processes clicking of Cancel button in dialog
        """
        self.hide()
        self.deleteLater()
    
    def process_current_change(self, index):
        """Loads the appropriate widget when the next button is clicked
        """
        ok = False
        if self.cur_index < index:
            if index is 2:
                self.setup_data_input()
            elif index is 3:
                self.setup_weight_input()
            elif index is 4:
                self.setup_run()
                
        self.cur_index = index

class InputDataSet():
    """Maintains altern/crit grid input data by the user.
    
    The grid cells of data are represented in a linear list, not a 2D list or other
    The row and column of each cell is stored within the cells structure
    So an 8x8 grid, 8 alternatives, 8 criteria would have a 64 element cell_data list
    
    Ties input values to their associated altern/criteria pair so
    that the user can go back and change the altern and crit without losing
    the data that they already input.  It also separates data from 
    presentation.
    
    input_data: [[[altern_data][crit_data][row][col][value]], ...]
    altern_data: (altern_id, altern_name, altern_color)
    crit_data: (crit_id, crit_name, crit_type, crit_options_units, cost_benefit)
    """
    
    def __init__(self, altern_data=None, crit_data=None):
        self.num_alterns = 0
        self.num_crits = 0
        self.cell_data = None
        if altern_data and crit_data:      
            self.cell_data = self.create_cell_data(altern_data, crit_data)
 
    def make_copy(self):
        new_set = InputDataSet()
        new_set.cell_data = copy.copy(self.cell_data)
        new_set.num_alterns = self.num_alterns
        new_set.num_crits = self.num_crits
        return new_set
    
    def create_cell_data(self, altern_data, crit_data):
        cell_data = []
        self.num_alterns = len(altern_data)
        self.num_crits = len(crit_data)
        for i in range(self.num_crits):
            for j in range(self.num_alterns):
                #Append associated alter and crit data to each 'cell'.  
                #Append row and column to put in
                #Append space for input value
                cell_data.append([altern_data[j], crit_data[i], i, j, None])
        
        #print "input data:"
        #print input_data
        
        return cell_data
    
    def update_values(self, new_values):
        for i in range(len(self.cell_data)):
            self.set_value(i, new_values.get_value(i))
    
    def update_headings(self, new_altern_data, new_crit_data):
        if not new_altern_data or not new_crit_data:
            raise Exception, "Error updating input table"
    
        #Create new empty input set
        new_input_data = InputDataSet(new_altern_data, new_crit_data)
        
        #Load values from current input set into new input set where altern 
        #and crit id match
        for i in range(len(self.cell_data)):
            for j in range(len(new_input_data.cell_data)):
                cur_altern_id = self.cell_data[i][0][0]
                cur_crit_id = self.cell_data[i][1][0]
                new_altern_id = new_input_data.cell_data[j][0][0]
                new_crit_id = new_input_data.cell_data[j][1][0]
                if cur_altern_id == new_altern_id and cur_crit_id == new_crit_id:
                    #Copy value
                    new_input_data.cell_data[j][4] = self.cell_data[i][4]
        
        #Replace current input data set with new updated one
        self.num_alterns = new_input_data.num_alterns
        self.num_crits = new_input_data.num_crits
        self.cell_data = new_input_data.cell_data

    def get_num_alterns(self):
        return self.num_alterns

    def get_num_crits(self):
        return self.num_crits
  
    def get_cell_data(self):
        return self.cell_data
    
    def get_cell_contents(self, index):
        return self.cell_data[index]
    
    def get_num_cells(self):
        return len(self.cell_data)
        
    def get_row(self, index):
        return self.cell_data[index][2]
        
    def get_col(self, index):
        return self.cell_data[index][3]

    def get_value(self, index):
        return self.cell_data[index][4]

    def set_value(self, index, value):
        self.cell_data[index][4] = value

    def get_crit_name(self, index):
        return self.cell_data[index][1][1]
    
    def get_crit_type(self, index):
        return self.cell_data[index][1][2]
    
    def get_altern_name(self, index):
        return self.cell_data[index][0][1]

    def get_qual_rows(self):
        return list(Set([x[2] for x in self.cell_data if x[1][2] == "Ordinal" or x[1][2] == "Binary"]))
    
    def get_quant_rows(self):
        return list(Set([x[2] for x in self.cell_data if x[1][2] == "Ratio"]))

    def check_quant_rows(self):
        """Check if all rows with quantative criteria have the same values
        within a given row"""
        quant_rows = self.get_quant_rows()
        for row in quant_rows:
            if self.check_same_values_by_row(row):
                crit_name = self.get_crit_name(row)
                raise InputError, str(row+1)+" '"+str(crit_name)+"'"
        
    def check_qual_rows(self):
        """Check if all rows with qualitative criteria have the same values
        within a given row"""
        qual_rows = self.get_qual_rows()       
        row_same_list = []
        for row in qual_rows:           
            crit_name = self.get_crit_name(row)
            row_same_list.append(self.check_same_values_by_row(row))
             
        all_same = reduce(lambda x,y: x and y, row_same_list) 
        if all_same: 
            raise InputError, str(row+1)+" '"+str(crit_name)+"'"
            
    def check_same_values_by_row(self, row):
        """Check if the cells in any row all have the same values
        """
        row_cells = self.get_row_cells(row)            
        same_bool_list = [x[4] == y[4] for x in [row_cells[0]] for y in row_cells]
        same = reduce(lambda x, y: x and y, same_bool_list)
        if same:
            return True
        else:
            return False
        
    def get_num_rows(self):
        """Return number of rows in input data
        """
        #return list(Set([x[2] for x in self.cell_data]))
        return self.num_crits
    
    def get_row_cells(self, row):
        return [cell for cell in self.cell_data if cell[2] == row]
    
    def get_mca_input(self):
        """Generate in matrix for Evamix MCA
        alterns down, criteria across, opposite of table widget"""
        input = initialize_int_array(self.get_num_alterns(), self.get_num_crits())
        for cell in self.cell_data:
            col = cell[2] #Note pulling the row valu and using as column
            row = cell[3] #Note pulling the column value and using as row
            input[row][col] = cell[4]
        return input
    
    def load_mca_input(self, input_matrix):
    	for cell in self.cell_data:
    		col = cell[2]
    		row = cell[3]
    		cell[4] = input_matrix[row][col]
        
class InputWeightSet():
    """Maintains weights input by the user.
    
    Ties weight values input by user to their associated criterion so
    that the user can go back and change the criteria without losing
    the data that they already input.  It also separates data from 
    presentation.
    """
    def __init__(self, crit_data):
        #TODO: Really we should only be keeping the id, name and weight
        self.crit_id_column = 0
        self.crit_name_column = 1
        self.weight_column = 2        

        self.weight_data = self.create_weight_data(crit_data)

    def create_weight_data(self, crit_data):
        """Given a critieria set, create an empty weight set
        """
        weight_data = []
        for crit in crit_data:
            id = crit[self.crit_id_column]
            name = crit[self.crit_name_column]
            weight_data.append([id, name, None])
        return weight_data
            
    def update_weights(self, new_weights):
        
        if not new_weights or len(new_weights) != len(self.weight_data):
            raise Exception, "Error updating weights"

        #print "Weights before: "
        #print self.get_weight_data()

        #print "New weights: "
        #print new_weights

        for i in range(len(new_weights)):
            self.weight_data[i][self.weight_column] = new_weights[i]
                  
        #print "Update weights"
        #print self.get_weight_data()

    def update_crits(self, new_crit_data):
        #print "New crit data"
        #print new_crit_data
    
        #Create new weight data
        new_weight_data = self.create_weight_data(new_crit_data)
        #Transfer weight values
        for i in range(len(self.weight_data)):    
            for j in range(len(new_weight_data)):
                if new_weight_data[j][self.crit_id_column] == self.weight_data[i][self.crit_id_column]:
                    new_weight_data[j][self.weight_column] = self.weight_data[i][self.weight_column]                
        
        #Drop the old weight data
        self.weight_data = new_weight_data
        
        #print "Updated crit data"
        #print self.weight_data
    
    def get_weight_data(self):
        return self.weight_data
    
    def get_weights(self):
        weights = []
        for item in self.weight_data:
            weights.append(item[self.weight_column])
        return weights