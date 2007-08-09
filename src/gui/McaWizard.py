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
		self.cur_index = 0
		
		#Button Signals
		QObject.connect(self.altern_next_button,QtCore.SIGNAL("clicked()"), self.process_altern_select)
		QObject.connect(self.crit_next_button,QtCore.SIGNAL("clicked()"), self.process_crit_select)
		QObject.connect(self.input_next_button,QtCore.SIGNAL("clicked()"), self.process_data_input)
		QObject.connect(self.weight_next_button,QtCore.SIGNAL("clicked()"), self.process_weight_input)
		
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
		QObject.connect(self.mca_stack,QtCore.SIGNAL("currentChanged(int)"), self.process_current_change)
		
		self.setup_crit_select()		
		self.setup_altern_select()

	def setup_altern_select(self):
		self.altern_data = self.project.get_all_alternatives()
		self.altern_table.load(self.altern_data)		

	def setup_crit_select(self):
		self.crit_data = self.project.get_all_criteria()
		self.crit_table.load(self.crit_data)

	def setup_data_input(self):
		self.input_table.load(self.selected_altern_data, self.selected_crit_data)

	def setup_weight_input(self):
		#Reuse selected altern ids from 
		self.weight_table.load(self.selected_altern_data)

	def process_altern_select(self):
		selected_altern_indexes = self.altern_table.get_selected_indexes()
		if len(selected_altern_indexes) < 2:
			QMessageBox.critical(self,"Error", "You must select at least two alternatives")
		else:
			#Build list of selected altern data
			self.selected_altern_data = []
			for index in selected_altern_indexes:
				self.selected_altern_data.append(self.altern_data[index])
			self.next_click()
		
	def process_crit_select(self):
		selected_crit_indexes = self.crit_table.get_selected_indexes()
		if len(selected_crit_indexes) < 1:
			QMessageBox.critical(self,"Error", "You must select at least one criteria")
		else:
			#Build list of selected crit data
			self.selected_crit_data = []
			for index in selected_crit_indexes:
				self.selected_crit_data.append(self.crit_data[index])
			self.next_click()

	def process_data_input(self):
		#Get data from table
		input_data = self.input_table.get_input_data()
		if input_data:
			print input_data
			self.next_click()

	def process_weight_input(self):
		QMessageBox.critical(self,"Error", "Not Implemented")
		#self.next_click()

	def process_run(self):
		"""Processes clicking of 'Run Analysis' button
		"""
		analysis_info = []
		
		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("mca_analysis_info_collected"), analysis_info)

	def next_click(self):
		"""Shift stack forward one
		"""
		current_index = self.mca_stack.currentIndex()
		self.mca_stack.setCurrentIndex(current_index+1)

	def prev_click(self):
		"""Shift stack back one
		"""
		current_index = self.mca_stack.currentIndex()
		prev_widget = self.mca_stack.widget(current_index-1)
		self.mca_stack.setCurrentWidget(prev_widget)	

	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()
		self.deleteLater()
	
	def process_current_change(self, index):
		"""Loads the appropriate widget when the next button is clicked
		"""
		if self.cur_index < index:
			if index is 2:
				self.setup_data_input()
			elif index is 3:
				self.setup_weight_input()
			elif index is 4:
				self.setup_run()
		self.cur_index = index
			