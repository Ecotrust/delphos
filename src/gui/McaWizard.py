import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mca_wizard_ui import Ui_McaWizard

class McaWizard(QDialog, Ui_McaWizard):
	"""Manages the collection of MCA analysis input
	"""
	def __init__(self, gui_manager, parent, project):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.project = project
		self.gui_manager = gui_manager
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
		
		#Connect slots to signals
		QObject.connect(self.run_analysis_button,QtCore.SIGNAL("clicked()"), self.process_run)
		QObject.connect(self.altern_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.crit_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.input_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.weight_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.run_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)

		self.setup_alternative_table()
		self.setup_criteria_table()

	def setup_alternative_table(self):		
		self.altern_table.load(self.project.get_all_alternatives())
	
	def setup_criteria_table(self):
		self.criteria_table.load(self.project.get_all_criteria())
	
	def process_run(self):
		"""Processes clicking of OK button in dialog
		"""
		analysis_info = []
		
		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("mca_analysis_info_collected"), analysis_info)
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()
		self.deleteLater()