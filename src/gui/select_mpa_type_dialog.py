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
# $Id: select_type_dialog.py 99 2007-10-19 21:15:10Z timw $
#
# @summary - 
#===============================================================================

import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from select_mpa_type_ui import Ui_SelectMpaTypeDialog

class SelectMpaTypeDialog(QDialog, Ui_SelectMpaTypeDialog):
	"""Dialog allowing user to select type of analysis to perform
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		
		#Connect slots to signals
		QObject.connect(self.communities_type_button,QtCore.SIGNAL("clicked()"), self.communities_selection)
		QObject.connect(self.sites_type_button,QtCore.SIGNAL("clicked()"), self.sites_selection)

	def closeEvent(self, event):
		"""Don't allow dialog to be closed without making a selection
		"""
		event.ignore()

	def communities_selection(self):
		self.emit(SIGNAL("mpa_type_selected"), "communities")
		
	def sites_selection(self):
		self.emit(SIGNAL("mpa_type_selected"), "sites")