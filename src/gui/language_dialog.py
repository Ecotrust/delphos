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

from language_dialog_ui import Ui_LanguageDialog

class LanguageDialog(QDialog, Ui_LanguageDialog):
	"""Dialog allowing user to select language to use
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		
		#Connect slots to signals
		QObject.connect(self.english_button,QtCore.SIGNAL("clicked()"), self.english_selection)
		QObject.connect(self.spanish_button,QtCore.SIGNAL("clicked()"), self.spanish_selection)
		
	def english_selection(self):
		self.emit(SIGNAL("language_selected"), "english")
		
	def spanish_selection(self):
		self.emit(SIGNAL("language_selected"), "spanish")