import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from project_view_ui import Ui_ProjectView
from add_alternative_dialog import AddAlternDialog

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

		self.load_project_data_tab()
		self.load_alternative_table()
		self.load_criteria_table()

	def load_project_data_tab(self):
		try:
			(project_name, project_type, project_created) = self.project.get_project_data()
		except DelphosError, r:
			QMessageBox.critical(self,"Delphos", "Project data not found")
		else:			
			self.project_name.setText(project_name)
			self.project_type.setText(project_type)
			self.project_created.setText(str(project_created))
			
	def load_alternative_table(self):
		"""Loads the table in the alternatives tab with the existing project alternatives
		"""
		alternative_recs = self.project.get_all_alternatives()
		self.altern_table.setColumnCount(1)
		self.altern_table.setRowCount(len(alternative_recs))
		
		for i in range(len(alternative_recs)):
			item = QTableWidgetItem()
			item.setText(str(alternative_recs[i][1]))
			self.altern_table.setItem(i, 0, item)
		self.altern_table.resizeColumnsToContents()
	
	def load_criteria_table(self):
		"""Loads the table in the criteria tab with the existing project criteria
		"""
		criteria_recs = self.project.get_all_criteria()
		print criteria_recs
		self.crit_table.setColumnCount(3)
		self.crit_table.setRowCount(len(criteria_recs))
		
		for i in range(len(criteria_recs)):
			name_item = QTableWidgetItem()
			name_item.setText(str(criteria_recs[i][1]))
			self.crit_table.setItem(i, 0, name_item)

			type_item = QTableWidgetItem()
			type_item.setText(str(criteria_recs[i][2]))
			self.crit_table.setItem(i, 1, type_item)

			cb_item = QTableWidgetItem()
			cb_item.setText(str(criteria_recs[i][3]))
			self.crit_table.setItem(i, 2, cb_item)

		self.crit_table.resizeColumnsToContents()
	
	def start_add_alternative(self):
		"""Create dialog for adding an alternative
		"""
		#Load add alternative dialog form
		self.add_altern_dialog = AddAlternDialog(self.gui_manager, self)
		self.connect(self.add_altern_dialog, SIGNAL("add_alternative_info_collected"), self.finish_add_alternative)
		self.add_altern_dialog.show()
	
	def finish_add_alternative(self, alternative_name):
		"""Add alternative given its name from dialog
		"""
		self.add_altern_dialog.hide()
		del self.add_altern_dialog
		print alternative_name
		return
		try:
			self.project.add_altern(project_filename, project_path)
		except DelphosError, e:
			QMessageBox.critical(self.open_proj_dialog,"Project Open Error", "Project opening failed: "+str(e))
		else:
			self.open_proj_dialog.close()
			self.start_project_display()