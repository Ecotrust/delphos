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

from mca_rerun_ui import Ui_McaRerunDialog

class McaRerunDialog(QDialog, Ui_McaRerunDialog):
	"""Manages the add alternative dialog
	"""
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent	
		QObject.connect(self.restart_analysis_button,QtCore.SIGNAL("clicked()"), self.process_input)
        self.retranslate() #Translate the UI
        
	def process_input(self):
		name = self.analysis_name_edit.text()
		if not name:
			QMessageBox.critical(self,self.analysis_error, self.analysis_error_text)
			return False;
		description = self.analysis_description_edit.text()
		self.emit(SIGNAL("mca_rerun_info_collected"), name, description)
        
    def retranslate(self):
       self.analysis_error = QApplication.translate("McaRerunDialog", "Analysis Error", "error name", QApplication.UnicodeUTF8)
       self.analysis_error_text = QApplication.translate("McaRerunDialog", "You must enter a name for this analysis", "", QApplication.UnicodeUTF8)