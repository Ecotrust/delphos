import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from project_view_ui import Ui_ProjectView
from add_alternative_dialog import AddAlternDialog
from add_criteria_dialog import AddCriteriaDialog

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
        QObject.connect(self.new_analysis_button,QtCore.SIGNAL("clicked()"), self.start_new_analysis)
        self.load_project_data_tab()
        self.altern_table.load(self.project.get_all_alternatives())
        self.crit_table.load(self.project.get_all_criteria())

    def load_project_data_tab(self):
        try:
            (project_name, project_type, project_created) = self.project.get_project_data()
        except DelphosError, r:
            QMessageBox.critical(self,"Delphos", "Project data not found")
        else:            
            self.project_name.setText(project_name)
            self.project_type.setText(project_type)
            self.project_created.setText(str(project_created))
    
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
            print "cur_row: "+str(cur_row_item)
        except DelphosError, e:
            QMessageBox.critical(self,"Please select or add an alternative first.", str(e))
        else:
            if cur_row_item:
                success = self.project.remove_alternative_by_name(str(cur_row_item.text()))
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

    def start_view_analysis(self):
        pass

    def start_new_analysis(self):
        pass