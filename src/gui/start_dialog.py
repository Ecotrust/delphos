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

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from start_ui import Ui_StartDialog


class StartDialog(QDialog, Ui_StartDialog):
	"""Manages the initial startup dialog
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		QObject.connect(self.start_button_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.start_button_box,QtCore.SIGNAL("rejected()"), self.process_reject)

	def process_accept(self):
		"""Processes clicking of OK button in startup dialog
		"""
		if self.start_project_button.isChecked():
			self.hide()
			self.gui_manager.start_project_creation()
		elif self.open_project_button.isChecked():
			self.hide()
			self.gui_manager.start_project_opening()
		else:
			QMessageBox.critical(self,"Delphos","Please choose whether you would like to start a new project or open an existing one")

	def process_reject(self):
		"""Processes clicking of Cancel button in startup dialog
		"""
		self.hide()
		