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

from export_analysis_ui import Ui_ExportAnalysisDialog

class ExportAnalysisDialog(QDialog, Ui_ExportAnalysisDialog):
	"""Manages the initial startup dialog
	"""
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		
		self.isError = False
		self.errorMsg = ""
		
		#Connect slots to signals
		QObject.connect(self.browse_button,QtCore.SIGNAL("clicked()"), self.process_browse)
		QObject.connect(self.button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.button_box,QtCore.SIGNAL("rejected()"), self.process_reject)

	def process_browse(self):
		"""Processes clicking of browse button
		"""
		fd = QtGui.QFileDialog(self)
		fd.setFileMode(QFileDialog.AnyFile)
		self.filename = fd.getSaveFileName()

		#Check if filename and if extension already added
		if not re.search('[.]csv$', self.filename):
			self.filename += '.csv'

		if path.isfile(self.filename):
			try:
				os.remove(self.filename)
			except OSError, e:
				QMessageBox.critical(self,"File Error", "Error while overwriting the existing project "+e)
		
		self.path_edit.setText(self.filename)

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		if not self.filename:
			self.isError = True;
			self.errorMsg += "Please choose a filename by clicking the browse button"

		if self.isError:
			QMessageBox.critical(self,"Delphos",self.errorMsg)
			self.isError = False
		else:
			self.emit(SIGNAL("export_analysis_info_collected"), self.filename)
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()