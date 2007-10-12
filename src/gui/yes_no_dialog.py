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

from yes_no_ui import Ui_YesNoDialog

class YesNoDialog(QDialog, Ui_YesNoDialog):
	"""Manages the add alternative dialog
	"""
	def __init__(self, parent, message):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.errorMsg = ""
		
		#Connect slots to signals
		QObject.connect(self.confirm_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.confirm_box,QtCore.SIGNAL("rejected()"), self.process_reject)

		self.message_label.setText(message)

	def process_accept(self):
		"""Processes clicking of Yes button in dialog
		"""
		self.emit(SIGNAL("delete_confirm"), True)
			
	def process_reject(self):
		"""Processes clicking of No button in dialog
		"""
		self.emit(SIGNAL("delete_confirm"), False)