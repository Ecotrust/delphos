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

from main_window_ui import Ui_MainWindow

import os
import urllib

class DelphosWindow(QMainWindow):
	"""Manages the main Delphos window interface (Ui_MainWindow)
	"""
	def __init__(self, gui_manager):
		QWidget.__init__(self, None)	#Initialize myself as a widget
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)	#Create the components of the window
		
		self.gui_manager = gui_manager
		
		self.dock_full_screen = False
		self.min_doc_dock_width = 200
		
		#Maximize the display to full size
		#self.showMaximized()
		
		QObject.connect(self.ui.menu_dock_visible, SIGNAL("triggered()"), self.toggle_documentation_window)
		QObject.connect(self.ui.dock_doc, SIGNAL("visibilityChanged(bool)"), self.toggle_dock_visible_menu)

		QObject.connect(self.ui.menu_dock_floating, SIGNAL("triggered()"), self.toggle_dock_float)
		QObject.connect(self.ui.dock_doc, SIGNAL("topLevelChanged(bool)"), self.toggle_dock_floating_menu)

		QObject.connect(self.ui.menu_open_full_doc, SIGNAL("triggered()"), self.load_full_doc)

		#self.ui.dock_doc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.load_toc()

	def load_full_doc(self):
		"""Load full documentation in help window
		"""

		#Find which documentation subdir to look in
		project_type = self.gui_manager.project_manager.get_current_project_type()
		language = self.gui_manager.config_manager.get_language()
		if project_type == 'fisheries':
			if language == 'english':
				doc_subdir = 'fisheries'+os.sep+'english'+os.sep
			else:
				doc_subdir = 'fisheries'+os.sep+'spanish'+os.sep
		else:
			if language == 'english':
				doc_subdir = 'mpa'+os.sep+'english'+os.sep
			else:
				doc_subdir = 'mpa'+os.sep+'spanish'+os.sep
		
		doc_path = os.getcwd()+os.sep+"documentation"+os.sep+doc_subdir+'documentation.html'
		doc_url = "file:"+urllib.pathname2url(unicode(doc_path))

		#file:///U|/dev/delphos/src/documentation/fisheries/english/letter_to_experts.doc
		self.gui_manager.desktop_services.openUrl(QUrl(doc_url))
									  
	def load_toc(self):
		"""Loads the table of contents within the dock widget
		"""
		fisheries_toc = [
			"Introduction",
			{"Background": [
			    "Program History",
			]}, 
			{"Multicriteria Analysis/Evamix": [
				"References"
			]},
			{"The Delphos Process": [
				"1. Define Your Goals",
				"2. Define Your Timeline",
				"3. Define the Region",
				"4. Identify Experts",
				{"5. Consult the Experts": [
					"Pre-Analysis Workshop",
					"The Questionnaire"
				]},
				"6. Review Recommendations",
				{"7. Design Your Database": [
					"Create New Project",
					"Define Alternatives",
					"Define Criteria",
					{"Input Data": [
					    "Inputting Data Directly",
					    "Importing Data",
					    "Data Gaps"
					]}
				]},
				{"8. Run Analysis":[
					"Select Alternatives",
					"Select Criteria",
					"Input MCA Data",
					"Weight Criteria",
					"Run the Program"
				]}
			]},
			"Evaluating Your Results",
			"Next Steps",
			"Conclusion",
			"Contact Information",
		]
		
		self.process_toc(fisheries_toc)
		
	def process_toc(self, toc):
		self.ui.toc_tree.clear()
		for heading in toc:
			root_item = self.ui.toc_tree.invisibleRootItem()
			self.process_heading(heading, root_item)
	
	def process_heading(self, heading, parent):
		#print type(heading)
		if type(heading) == str:
			tree_item = QTreeWidgetItem(parent)
			tree_item.setText(0, heading)
		if type(heading) == dict:
			(heading_name, subheadings) = heading.popitem()
			tree_item = QTreeWidgetItem(parent)
			tree_item.setText(0, heading_name)
			for subheading in subheadings:
				self.process_heading(subheading, tree_item)                               

	def process_toc_click(self, item, column):
		"""Builds URL from toc heading name and reloads doc editor
		"""
		heading = item.text(column)
		#Morph heading name into anchor label name
		label = heading.replace(' ', '_')
		label = heading.replace('/', '_')
		label = heading.replace('.', '')
		label = label.toLower()
		
		#Build URL
		project_type = self.gui_manager.project_manager.get_current_project_type()
		language = self.gui_manager.config_manager.get_language()
		#Load URL and go to anchor within it
		self.ui.doc_browser.load_anchor(label, project_type, language)

	def process_help_click(self, name):
		"""Uses the help type given to load a section of the documentation
		"""
		label = name.replace('help_', '')
		#Build URL
		project_type = self.gui_manager.project_manager.get_current_project_type()
		language = self.gui_manager.config_manager.get_language()
		#Load URL and go to anchor within it
		self.ui.doc_browser.load_anchor(label, project_type, language)
		#Show the documentation if its hidden		
		if not self.ui.dock_doc.isVisible():
			self.ui.menu_dock_visible.trigger()
			

	def dock_full_screen(self):
		return self.dock_full_screen
 
 	def toggle_dock(self):
 		if self.dock_full_screen:
 			
  			self.ui.dock_doc.setMinimumSize(self.min_doc_dock_width, 0)
  			self.ui.dock_doc.resize(self.min_doc_dock_width, self.ui.dock_doc.height())

 			doc_dock_size = self.ui.dock_doc.sizeHint()

  			self.ui.toc_box.resize(100, self.ui.toc_box.height())
  			self.ui.toc_tree.resize(100, self.ui.toc_box.height())
   			self.ui.doc_box.resize(100, self.ui.doc_box.height())
  			self.ui.doc_browser.resize(100, self.ui.toc_box.height())
 			self.dock_full_screen = False
 		else:
	 		self.ui.dock_doc.setMinimumSize(self.width(), 0)
 			self.dock_full_screen = True

	def toggle_documentation_window(self):
		if self.ui.dock_doc.isVisible():
			self.ui.dock_doc.hide()
		else:			
			self.ui.dock_doc.show()

	def toggle_dock_visible_menu(self):
		if self.ui.dock_doc.isVisible():
			self.ui.menu_dock_visible.setChecked(True)
		else:			
			self.ui.menu_dock_visible.setChecked(False)
 
 	def toggle_dock_float(self):
		if self.ui.dock_doc.isFloating():
			self.ui.dock_doc.setFloating(False)
		else:			
			self.ui.dock_doc.setFloating(True)

	def toggle_dock_floating_menu(self, isFloating):
		print "got here"
		print isFloating
		if isFloating:
			self.ui.menu_dock_floating.setChecked(False)
		else:			
			self.ui.menu_dock_floating.setChecked(True)
