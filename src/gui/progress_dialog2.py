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
# $Id: ProgressDialog2.py 117 2007-12-21 19:14:00Z timw $
#
# @summary - 
#===============================================================================

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from progress_dialog2_ui import Ui_ProgressDialog2

class ProgressDialog2(QDialog, Ui_ProgressDialog2):
	"""Manages the progress bar
	"""
	def __init__(self, title):
		QDialog.__init__(self, None)
		self.setupUi(self)
		self.timer_label.setText(title)
		
#		self.counter = 0	
#		self.timer = QTimer()
#		self.timer.setInterval(250)
#		QObject.connect(self.timer,QtCore.SIGNAL("timeout()"), self.increment_progress)

	def start(self):
		self.timer.start()
	
	def stop(self):
		self.timer.stop()

	def increment_progress(self):
		#print "timeout!"
		self.counter += 1
		self.progress_bar.setValue(self.counter % 4)
