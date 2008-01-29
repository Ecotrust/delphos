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
from os import path
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from core.input_data_set import InputDataSet

from util.unicode_csv import *
from util.common_functions import *

from delphos_exceptions import *
from project_view_ui import Ui_ProjectView
from add_alternative_dialog import AddAlternDialog
from add_criteria_dialog import AddCriteriaDialog
from McaWizard import McaWizard 
from McaResultView import McaResultView
from yes_no_dialog import YesNoDialog
from mca_rerun_dialog import McaRerunDialog
from export_analysis_dialog import ExportAnalysisDialog

class ProjectViewDialog(QDialog, Ui_ProjectView):
    """Manages interaction with the project interface and the underlying DB
    
    Includes adding, removing, editing and displaying of project data and the sub interfaces needed
    to do that (eg. add new criteria subwindow).
    """
    def __init__(self, gui_manager, project):
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.gui_manager = gui_manager
        self.project = project
        self.input_data = None

        self.cur_tab = 0

        self.default_template_extension = "csv"
        self.output_encoding = 'latin-1'

        QObject.connect(self.add_altern_button,QtCore.SIGNAL("clicked()"), self.start_add_alternative)
        QObject.connect(self.remove_altern_button,QtCore.SIGNAL("clicked()"), self.start_remove_alternative)
        QObject.connect(self.add_criteria_button,QtCore.SIGNAL("clicked()"), self.start_add_criteria)
        QObject.connect(self.remove_criteria_button,QtCore.SIGNAL("clicked()"), self.start_remove_criteria)        
        QObject.connect(self.view_analysis_button,QtCore.SIGNAL("clicked()"), self.start_view_analysis)
        QObject.connect(self.rerun_analysis_button,QtCore.SIGNAL("clicked()"), self.start_rerun_analysis1)
        QObject.connect(self.export_analysis_button,QtCore.SIGNAL("clicked()"), self.start_export_analysis)
        QObject.connect(self.delete_analysis_button,QtCore.SIGNAL("clicked()"), self.start_delete_analysis)
        QObject.connect(self.new_analysis_button,QtCore.SIGNAL("clicked()"), self.start_new_analysis)

        self.connect(self.help_define_alternatives, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_define_criteria, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_input_data, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_8_run_analysis, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)
        self.connect(self.help_run_the_program, SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)

        self.connect(self.input_table, SIGNAL("update_input_value"), self.project.update_input_value)
        self.connect(self.input_table, SIGNAL("update_input_complete"), self.load_data_input)
        self.connect(self.input_table, SIGNAL("input_changed"), self.enable_input_save)

        QObject.connect(self.tabProject,QtCore.SIGNAL("currentChanged(int)"), self.process_current_change)
        QObject.connect(self.save_button,QtCore.SIGNAL("clicked()"), self.save_input)

        QObject.connect(self.export_button,QtCore.SIGNAL("clicked()"), self.process_template_export)
        QObject.connect(self.import_button,QtCore.SIGNAL("clicked()"), self.process_template_import)

        self.load_project_data_tab()
        
        all_alternatives = self.project.get_all_alternatives()
        all_criteria = self.project.get_all_criteria()
        all_input = self.project.get_all_input()
        
        self.altern_table.load(all_alternatives)
        self.crit_table.load(all_criteria)
        
        self.load_data_input()
        
        #self.input_table.load(all_alternatives, all_criteria, all_input)
        self.mca_runs_table.load(self.project.get_mca_runs_basic())

    def load_project_data_tab(self):
        try:
            (project_name, project_type, project_sub_type, project_created) = self.project.get_project_data()
        except DelphosError, r:
            QMessageBox.critical(self,"Delphos", "Project data not found")
        else:            
            self.project_name.setText(project_name)
            self.project_type.setText(project_type)
            self.project_sub_type.setText(project_sub_type)
            self.project_created.setText(unicode(project_created))
            self.num_runs_label.setText(unicode(self.project.get_num_mca_runs()))

    ################################# Alternatives ##############################

    def start_add_alternative(self):
        """Create dialog for adding an alternative
        """
        #Load add alternative dialog form
        self.add_altern_dialog = AddAlternDialog(self.gui_manager, self)
        #Register handler for signal that alternative info has been collected and can be added
        self.connect(self.add_altern_dialog, SIGNAL("add_alternative_info_collected"), self.finish_add_alternative)
        self.add_altern_dialog.show()
    
    def finish_add_alternative(self, alternative_name, alternative_color):
        """Add alternative given its name from dialog
        """
        try:
            self.project.add_alternative(alternative_name, alternative_color)
        except DelphosError, e:
            QMessageBox.critical(self.add_altern_dialog,"Alternative Error", unicode(e.value))
        else:
            self.add_altern_dialog.close()
            self.add_altern_dialog.deleteLater()
            self.altern_table.load(self.project.get_all_alternatives())
    
    def start_remove_alternative(self):
        try:
            cur_row_item = self.altern_table.get_current_row_items()
        except DelphosError, e:
            QMessageBox.critical(self,"Please select or add an alternative first.", unicode(e.value))
        else:
            altern_name = unicode(cur_row_item.text())
            altern_id = self.project.get_alternative_id_by_name(altern_name)
            altern_success = self.project.remove_alternative_by_name(altern_name)
            input_success = self.project.remove_input_by_alternative(altern_id)
            if not altern_success or not input_success:
                QMessageBox.critical(self,"Remove Alternative Error", "Failed to remove alternative and all associated input data.")
            else:
                self.altern_table.load(self.project.get_all_alternatives())

    ################################# Criteria ##############################

    def start_add_criteria(self):
        """Create dialog for adding criteria
        """
        #Load add criteria dialog form
        self.add_criteria_dialog = AddCriteriaDialog(self.gui_manager, self)
        #Register handler for signal that alternative info has been collected and can be added
        self.connect(self.add_criteria_dialog, SIGNAL("add_criteria_info_collected"), self.finish_add_criteria)
        self.add_criteria_dialog.show()

    def finish_add_criteria(self, criteria_info):
        try:
            #Add criterion to DB
            self.project.add_criteria(criteria_info)
        except DelphosError, e:
            QMessageBox.critical(self.add_criteria_dialog,"Criteria Error", str(e.value))
        else:
            self.add_criteria_dialog.close()
            self.add_criteria_dialog.deleteLater()
            self.crit_table.load(self.project.get_all_criteria())

    def start_remove_criteria(self):
        try:
            cur_item = self.crit_table.get_current_row_items()
        except DelphosError, e:
            QMessageBox.critical(self,"Error Removing Criterion", unicode(e.value))
        else:
            crit_desc = unicode(cur_item.text())
            crit_id = self.project.get_criteria_id_by_name(crit_desc)            
            crit_success = self.project.remove_criteria_by_description(crit_desc)
            input_success = self.project.remove_input_by_criteria(crit_id)
            if not crit_success or not input_success:
                QMessageBox.critical(self,"Remove Criteria Error", "Failed to remove criteria and all associated input data.")
            else:
                self.crit_table.load(self.project.get_all_criteria())

    ################################# Input Data ##############################

    def enable_input_save(self, prevRow=0, prevCol=0, curRow=0, curCol=0):
        self.save_button.setEnabled(True)

    def disable_input_save(self):
        self.save_button.setEnabled(False)

    def save_input(self):
        self.gui_manager.save_dialog.show()
        success = self.input_table.save_input_data()
        if success:
            self.save_button.setDisabled(True)
        self.gui_manager.save_dialog.hide()

    def load_data_input(self):
        self.gui_manager.load_dialog.show()
        all_alternatives = self.project.get_all_alternatives()
        all_criteria = self.project.get_all_criteria()
        all_input = self.project.get_all_input()
        self.input_table.load(all_alternatives, all_criteria, all_input)
        #Loading of input will trigger enabling of save button, needs to default to diabled
        self.disable_input_save()
        self.gui_manager.load_dialog.hide()

    def get_current_input(self):
        try:
            cur_input_vals = self.input_table.get_input_vals(input_required=False)
        except DelphosError, e:
            QMessageBox.critical(self,"Input Error", unicode(e.value))
            return False
        else:     
            #Associate current values with their altern and crit id's
            cur_input_set = []
            num_rows = self.project.num_criteria()
            num_columns = self.project.num_alternatives()
            altern_data = self.project.get_all_alternatives()
            crit_data = self.project.get_all_criteria()
            
            for i in range(num_rows):
                (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data[i]
                row = i
                for j in range(num_columns):
                    (altern_id, altern_name, altern_color) = altern_data[j]
                    column = j
    
                    cur_val = cur_input_vals[row][column]
                    cur_input_set.append((altern_id, crit_id, cur_val)) 
            return cur_input_set      

    def process_template_export(self):
        """Creates a unicode CSV containing alternatives and criteria for quickly inputting data
        """
        fd = QtGui.QFileDialog(self)
        fd.setFileMode(QFileDialog.AnyFile)
        template_filename = fd.getSaveFileName()
        
        num_alterns = self.project.num_alternatives()
        num_criteria = self.project.num_criteria()
        altern_data = self.project.get_all_alternatives()
        crit_data = self.project.get_all_criteria()
        input_data = self.project.get_all_input()
        
        #Check if filename and if extension already added
        if template_filename:
            if not re.search('[.]'+self.default_template_extension+'$', template_filename):
                template_filename += '.'+self.default_template_extension

            export_arr = initialize_str_array(num_criteria+1, num_alterns+3)
            #add alternatives to first row leaving first two cells blank
            altern_names = [name for (id, name, color) in altern_data]
            altern_col_header_row = ["",""]+altern_names 
            export_arr[0] = altern_col_header_row
            #add criteria data to first two columns leaving top left cell blank
            for i in range(num_criteria):
                (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data[i]
                #Add criteria name to first column of each row
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

                #Add input values for row if they exist
                for j in range(num_alterns):
                    (altern_id, altern_name, altern_color) = altern_data[j]
                    #Get input value
                    input_value = self.project.get_input_value(altern_id, crit_id)
                    if input_value:
                        export_arr[i+1][j+2] = unicode(input_value)
                export_arr[i+1][j+3] = "|"                 

            # Add extra row with filler characters in each cell to ensure empty
            # values are maintained in the CSV for all rows 
            # (eg. 2,3,2,,,,,,,,,,,,).  Excel chops off end columns with no 
            # data when resaving a CSV.
            export_arr.append(["------------------------","------------------------"] + ["------------------------" for row in range(num_alterns)])

            #Add comments to file explaining the structure
            comments =     [
                            [""],
                            [""],
                            [""],                                                                                  
                            ["*******************************************************************"],
                            ["* This file was generated by Delphos and should ONLY be"],
                            ["*  used to input data."],
                            ["*"],
                            ["****** Template structure ******"],
                            ["*"],
                            ["* Row 1: alternative names (starting with the third column)"],
                            ["* Column A: criteria names"],
                            ["* Column B: criteria values with text description"],
                            ["*"],
                            ["****** Instructions ******"],
                            ["*"],
                            ["* - 1. If using a spreadsheet program, resize the"],
                            ["*    columns so you can see everything"],
                            ["* - 2. The alternatives and criteria form a"],
                            ["*    pair-wise matrix.  Any input you already"],
                            ["*    provided should be available."],
                            ["* - 3a. Enter new values or edit existing ones."],
                            ["* - 3b. For Ordinal and Binary criteria, enter an"],
                            ["*    integer value from the list of possible"],
                            ["*    options in column B.  Do not input the name."],
                            ["* - 3c. For Ratio criteria, enter a positive integer"],
                            ["*    value, the units for that value are given"],
                            ["*    in column B."],
                            ["* - 4. After inputting data, be sure to resave as"],
                            ["*    as a CSV file.  On Apple Macs you may need to"],
                            ["*    save the file in 'CSV (Windows)' format"],
                            ["* - 5. Import the CSV template back into Delphos"],
                            ["*    by clicking the Import button in the input"],
                            ["*    data tab."],
                            ["* - 6a. Each time you alter the project alternatives or"], 
                            ["*    criteria you will need to export a new updated"],
                            ["*    template."],
                            ["* - 6b. DO NOT add extra criteria or alternatives"],
                            ["*    to the CSV template, they will not be read."],                            
                            ["* - 6c. DO NOT remove any alternatives or criteria from"],
                            ["*    the CSV template, do this in Delphos and export"],
                            ["*    a new template"],                      
                            ["* - 6d. DO NOT re-arrange rows/columns in the CSV"],
                            ["*    template.  Upon import, they are expected in the"],
                            ["*    order in which they were exported."],
                            [""],
                            ["* Failure to follow directions may produce unexpected results!"],
                            ["*******************************************************************"],                            
                        ]
                                
            #output list to CSV.  Use latin1 encoding
            writer = UnicodeWriter(open(template_filename, "wb"), csv.excel, 'utf-8')
            #writer = csv.writer(open(template_filename, "wb"), csv.excel)
            writer.writerows(export_arr)
            writer.writerows(comments)
            
            QMessageBox.information(self,"CSV Template Exported", "A CSV file has been exported to "+template_filename+"\n\nOpen this file in a spreadsheet program like OpenOffice Calc or MS Excel.\n\nFollow the instructions at the bottom of the file.\n\nPopulate the template with data and import it back into Delphos")

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
            reader = UnicodeReader(open(template_filename, "r"), csv.excel, 'utf-8')

            num_alterns = self.project.num_alternatives()
            num_criteria = self.project.num_criteria()
            
            #Load new values into one long import list
            import_list = []
            for i in range(num_criteria+1):
                try:
                    row = reader.next()
                except csv.Error, e:
                    QMessageBox.critical(self,"Import Error", "Missing or malformed values in CSV file, check all cells where input values are expected")                    
                else:
                    if i is not 0:
                        #append all but first two columns to end of existing list
                        import_list.append(row[2:])
                      
            altern_data = self.project.get_all_alternatives()
            crit_data = self.project.get_all_criteria()            
            
            #Start with the current input
            #new_input_data = self.project.get_all_input()
            
            #Load the new input
            new_input_data = None
            try:
                new_input_data = self.load_data_input_from_array(altern_data, crit_data, import_list)
            except DataImportError, e:
                QMessageBox.critical(self,"ImportError", unicode(e.value))
                return
            
            #Replace current input data with new known-good input data from CSV
            self.input_data = new_input_data

            #Reload the input_table
            success = self.input_table.load(altern_data, crit_data, self.input_data)
            if success:
                QMessageBox.information(self,"Success", "CSV loaded successfully")
            else :
                QMessageBox.critical(self,"Error", "Due to error, table may only be partially loaded")

    def load_data_input_from_array(self, altern_data, crit_data, import_list):
        """Load new input_values into input_data, overwriting existing input"""

        num_alterns = self.project.num_alternatives()
        num_criteria = self.project.num_criteria()
        new_input_data = []

        #Check for missing or malformed data
        #cell_data = input_data.get_cell_data()

        for i in range(num_criteria):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data[i]
            row = i
            for j in range(num_alterns):
                (altern_id, altern_name, altern_color) = altern_data[j]
                column = j
                new_value = import_list[row][column]

                if new_value != "" and not strIsInt(new_value):
                    raise DataImportError, "Malformed input '"+new_value+"' in imported CSV file. Check row "+unicode(row+2)+": '"+crit_name+"', column "+unicode(column+3)+": '"+altern_name+"'"                        
                else:
                    new_input_data.append((altern_id, crit_id, new_value))

        return new_input_data  

    ################################# Analysis ##############################

    def start_new_analysis(self):
        self.analysis_name = self.analysis_name_edit.text()
        self.analysis_description = self.analysis_description_edit.text()
        if not self.analysis_name:
            QMessageBox.critical(self,"Analysis Error", "You must enter a name for this analysis")
            return False;
        else:
            #Fire up MCA Wizard.
            self.gui_manager.load_dialog.show()           
            if self.input_table.loaded:
                cur_input_data = self.get_current_input()
                if not cur_input_data:
                    self.gui_manager.load_dialog.hide()
                    return False;
                self.mca_wizard = McaWizard(self.gui_manager, self, self.project, global_input_data=cur_input_data)
            else:
                self.mca_wizard = McaWizard(self.gui_manager, self, self.project)
                
            self.connect(self.mca_wizard, SIGNAL("mca_analysis_info_collected"), self.finish_new_analysis)
            self.mca_wizard.show()
        self.gui_manager.load_dialog.hide()
            
    def finish_new_analysis(self, altern_data, crit_data, input_data, input_weights, selected_crit_types, selected_crit_bc):
        try:
            input_weights_copy = copy.deepcopy(input_weights)
            self.gui_manager.process_dialog.show()
            [final_scores, int_data] = self.project.run_mca(input_data, input_weights_copy, selected_crit_types, selected_crit_bc)
        except DelphosError, e:
            self.gui_manager.process_dialog.hide()
            QMessageBox.critical(self,"Evamix Error", str(e))
        except ZeroDivisionError, e:
            self.gui_manager.process_dialog.hide()
            QMessageBox.critical(self,"Evamix Error", "Division by zero: "+str(e))
        else:
            if final_scores:
                self.mca_wizard.hide()
                self.mca_wizard.deleteLater()       
                self.project.save_analysis(self.analysis_name, self.analysis_description, altern_data, crit_data, input_data, input_weights, final_scores, int_data)
                self.mca_runs_table.load(self.project.get_mca_runs_basic())
                self.gui_manager.process_dialog.hide()
                self.show_analysis_results(self.analysis_name, self.analysis_description, altern_data, crit_data, input_data, input_weights, final_scores)
            else:
                QMessageBox.critical(self,"Analysis Error", "MCA analysis failed.")
            


    def start_view_analysis(self):
        try:
            selected_id = self.mca_runs_table.get_selected_id()
        except InputError, e:
            QMessageBox.critical(self,"View Error", str(e.value))
        else:
            (id, name, description, altern_data, crit_data, input_data, input_weights, results, created, int_data) = self.project.get_mca_run_by_id(selected_id)
            self.show_analysis_results(name, description, altern_data, crit_data, input_data, input_weights, results)

    def start_rerun_analysis1(self):
        try:
            selected_id = self.mca_runs_table.get_selected_id()
            self.mca_data = self.project.get_mca_run_by_id(selected_id)
        except InputError, e:
            QMessageBox.critical(self,"Run Error", str(e.value))
        else:            
            self.rerun_dialog = McaRerunDialog(self)
            self.connect(self.rerun_dialog, SIGNAL("mca_rerun_info_collected"), self.start_rerun_analysis2)
            self.rerun_dialog.show()
    
    def start_rerun_analysis2(self, name, description):
        self.analysis_name = name
        self.analysis_description = description
        self.rerun_dialog.hide()
        self.rerun_dialog.deleteLater()
        self.mca_wizard = McaWizard(self.gui_manager, self, self.project, self.mca_data)
        self.connect(self.mca_wizard, SIGNAL("mca_analysis_info_collected"), self.finish_new_analysis)
        self.mca_wizard.show()    
    
    def start_export_analysis(self):
        try:
            self.export_id = self.mca_runs_table.get_selected_id()
        except DelphosError, e:
            QMessageBox.critical(self,"Analysis Delete Error", str(e.value))    
        else:
            self.export_analysis_dialog = ExportAnalysisDialog(self)
            self.connect(self.export_analysis_dialog, SIGNAL("export_analysis_info_collected"), self.finish_export_analysis)
            self.export_analysis_dialog.show()
    
    def finish_export_analysis(self, filename):
        
        (run_id, run_name, run_description, altern_data, crit_data, input_data, input_weights, results, creation_date, int_results) = self.project.get_mca_run_by_id(self.export_id) 
        
        num_crits = len(crit_data)
        num_alterns = len(altern_data)
        altern_names = [x[1] for x in altern_data]

        cols = num_alterns+5
        
        #Blank row of right width for insertion into CSV
        blank_row = [["" for col in range(cols)]]
        #Build header row with given title of correct width
        build_header_row = lambda cols, title: [[title]+["" for col in range(cols-1)]]

        num_header_rows = 3
        header_arr = initialize_str_array(num_header_rows, cols)
        header_arr [0][0] = "Name: "
        header_arr [0][1] = unicode(run_name)
        header_arr [1][0] = "Description: "
        header_arr [1][1] = unicode(run_description)
        header_arr [2][0] = "Creation Date: "
        header_arr [2][1] = unicode(creation_date)

        #Input data
        input_arr = initialize_str_array(num_crits+1, cols)
        input_arr[0] = ["",""]+altern_names+["","Original Weight", "Standardized Weight"]          
                
        for i in range(num_crits):
            (crit_id, crit_name, crit_type, crit_options_units, cost_benefit) = crit_data[i]
            
            #Add criteria name to first column
            input_arr[i+1][0] = crit_name

            #Build option/unit string and add to second column
            crit_option_str = ""                
            if crit_type == "Ordinal" or crit_type == "Binary":
                for option in crit_options_units:
                    (name, value) = option
                    crit_option_str += "("+unicode(value)+" = "+unicode(name)+")"
            elif crit_type == "Ratio":
                crit_option_str += "("+unicode(crit_options_units)+")"    
            input_arr[i+1][1] = crit_option_str
            
            #Fill in input values
            for j in range(num_alterns):
                #input data is transposed in the DB
                input_arr[i+1][j+2] = unicode(input_data[j][i])
            
            #Add original weight
            input_arr[i+1][-2] = unicode(input_weights[i])
            #Add standardized weight 
            input_arr[i+1][-1] = unicode(int_results[0][i])

        #quantitative impact matrix
        quant_impact_arr = initialize_str_array(num_alterns+1, cols)
        quant_impact_arr[0] = [""]+altern_names+["","",""]
        
        #qualitative impact matrix
        qual_impact_arr = initialize_str_array(num_alterns+1, cols)
        qual_impact_arr[0] = [""]+altern_names+["","",""]  
        
        #final impact matrix
        final_arr = initialize_str_array(num_alterns+1, cols)
        final_arr[0] = [""]+altern_names+["","",""] 
        
        #final_score matrix
        final_score_arr = initialize_str_array(num_alterns+1, cols)
        final_score_arr[0] = ["Alternative", "Score (The higher the better, sort to get ranking)"]

        for i in range(num_alterns):
            #Add altern name to first column
            quant_impact_arr[i+1][0] = altern_names[i]
            #Fill in values
            for j in range(num_alterns):
                #data is transposed in the DB
                quant_impact_arr[i+1][j+1] = unicode(int_results[1][j][i])
            
            #Add altern name to first column
            qual_impact_arr[i+1][0] = altern_names[i]
            #Fill in values
            for j in range(num_alterns):
                #data is transposed in the DB
                qual_impact_arr[i+1][j+1] = unicode(int_results[2][j][i])
                
            #Add altern name to first column
            final_arr[i+1][0] = altern_names[i]
            #Fill in values
            for j in range(num_alterns):
                #data is transposed in the DB
                final_arr[i+1][j+1] = unicode(int_results[3][j][i])

            #Add altern name to first column
            final_score_arr[i+1][0] = altern_names[i]
            #Fill in score
            final_score_arr[i+1][1] = unicode(results[i]) 
        
        #Output lists to CSV
        #writer = csv.writer(open(filename, "wb"), csv.excel)
        writer = UnicodeWriter(open(filename, "wb"), csv.excel, 'utf-8')
        writer.writerows(header_arr)
        writer.writerows(blank_row)
        writer.writerows(build_header_row(cols, "Input From Interview Process"))
        writer.writerows(blank_row)
        writer.writerows(input_arr)
        writer.writerows(blank_row)
        writer.writerows(build_header_row(cols, "Quantitative Impact Matrix"))
        writer.writerows(blank_row)
        writer.writerows(quant_impact_arr)
        writer.writerows(blank_row)
        writer.writerows(build_header_row(cols, "Qualitative Impact Matrix"))
        writer.writerows(blank_row)
        writer.writerows(qual_impact_arr)
        writer.writerows(blank_row)
        writer.writerows(build_header_row(cols, "Final Matrix"))
        writer.writerows(blank_row)
        writer.writerows(final_arr)
        writer.writerows(blank_row)
        writer.writerows(build_header_row(cols, "Final Alternative Scores"))
        writer.writerows(blank_row)
        writer.writerows(final_score_arr)
        #writer.writerows(comments)
        
        self.export_analysis_dialog.hide()
        self.export_analysis_dialog.deleteLater()
        QMessageBox.information(self,"Template Exported", "Analysis was successfully exported to "+filename)
    
    def start_delete_analysis(self):
        try:
            selected_id = self.mca_runs_table.get_selected_id()
        except DelphosError, e:
            QMessageBox.critical(self,"Analysis Delete Error", str(e.value))    
        else:
            self.yes_no_dialog = YesNoDialog(self, "Are you sure you want to delete this analysis run?")
            self.connect(self.yes_no_dialog, SIGNAL("delete_confirm"), self.finish_delete_analysis)
            self.yes_no_dialog.show()

    def finish_delete_analysis(self, confirm):
        if confirm is True:
            selected_id = self.mca_runs_table.get_selected_id()        
            try:
                self.project.delete_analysis(selected_id)
            except DelphosError, e:
                QMessageBox.critical(self,"Analysis Delete Error", str(e.value))
            else:
                self.mca_runs_table.load(self.project.get_mca_runs_basic())
        
        self.yes_no_dialog.hide()
        self.yes_no_dialog.deleteLater()
            
    def show_analysis_results(self, name, description, altern_data, crit_data, input_data, input_weights, results):
        self.mca_result_view = McaResultView(self.gui_manager, self, self.project)
        self.mca_result_view.load_results(name, description, altern_data, crit_data, input_data, input_weights, results)
        self.mca_result_view.show()

    ################################# General ##############################
        
    def process_current_change(self, index):
        """Loads the appropriate widget when the next button is clicked
        """
        #if tab was 3
        if self.cur_tab == 3:
            if self.save_button.isEnabled():
                response = QMessageBox.question(self, "Save Input", "You have new or modified input values.  Do you want to save them now?", QMessageBox.Yes, QMessageBox.No)
                if response == QMessageBox.Yes:
                    self.save_input()

        #if new tab is 3
        if index is 3:
            if self.cur_tab > 3 and not self.input_table.loaded:
                self.load_data_input()
            if self.cur_tab < 3:
                self.load_data_input()
                
        self.cur_tab = index