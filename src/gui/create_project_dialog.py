#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
# @license		GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id$
#
# @summary - 
#===============================================================================

import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from create_project_ui import Ui_CreateProjectDialog

class CreateProjectDialog(QDialog, Ui_CreateProjectDialog):
	"""Manages the initial startup dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		self.isError = False	#Error flag for form processing
		self.errorMsg = ""
		self.default_file_extension = ".dlp"
		self.project_path = None
		
		type_group = QButtonGroup(self)
		type_group.addButton(self.mpa_type_button)
		type_group.addButton(self.fisheries_type_button)
		sub_type_group = QButtonGroup(self)
		sub_type_group.addButton(self.communities_sub_type_button)
		sub_type_group.addButton(self.sites_sub_type_button)
		
		#Connect slots to signals
		QObject.connect(self.project_browse_button,QtCore.SIGNAL("clicked()"), self.process_browse)
		QObject.connect(self.fisheries_type_button,QtCore.SIGNAL("clicked()"), self.process_fisheries_click)
		QObject.connect(self.mpa_type_button,QtCore.SIGNAL("clicked()"), self.process_mpa_click)
		QObject.connect(self.create_button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.create_button_box,QtCore.SIGNAL("rejected()"), self.process_reject)
		self.default_altern_check.hide()

	def process_fisheries_click(self):
		self.communities_sub_type_button.setEnabled(False)
		self.sites_sub_type_button.setEnabled(False)
	
	def process_mpa_click(self):
		self.communities_sub_type_button.setEnabled(True)
		self.sites_sub_type_button.setEnabled(True)
	
	def process_browse(self):
		"""Processes clicking of browse button
		"""
		fd = QtGui.QFileDialog(self)
		fd.setFileMode(QFileDialog.AnyFile)
		full_name = fd.getSaveFileName()

		self.filename = path.basename(str(full_name))
		self.project_path = path.dirname(str(full_name))

		#Check if filename and if extension already added
		if self.filename and not re.search('[.]dlp$', self.filename):
			self.filename += self.default_file_extension

		full_name = self.project_path + os.sep + self.filename

		if path.isfile(full_name):
			try:
				os.remove(full_name)
			except OSError, e:
				QMessageBox.critical(self,"File Error", "Error while overwriting the existing project "+e)

		#Put path & filename into textbox
		
		self.project_path_edit.setText(full_name)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		self.project_type = ""
		
		if self.mpa_type_button.isChecked():
			if self.communities_sub_type_button.isChecked():
				self.project_type = "communities"
			elif self.sites_sub_type_button.isChecked():
				self.project_type = "sites"
			else:
				self.isError = True
				self.errorMsg += "Please select \"Communities\" or \"Sites\n"
				
		elif self.fisheries_type_button.isChecked():
			self.project_type = "fisheries"
		else:
			self.isError = True
			self.errorMsg += "Please select \"Fisheries\" or \"Marine Protected Areas\n"

		if not self.project_path:
			self.isError = True;
			self.errorMsg += "Please enter a project path and name by clicking the browse button"

		if self.isError:
			QMessageBox.critical(self,"Delphos",self.errorMsg)
			self.errorMsg = ""
			self.isError = False
		else:
			self.emit(SIGNAL("create_project_info_collected"), self.filename, self.project_path, self.project_type, self.default_altern_check.checkState(), self.default_crit_check.checkState())
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()