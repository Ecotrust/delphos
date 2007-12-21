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
		
		#Get doc stylesheet
		doc_style_qss = QFile(":/qss/help_doc.css")
		doc_style_qss.open(QIODevice.ReadOnly)
		self.doc_style_str = str(doc_style_qss.readAll())
		doc_style_qss.close()
		
		print self.doc_style_str
		

	
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
		self.setStyleSheet(QString(self.doc_style_str))	
	
	def load_anchor(self, label, project_type, language):
		doc_name = self.get_doc_name(project_type, language)
		self.setSource(QUrl(doc_name+"#"+label))

	def get_doc_name(self, project_type, language):
		if project_type == 'fisheries':
			if language == 'english':
				return 'qrc:/documentation/fisheries/english/documentation.html'
			else:
				return 'qrc:/documentation/fisheries/spanish/documentation.html'
		else:
			if language == 'english':
				return 'qrc:/documentation/mpa/english/documentation.html'
			else:
				return 'qrc:/documentation/mpa/spanish/documentation.html'
							
if __name__ == "__main__":
	from resources_rc import *

	class HelpLoader(QMainWindow):
		def __init__(self, parent=None):
			QWidget.__init__(self, parent)
			self.help_browser = HelpTextBrowser(self)
			#self.help_browser.setSource(QUrl('qrc:/documentation/fisheries_documentation_english.html'))
			self.help_browser.setHtml("<a href='qrc:/doc/fisheries_general_questionnaire.doc'>link</a>")
			QObject.connect(self.help_browser, SIGNAL("anchorClicked(QUrl)"), self.anchor_click_handler)

		def anchor_click_handler(self, url):
			print url.path()
			list = url.path().split('/')
			
			#If less than 3 elements it's not a URL we care about
			for item in list:
				print item
			print len(list)
			if len(list) < 3:
				return
			#Extract 'keywords' from path
			type = list[1]
			action = list[2]
	
			if type == 'app':
				if action == 'create_project':
					self.start_project_creation()
			
			elif type == 'doc':
				doc_path = os.getcwd()+os.sep+"documentation"+os.sep+action
				print doc_path
				doc_url = "file:"+urllib.pathname2url(unicode(doc_path))
				print "doc_url"
				print doc_url
				self.desktop_services.openUrl(QUrl(doc_url))

	a = QApplication(sys.argv)
	app = HelpLoader()
	app.show()
	a.exec_()