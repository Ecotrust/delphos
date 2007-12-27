#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
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
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from mca_wizard_ui import Ui_McaWizard
from util.common_functions import *
from util.unicode_csv import *
from core.input_data_set import *
from core.input_weight_set import *

class McaWizard(QDialog, Ui_McaWizard):
    """Manages the collection of MCA analysis input
    
    Optionally takes input from a previous MCA analysis run
    """
    def __init__(self, gui_manager, parent, project, prev_run_data=None, global_input_data=None):
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
        self.altern_data = None
        self.selected_altern_data = []
        self.selected_altern_ids = []
        self.selected_altern_names = []
        self.num_selected_alternatives = 0
        self.altern_id_column = 0 # in altern_data type list
        self.altern_name_column = 1    #in altern_data type list
        
        #Contains field data for all criteria selected, each row is a
        #list of [crit_id, crit_name, crit_type, crit_options, crit_cost_benefit]
        self.crit_data = None
        self.selected_crit_data = []
        self.selected_crit_ids = []
        self.selected_crit_names = []
        self.num_selected_criteria = 0
        self.crit_id_column = 0
        self.crit_name_column = 1
        self.crit_type_column = 2
        self.crit_options_column = 3
        self.crit_bc_column = 4
        
        self.global_input_data = None
        
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
        QObject.connect(self.run_analysis_button,QtCore.SIGNAL("clicked()"), self.process_run)

        self.connect(self.help_select_alternatives, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_select_criteria, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_input_mca_data, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_weight_criteria, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
                
        #Other signals
        QObject.connect(self.mca_stack,QtCore.SIGNAL("currentChanged(int)"), self.process_current_change)
        
        if prev_run_data:
            (prev_run_id, prev_run_name, prev_run_description, prev_altern_data, prev_crit_data, prev_input_data, prev_input_weights, prev_results, prev_creation_date, int_results) = prev_run_data
            #self.altern_data = prev_altern_data        
            #self.crit_data = prev_crit_data
        elif global_input_data:
            self.global_input_data = global_input_data
            
        self.setup_altern_select()
        self.setup_crit_select()
        
        if prev_run_data:
        	#Load up the wizard dialogs
            self.check_prev_alternatives(prev_altern_data)
            self.check_prev_criteria(prev_crit_data)

            self.process_altern_select()
            self.process_crit_select()
            
            self.setup_data_input()
            self.input_data.load_mca_input(prev_input_data)
            self.input_table.load(self.input_data)
            self.process_data_input()
            
            self.setup_weight_input()
            self.input_weights.update_weights(prev_input_weights)
            self.weight_table.load(self.input_weights)
            self.process_weight_input()
        elif global_input_data:         
            #Creates InputDataSet and loads global input values too
            self.setup_data_input()
            
        self.jump_to_page(1)

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
    
    def check_prev_alternatives(self, prev_altern_data):
        for i in range(len(prev_altern_data)):
            for j in range(len(self.altern_data)):
                if prev_altern_data[i][self.altern_id_column] == self.altern_data[j][self.altern_id_column]:
                    self.altern_table.check_one(j)
                    break
    
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
            self.selected_crit_bc = []
            for index in selected_crit_indexes:
                crit = self.crit_data[index]
                self.selected_crit_data.append(crit)
                self.selected_crit_ids.append(crit[self.crit_id_column])
                self.selected_crit_names.append(crit[self.crit_name_column])
                self.selected_crit_types.append(crit[self.crit_type_column])
                self.selected_crit_bc.append(crit[self.crit_bc_column])
            self.next_click()
        self.num_selected_criteria = len(self.selected_crit_data)

    def check_all_criteria(self):
        self.crit_table.check_all()

    def check_prev_criteria(self, prev_crit_data):
        for i in range(len(prev_crit_data)):
            for j in range(len(self.crit_data)):
                if prev_crit_data[i][self.crit_id_column] == self.crit_data[j][self.crit_id_column]:
                    self.crit_table.check_one(j)
                    break

    def uncheck_all_criteria(self):
        self.crit_table.uncheck_all()

    ################################# Input Data ##############################

    def input_prev_click(self):
        ok = self.process_data_input("backward")
        if ok:
            self.prev_click()

    def setup_data_input(self):
        """Create or update InputDataSet which brings together alterns, crits, 
        and input values in one place.  Perhaps not a good implementation, but
        encapsulates a lot of the logic to work with them.
        """
        self.gui_manager.load_dialog.show()
        if not self.input_data and self.global_input_data:
            self.input_data = InputDataSet(self.altern_data, self.crit_data)
            self.input_data.load_values(self.global_input_data)
        elif not self.input_data:
            #Create input set
            self.input_data = InputDataSet(self.selected_altern_data, self.selected_crit_data)
            self.input_data.load_values(self.project.get_all_input())
        else:
            #Update input set with any changes in criteria/alternatives
            self.input_data.update_headings(self.selected_altern_data, self.selected_crit_data)
        #Load the weight input table
        self.input_table.load(self.input_data)
        self.gui_manager.load_dialog.hide()

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
            QMessageBox.critical(self,"Input Error", unicode(e.value))
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
            QMessageBox.critical(self,"Input Error", "Your inputs for a given quantitative criterion (Ratio) are all the same value.  This is a limitation of the Evamix algorithm, at least one value in a row must be difference."+unicode(e.value))
            return False

        try:
            self.input_data.check_qual_rows()
        except InputError, e:
            QMessageBox.critical(self,"Input Error", "Your inputs for all qualitative criteria (Ordinal/Binary) are the same value.  This is not valid input for the Evamix algorithm, at least one value in one qualitative criteria row must be different."+unicode(e.value))
            return False

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
                self.emit(SIGNAL("mca_analysis_info_collected"), self.selected_altern_data, self.selected_crit_data, self.input_data.get_mca_input(), self.input_weights.get_weights(), self.selected_crit_types, self.selected_crit_bc)

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
    
    def jump_to_page(self, page_num):
        widget = self.mca_stack.widget(page_num-1)
        self.mca_stack.setCurrentWidget(widget)

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