import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mca_wizard_ui import Ui_McaWizard
from util.common_functions import *
from util.unicode_csv import *

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
		self.default_template_extension = "csv"
		self.cur_index = 0
		
		#Contains field data for all alternatives selected, each row is a 
		#list of [altern_id, altern_name]
		self.selected_altern_data = []
		self.selected_altern_names = []
		self.num_selected_alternatives = 0
		self.altern_name_column = 1	#in altern_data type list
		
		#Contains field data for all criteria selected, each row is a
		#list of [crit_id, crit_name, crit_type, crit_options, crit_cost_benefit]
		self.selected_crit_data = []
		self.selected_crit_names = []
		self.num_selected_criteria = 0
		self.crit_name_column = 1
		self.crit_type_column = 2
		
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

		QObject.connect(self.export_button,QtCore.SIGNAL("clicked()"), self.process_template_export)
		QObject.connect(self.import_button,QtCore.SIGNAL("clicked()"), self.process_template_import)		
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
		self.weight_table.load(self.selected_crit_data)
	
	def setup_run(self):
		self.num_alternatives_label.setText(str(self.num_selected_alternatives))
		self.num_criteria_label.setText(str(self.num_selected_criteria))

	def process_altern_select(self):
		selected_altern_indexes = self.altern_table.get_selected_indexes()
		if len(selected_altern_indexes) < 2:
			QMessageBox.critical(self,"Error", "You must select at least two alternatives")
		else:
			#Build list of selected altern data
			self.selected_altern_data = []
			for index in selected_altern_indexes:
				self.selected_altern_data.append(self.altern_data[index])
				self.selected_altern_names.append(self.altern_data[index][self.altern_name_column])
			self.next_click()
		self.num_selected_alternatives = len(self.selected_altern_data)
		
	def process_crit_select(self):
		selected_crit_indexes = self.crit_table.get_selected_indexes()
		if len(selected_crit_indexes) < 1:
			QMessageBox.critical(self,"Error", "You must select at least one criteria")
		else:
			#Build list of selected crit data
			self.selected_crit_data = []
			self.selected_crit_types = []
			for index in selected_crit_indexes:
				crit = self.crit_data[index]
				self.selected_crit_data.append(crit)
				self.selected_crit_names.append(crit[self.crit_name_column])
				self.selected_crit_types.append(crit[self.crit_type_column])
			self.next_click()
		self.num_selected_criteria = len(self.selected_crit_data)

	def process_template_export(self):
		"""Creates a unicode CSV containing alternatives and criteria for quickly inputting data
		"""
		fd = QtGui.QFileDialog(self)
		fd.setFileMode(QFileDialog.AnyFile)
		self.template_filename = fd.getSaveFileName()
		#Check if filename and if extension already added
		if self.template_filename:
			if not re.search('[.]'+self.default_template_extension+'$', self.template_filename):
				self.template_filename += '.'+self.default_template_extension

			export_arr = initialize_str_array(self.num_selected_criteria+1, self.num_selected_alternatives+1)
			#add alternatives to first row leaving first cell blank
			export_arr[0] = [""]+self.selected_altern_names
			#add criteria to first column leaving first cell blank
			for i in range(self.num_selected_criteria):
				export_arr[i+1][0] = self.selected_crit_names[i]
			#output list to CSV. Use default encoding of system
    		writer = UnicodeWriter(open(self.template_filename, "wb"), csv.excel, 'utf-16')
    		writer.writerows(export_arr)
    		QMessageBox.critical(self,"Template Exported", "The template has been successfully exported to "+self.template_filename+"  Enter data into this template and re-save it, then select 'Import From CSV' to load it into Delphos.")

	def process_template_import(self):
		"""Reads in input from a template
		"""
		QMessageBox.critical(self,"Error", "Not Implemented")
		
	def process_data_input(self):
		#Get data from table
		self.input_data = self.input_table.get_input_data()
		if self.input_data:
			#for row in self.input_data
			#	print row
			self.next_click()

	def process_weight_input(self):
		self.input_weights = self.weight_table.get_input_weights()
		if self.input_weights:
			#print self.input_weights
			self.next_click()

	def process_run(self):
		"""Processes clicking of 'Run Analysis' button
		"""
		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("mca_analysis_info_collected"), self.input_data, self.input_weights, self.selected_crit_types)

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
			