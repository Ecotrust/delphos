import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from project_view_ui import Ui_ProjectView

class ProjectView(QDialog, Ui_ProjectView):
	"""Manages interaction with the project interface and the underlying DB
	
	Includes adding, removing, editing and displaying of project data and the sub interfaces needed
	to do that (eg. add new criteria subwindow).
	"""
	def __init__(self, gui_manager, project):
		QDialog.__init__(self, None)
		self.setupUi(self)
		self.gui_manager = gui_manager
		self.project = project
		
		self.load_project_data_tab()
	
	def load_project_data_tab(self):
		try:
			(project_name, project_type, project_created) = self.project.get_project_data()
		except DelphosError, r:
			QMessageBox.critical(self,"Delphos", "Project data not found")
		else:			
			self.project_name.setText(project_name)
			self.project_type.setText(project_type)
			self.project_created.setText(str(project_created))