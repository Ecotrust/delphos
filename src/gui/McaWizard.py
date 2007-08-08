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
		
		#Button Signals
		QObject.connect(self.altern_next_button,QtCore.SIGNAL("clicked()"), self.next_click)
		QObject.connect(self.crit_next_button,QtCore.SIGNAL("clicked()"), self.next_click)
		QObject.connect(self.input_next_button,QtCore.SIGNAL("clicked()"), self.next_click)
		QObject.connect(self.weight_next_button,QtCore.SIGNAL("clicked()"), self.next_click)
		
		QObject.connect(self.crit_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
		QObject.connect(self.input_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
		QObject.connect(self.weight_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
		QObject.connect(self.run_prev_button,QtCore.SIGNAL("clicked()"), self.prev_click)
			
		QObject.connect(self.altern_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.crit_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.input_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.weight_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		QObject.connect(self.run_cancel_button,QtCore.SIGNAL("clicked()"), self.process_reject)
		
		QObject.connect(self.run_analysis_button,QtCore.SIGNAL("clicked()"), self.process_run)
		
		#Other signals
		QObject.connect(self.mca_tab_widget,QtCore.SIGNAL("currentChanged(int)"), self.process_tab_change)
		QObject.connect(self, QtCore.SIGNAL("input_data_tab_displayed"), self.setup_input_tab)		

		#Load tabs
		self.setup_alternative_tab()
		self.setup_criteria_tab()

	def setup_alternative_tab(self):
		self.altern_data = self.project.get_all_alternatives()
		self.altern_table.load(self.altern_data)
	
	def setup_criteria_tab(self):
		self.crit_data = self.project.get_all_criteria()
		self.crit_table.load(self.crit_data)

	def setup_input_tab(self):
		selected_altern_ids = self.altern_table.get_selected_ids()
		selected_crit_ids = self.crit_table.get_selected_ids()
		if not selected_altern_ids or not selected_crit_ids:
			QMessageBox.critical(self,"Input Error", "Reminder: before inputting data, you must first select alternatives and criteria to include.")
		self.input_table.load(self.altern_data, self.crit_data, selected_altern_ids, selected_crit_ids)

	def process_run(self):
		"""Processes clicking of OK button in dialog
		"""
		analysis_info = []
		
		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("mca_analysis_info_collected"), analysis_info)

	def next_click(self):
		current_index = self.mca_tab_widget.currentIndex()
		print "current index: "+str(current_index)
		next_widget = self.mca_tab_widget.widget(current_index+1)
		self.mca_tab_widget.setCurrentWidget(next_widget)

	def prev_click(self):
		current_index = self.mca_tab_widget.currentIndex()
		print "current index: "+str(current_index)
		prev_widget = self.mca_tab_widget.widget(current_index-1)
		self.mca_tab_widget.setCurrentWidget(prev_widget)	

	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()
		self.deleteLater()
	
	def process_tab_change(self, new_tab):
		if self.mca_tab_widget.tabText(new_tab) == "Input Data":
			self.emit(SIGNAL("input_data_tab_displayed"))