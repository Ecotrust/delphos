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
# @summary - defines a special help button in delphos in which the button name
# itself defines the type of help that is needed.  Signals for help when 
# clicked
#===============================================================================

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HelpButton(QPushButton):
	def __init__(self, parent=None):
		QPushButton.__init__(self, parent)
		QObject.connect(self,QtCore.SIGNAL("clicked()"), self.__help_click)
	
	def __help_click(self):
		#Call for help and use button name to specify what kind of help
		#Spanish name is stored in accessibleName, very much a hack
		self.emit(SIGNAL("help_button_clicked"), self.objectName(), self.accessibleDescription())