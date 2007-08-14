import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from add_criteria_ui import Ui_AddCriteriaDialog
from AddOrdinalOptionDialog import AddOrdinalOptionDialog

class AddCriteriaDialog(QDialog, Ui_AddCriteriaDialog):
	"""Manages the add alternative dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
		self.ordinal_option_list = []
		
		#Connect slots to signals
		QObject.connect(self.add_criteria_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.add_ordinal_option_button,QtCore.SIGNAL("clicked()"), self.start_add_ordinal_option)
		QObject.connect(self.remove_ordinal_option_button,QtCore.SIGNAL("clicked()"), self.handle_remove_ordinal_option)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		
		Raises signal 'add_criteria_info_collected' along with structure containing all of the collected criteria data
		as (criteria description - str, criteria type - str, type specific data - str or list, cost/benefit - str)
		Calls for deletion of self when done s
		"""
		self.errorMsg = ""
		criteria_info = None	#Holds all of the collected data including the type_info.  passed to observers
		type_info = None	#Holds collected data relative to the criteria type
		cost_benefit = None
		
		criteria_description = self.criteria_description_edit.text()
		if not criteria_description:
			self.isError = True
			self.errorMsg += "* Please enter a description of the criterion.\n"
		
		current_tab = self.criteria_type_tab.currentWidget()		
		if not current_tab:
			self.isError = True
			self.errorMsg += "* Please select a criteria type (ratio, binary, ordinal) and enter the appropriate information\n"
		
		current_tab_name = self.criteria_type_tab.tabText(self.criteria_type_tab.currentIndex())
		
		if current_tab_name == "Ratio":
			ratio_description = self.ratio_description_edit.text()
			if not ratio_description:
				self.isError = True
				self.errorMsg += "* Please enter a description of the quantitative ratio value.\n"
			if not self.isError:
				type_info = str(ratio_description)
				
		elif current_tab_name == "Binary":
			binary_yes_description = self.binary_yes_edit.text()
			binary_no_description = self.binary_no_edit.text()
			if not binary_yes_description:
				self.isError = True
				self.errorMsg += "* Please enter a \"Yes\" description\n"
			if not binary_no_description:
				self.isError = True
				self.errorMsg += "* Please enter a \"No\" description\n"
			if not self.isError:
				type_info = [[str(binary_yes_description), 2],[str(binary_no_description), 1]]
				
		elif current_tab_name == "Ordinal":
			type_info = self.ordinal_option_list
			
		else:
			self.isError = True
			self.errorMsg += "Delphos", "Criteria add failed unexpectedly.\n"

		if self.benefit_button.isChecked():
			cost_benefit = "B"
		elif self.cost_button.isChecked():
			cost_benefit = "C"
		else:
			self.isError = True
			self.errorMsg += "* Please define criterion as a \"Benefit\" or \"Cost\n"

		if self.isError:
			self.isError = False
			QMessageBox.critical(self,"Error adding criteria",self.errorMsg)
		else:
			criteria_info = [str(criteria_description), str(current_tab_name), type_info, cost_benefit]
			self.emit(SIGNAL("add_criteria_info_collected"), criteria_info)
			self.deleteLater()

	def start_add_ordinal_option(self):
		self.add_ordinal_option_dialog = AddOrdinalOptionDialog(self.gui_manager, self)
		self.connect(self.add_ordinal_option_dialog, SIGNAL("ordinal_option_info_collected"), self.finish_add_ordinal_option)
		self.add_ordinal_option_dialog.show()
	
	def finish_add_ordinal_option(self, option_info):
		self.ordinal_option_list.append(option_info)
		self.ordinal_option_table.load(self.ordinal_option_list)

	def handle_remove_ordinal_option(self):
		if not self.ordinal_option_list:
			QMessageBox.critical(self,"Error Removing Option", "There are no options")
			return
		
		try:
			cur_row = self.ordinal_option_table.get_current_row()
		except DelphosError, e:
			QMessageBox.critical(self,"Error Removing Option", str(e))
		else:
			#Remove selected row
			self.ordinal_option_list.pop(cur_row)
			#Reload the table
			self.ordinal_option_table.load(self.ordinal_option_list)
	
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.deleteLater()
		self.hide()