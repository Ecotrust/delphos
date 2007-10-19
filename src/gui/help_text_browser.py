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

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HelpTextBrowser(QTextBrowser):
	def __init__(self, parent=None):
		QTextBrowser.__init__(self, parent)
	
	def setSource(self, url):
		list = url.path().split('/')
		
		#If less than 3 elements it's not a URL we care about
		if len(list) < 3:
			return
		
		type = list[1]
		
		#Don't change the browsers source if its an 'app' link.
		if type == 'app' or type == 'doc':
			return
		else:
			#change the browser source as normal
			QTextBrowser.setSource(self, url)

	def load_doc(self, project_type, language):
		doc_name = self.get_doc_name(project_type, language)
		self.setSource(QUrl(doc_name))
	
	def load_anchor(self, label, project_type, language):
		doc_name = self.get_doc_name(project_type, language)
		self.setSource(QUrl(doc_name+"#"+label))

	def get_doc_name(self, project_type, language):
		if project_type == 'fisheries':
			if language == 'english':
				return 'qrc:/documentation/fisheries_documentation_english.html'
			else:
				return 'qrc:/documentation/fisheries_documentation_spanish.html'
		else:
			if language == 'english':
				return 'qrc:/documentation/mpa_documentation_english.html'
			else:
				return 'qrc:/documentation/mpa_documentation_spanish.html'
							
if __name__ == "__main__":
	class HelpLoader(QMainWindow):
		def __init__(self, parent=None):
			QWidget.__init__(self, parent)
			self.help_browser = HelpTextBrowser(self)
			self.help_browser.setSource(QUrl('qrc:/blort/foo'))
			
	a = QApplication(sys.argv)
	app = HelpLoader()
	app.show()
	a.exec_()