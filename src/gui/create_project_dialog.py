import os
import re
from os import path

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
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
		self.default_file_extension = ".del"
		
		#Connect slots to signals
		QObject.connect(self.project_browse_button,QtCore.SIGNAL("clicked()"), self.process_browse)
		QObject.connect(self.create_button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.create_button_box,QtCore.SIGNAL("rejected()"), self.process_reject)

	def process_browse(self):
		"""Processes clicking of browse button
		"""
		fd = QtGui.QFileDialog(self)
		fd.setFileMode(QFileDialog.AnyFile)
		full_name = fd.getSaveFileName()

		self.filename = path.basename(str(full_name))
		self.project_path = path.dirname(str(full_name))

		#Check if filename and if extension already added
		if self.filename and not re.search('[.]del$', self.filename):
			self.filename += self.default_file_extension

		full_name = self.project_path + os.sep + self.filename

		if path.isfile(full_name):
			try:
				print "got here"
				os.remove(full_name)
			except OSError, e:
				QMessageBox.critical(self,"File Error", "Error while overwriting the existing project "+e)

		#Put path & filename into textbox
		self.project_path_edit.setText(full_name)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		self.project_type = ""
		
		if self.mpa_type_button.isChecked():
			self.project_type = "mpa"
		elif self.fisheries_type_button.isChecked():
			self.project_type = "fisheries"
		else:
			self.isError = True
			self.errorMsg += "Please select \"Fisheries\" or \"Marine Protected Areas\n"

		if not self.project_path:
			self.isError = True;
			self.errorMsg += "Please enter a project path and name by clicking the browse button"

		if self.isError:
			QMessageBox.critical(self,"Delphos",self.errorMsg)
			self.isError = False
		else:
			self.gui_manager.finish_project_creation()
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()

	def get_project_type(self):
		"""Get project type selected by user
		"""
		return self.project_type
		
	def get_project_path(self):
		"""Get project path and name selected by user
		"""
		return self.project_path
	
	def get_project_filename(self):
		"""Get project filename entered by user
		"""
		return self.filename
	
	def do_load_default_altern(self):
		return self.default_altern_check.checkState()
	
	def do_load_default_crit(self):
		return self.default_crit_check.checkState()