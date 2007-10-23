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

        QObject.connect(self.add_altern_button,QtCore.SIGNAL("clicked()"), self.start_add_alternative)
        QObject.connect(self.remove_altern_button,QtCore.SIGNAL("clicked()"), self.start_remove_alternative)
        QObject.connect(self.add_criteria_button,QtCore.SIGNAL("clicked()"), self.start_add_criteria)
        QObject.connect(self.remove_criteria_button,QtCore.SIGNAL("clicked()"), self.start_remove_criteria)
        QObject.connect(self.view_analysis_button,QtCore.SIGNAL("clicked()"), self.start_view_analysis)
        QObject.connect(self.rerun_analysis_button,QtCore.SIGNAL("clicked()"), self.start_rerun_analysis1)
        QObject.connect(self.export_analysis_button,QtCore.SIGNAL("clicked()"), self.start_export_analysis)
        QObject.connect(self.delete_analysis_button,QtCore.SIGNAL("clicked()"), self.start_delete_analysis)
        QObject.connect(self.new_analysis_button,QtCore.SIGNAL("clicked()"), self.start_new_analysis)
        self.load_project_data_tab()
        self.altern_table.load(self.project.get_all_alternatives())
        self.crit_table.load(self.project.get_all_criteria())
        self.mca_runs_table.load(self.project.get_mca_runs_basic())

    def load_project_data_tab(self):
        try:
            (project_name, project_type, project_created) = self.project.get_project_data()
        except DelphosError, r:
            QMessageBox.critical(self,"Delphos", "Project data not found")
        else:            
            self.project_name.setText(project_name)
            self.project_type.setText(project_type)
            self.project_created.setText(unicode(project_created))
            self.num_runs_label.setText(unicode(self.project.get_num_mca_runs()))
    
    def start_add_alternative(self):
        """Create dialog for adding an alternative
        """
        #Load add alternative dialog form
        self.add_altern_dialog = AddAlternDialog(self.gui_manager, self)
        #Register handler for signal that alternative info has been collected and can be added
        self.connect(self.add_altern_dialog, SIGNAL("add_alternative_info_collected"), self.finish_add_alternative)
        self.add_altern_dialog.show()
    
    def finish_add_alternative(self, alternative_name):
        """Add alternative given its name from dialog
        """
        try:
            self.project.add_alternative(alternative_name)
        except DelphosError, e:
            QMessageBox.critical(self.add_altern_dialog,"Alternative Error", str(e))
        else:
            self.add_altern_dialog.close()
            self.add_altern_dialog.deleteLater()
            self.altern_table.load(self.project.get_all_alternatives())
    
    def start_remove_alternative(self):
        try:
            cur_row_item = self.altern_table.get_current_row_items()
        except DelphosError, e:
            QMessageBox.critical(self,"Please select or add an alternative first.", str(e))
        else:
            if cur_row_item:
                success = self.project.remove_alternative_by_name(unicode(cur_row_item.text()))
                if not success:
                    QMessageBox.critical(self,"Remove Alternative Error", "Failed to remove alternative.")
                else:
                    self.altern_table.load(self.project.get_all_alternatives())
            else:
                QMessageBox.critical(self,"Remove Alternative Error", "You must first select an alternative.")
    
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
            QMessageBox.critical(self.add_criteria_dialog,"Criteria Error", str(e))
        else:
            self.add_criteria_dialog.close()
            self.add_criteria_dialog.deleteLater()
            print "reloading"
            self.crit_table.load(self.project.get_all_criteria())

    def start_remove_criteria(self):
        cur_item = self.crit_table.get_current_row_items()
        if cur_item:
            success = self.project.remove_criteria_by_description(str(cur_item.text()))
            if not success:
                QMessageBox.critical(self,"Remove Criteria Error", "Failed to remove criteria.")
            else:
                self.crit_table.load(self.project.get_all_criteria())
        else:
            QMessageBox.critical(self,"Remove Criteria Error", "You must first select one from the criteria table.")

    def start_new_analysis(self):
        self.analysis_name = self.analysis_name_edit.text()
        self.analysis_description = self.analysis_description_edit.text()
        if not self.analysis_name:
            QMessageBox.critical(self,"Analysis Error", "You must enter a name for this analysis")
        else:
            #Load mca wizard
            self.mca_wizard = McaWizard(self.gui_manager, self, self.project)
            self.connect(self.mca_wizard, SIGNAL("mca_analysis_info_collected"), self.finish_new_analysis)
            self.mca_wizard.show()
            
    def finish_new_analysis(self, altern_data, crit_data, input_data, input_weights, selected_crit_types):
        try:
            input_weights_copy = copy.deepcopy(input_weights)
            [final_scores, int_data] = self.project.run_mca(input_data, input_weights_copy, selected_crit_types)
        except DelphosError, e:
            QMessageBox.critical(self,"Evamix Error", str(e))
        else:
            if final_scores:
                self.mca_wizard.hide()
                self.mca_wizard.deleteLater()            
                self.project.save_analysis(self.analysis_name, self.analysis_description, altern_data, crit_data, input_data, input_weights, final_scores, int_data)

                self.mca_runs_table.load(self.project.get_mca_runs_basic())
                self.show_analysis_results(self.analysis_name, self.analysis_description, altern_data, crit_data, input_data, input_weights, final_scores)
            else:
                QMessageBox.critical(self,"Analysis Error", "MCA analysis failed.")


    def start_view_analysis(self):
        try:
            selected_id = self.mca_runs_table.get_selected_id()
        except InputError, e:
            QMessageBox.critical(self,"View Error", str(e))
        else:
            (id, name, description, altern_data, crit_data, input_data, input_weights, results, created, int_data) = self.project.get_mca_run_by_id(selected_id)
            self.show_analysis_results(name, description, altern_data, crit_data, input_data, input_weights, results)

    def start_rerun_analysis1(self):
        try:
            selected_id = self.mca_runs_table.get_selected_id()
            self.mca_data = self.project.get_mca_run_by_id(selected_id)
        except InputError, e:
            QMessageBox.critical(self,"Run Error", str(e))
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
        self.export_id = self.mca_runs_table.get_selected_id()
        if not self.export_id:
            QMessageBox.critical(self,"Selection Error", "No analysis runs have been selected")
            return
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
        selected_id = self.mca_runs_table.get_selected_id()
        if not selected_id:
            QMessageBox.critical(self,"Selection Error", "No analysis runs have been selected")
            return
        self.yes_no_dialog = YesNoDialog(self, "Are you sure you want to delete this analysis run?")
        self.connect(self.yes_no_dialog, SIGNAL("delete_confirm"), self.finish_delete_analysis)
        self.yes_no_dialog.show()

    def finish_delete_analysis(self, confirm):
        if confirm is True:
            selected_id = self.mca_runs_table.get_selected_id()        
            try:
                self.project.delete_analysis(selected_id)
            except DelphosError, e:
                QMessageBox.critical(self,"Analysis Delete Error", str(e))
            else:
                self.mca_runs_table.load(self.project.get_mca_runs_basic())
        
        self.yes_no_dialog.hide()
        self.yes_no_dialog.deleteLater()
            
    def show_analysis_results(self, name, description, altern_data, crit_data, input_data, input_weights, results):
        self.mca_result_view = McaResultView(self.gui_manager, self, self.project)
        self.mca_result_view.load_results(name, description, altern_data, crit_data, input_data, input_weights, results)
        self.mca_result_view.show()