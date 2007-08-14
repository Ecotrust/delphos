import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from open_project_ui import Ui_OpenProjectDialog

class OpenProjectDialog(QDialog, Ui_OpenProjectDialog):
	"""Manages the open project dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
		self.default_file_extension = "del"	#Also defined in accept regex below
		
		self.filename = ""
		self.project_path = ""
		
		#Connect slots to signals
		QObject.connect(self.project_browse_button,QtCore.SIGNAL("clicked()"), self.process_browse)
		QObject.connect(self.open_button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.open_button_box,QtCore.SIGNAL("rejected()"), self.process_reject)

	def process_browse(self):
		"""Processes clicking of browse button
		"""
		fd = QtGui.QFileDialog(self)
		fd.setFileMode(QFileDialog.ExistingFile)
		fd.setFilter("*.del")
		full_name = fd.getOpenFileName()

		self.filename = path.basename(str(full_name))
		self.project_path = path.dirname(str(full_name))

		#Put path & filename into textbox
		self.project_path_edit.setText(full_name)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		self.project_type = ""

		if not self.filename:
			self.isError = True
			QMessageBox.critical(self,"Delphos", "Please select a project by clicking the browse button")
		elif not re.search('[.]'+self.default_file_extension+'$', self.filename):
			self.isError = True
			QMessageBox.critical(self,"Delphos", "You did not choose a valid Delphos project file.  A delphos project file should end in ."+self.default_file_extension)


		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("open_project_info_collected"), self.filename, self.project_path)
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()