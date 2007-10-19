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

from credits_dialog_ui import Ui_CreditsDialog

class CreditsDialog(QDialog, Ui_CreditsDialog):
	"""Dialog allowing user to select language to use
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.gui_manager = gui_manager
		QObject.connect(self.wwf_label, SIGNAL("linkActivated(QString)"), self.anchor_click_handler)
		QObject.connect(self.cobi_label, SIGNAL("linkActivated(QString)"), self.anchor_click_handler)
		QObject.connect(self.ecotrust_label, SIGNAL("linkActivated(QString)"), self.anchor_click_handler)
	
	def anchor_click_handler(self, url):
		self.gui_manager.desktop_services.openUrl(QUrl(url))