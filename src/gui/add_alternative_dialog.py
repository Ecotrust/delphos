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

from add_alternative_ui import Ui_AddAlternDialog
from util.common_functions import *

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

		self.project = self.gui_manager.project_manager.get_current_project()

		#Setup initial altern color
		label_palette = self.new_color_label.palette();
		self.altern_color = self.project.get_next_altern_color()
		label_palette.setColor(QPalette.Window, QColor(self.altern_color));
		self.new_color_label.setAutoFillBackground(True)
		self.new_color_label.setPalette(label_palette);

		#Connect slots to signals
		QObject.connect(self.add_alternative_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.add_alternative_box,QtCore.SIGNAL("rejected()"), self.process_reject)
		QObject.connect(self.alternative_name_edit,QtCore.SIGNAL("returnPressed()"), self.process_accept)
		QObject.connect(self.change_color_button,QtCore.SIGNAL("clicked()"), self.change_altern_color)
		QObject.connect(self.help_define_alternatives, QtCore.SIGNAL("help_button_clicked"), self.gui_manager.win.process_help_click)

	def change_altern_color(self):
		label_palette = self.new_color_label.palette();
		self.altern_color = random_hex_color()
		label_palette.setColor(QPalette.Window, QColor(self.altern_color));
		self.new_color_label.setAutoFillBackground(True)
		self.new_color_label.setPalette(label_palette);		
		self.new_color_label.update()

	def process_accept(self):
		"""Processes clicking of OK button in dialog
		"""
		alternative_name = self.alternative_name_edit.text()

		if not alternative_name:
			self.isError = True
			QMessageBox.critical(self,"Delphos", "Please enter an alternative name")

		if not self.isError and self.altern_color == "#ffffff":
			self.isError = True
			QMessageBox.critical(self,"Delphos", "Sorry, there are no predefined colors left to assign to this alternative.. Please choose a new color other than white that can be distinguished from the other colors.")

		if self.isError:
			self.isError = False
		else:
			self.emit(SIGNAL("add_alternative_info_collected"), unicode(alternative_name), self.altern_color)
			
	def process_reject(self):
		"""Processes clicking of Cancel button in dialog
		"""
		self.hide()
		self.deleteLater()