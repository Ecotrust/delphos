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
			del self.add_altern_dialog
			self.altern_table.load(self.project.get_all_alternatives())