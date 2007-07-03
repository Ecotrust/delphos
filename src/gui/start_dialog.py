from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from start_ui import Ui_StartDialog

class StartDialog(QDialog, Ui_StartDialog):
	"""Manages the initial startup dialog
	"""
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		QObject.connect(self.start_button_box,QtCore.SIGNAL("accepted()"), self.process_start)

	def process_start(self):
		"""Processes the startup dialog when the OK button has been clicked
		"""

		if self.start_project_button.isChecked():
			print "Create a new project already!"
		elif self.open_project_button.isChecked():
			print "Open an existing project already!"