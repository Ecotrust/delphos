import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mca_result_view_ui import Ui_McaResultView

class McaResultView(QDialog, Ui_McaResultView):
	"""Manages the viewing of MCA analysis results
	"""
	def __init__(self, gui_manager, parent, project):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.project = project
		self.gui_manager = gui_manager
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
	
	def load_results(self, name, description, altern_data, crit_data, input_data, input_weights, results):
		self.final_table.load(altern_data, results)