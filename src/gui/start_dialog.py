from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from start_ui import Ui_StartDialog


class StartDialog(QDialog, Ui_StartDialog):
	"""Manages the initial startup dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		QObject.connect(self.start_button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.start_button_box,QtCore.SIGNAL("rejected()"), self.process_reject)

	def process_accept(self):
		"""Processes clicking of OK button in startup dialog
		"""
		if self.start_project_button.isChecked():
			self.hide()
			self.gui_manager.start_project_creation()
		elif self.open_project_button.isChecked():
			self.hide()
			self.gui_manager.open_existing_project()
		else:
			QMessageBox.critical(self,"Delphos","Please choose whether you would like to start a new project or open an existing one")

	def process_reject(self):
		"""Processes clicking of Cancel button in startup dialog
		"""
		self.hide()
		