import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from add_alternative_ui import Ui_AddAlternDialog

class AddAlternDialog(QDialog, Ui_AddAlternDialog):
	"""Manages the add alternative dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
		
		#Connect slots to signals
		QObject.connect(self.add_alternative_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.add_alternative_box,QtCore.SIGNAL("rejected()"), self.process_reject)
		QObject.connect(self.alternative_name_edit,QtCore.SIGNAL("returnPressed()"), self.process_accept)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		alternative_name = self.alternative_name_edit.text()

		if not alternative_name:
			self.isError = True
			QMessageBox.critical(self,"Delphos", "Please enter an alternative name")

		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("add_alternative_info_collected"), str(alternative_name))
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()
		self.deleteLater()