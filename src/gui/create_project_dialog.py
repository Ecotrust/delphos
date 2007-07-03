from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from create_project_ui import Ui_CreateProjectDialog

class CreateProjectDialog(QDialog, Ui_CreateProjectDialog):
	"""Manages the initial startup dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		QObject.connect(self.create_button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.create_button_box,QtCore.SIGNAL("rejected()"), self.process_reject)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		project_type = ""
		project_path = ""
		isError = False
		
		if self.mpa_type_button.isChecked():
			project_type = "mpa"
		elif self.fisheries_type_button.isChecked():
			project_type = "fisheries"
		else:
			isError = True
			QMessageBox.critical(self,"Delphos","Please select \"Fisheries\" or \"Marine Protected Areas\"")
		
		project_path = self.project_path_edit.text()
		if not project_path:
			isError = True;
			QMessageBox.critical(self,"Delphos","Please enter a project directory path and name by clicking the \"Browse\" button, selecting a file directory and then entering a project name")

		if not isError:
			self.hide()
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()