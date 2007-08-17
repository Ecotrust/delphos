from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from main_window_ui import Ui_MainWindow

import os

class DelphosWindow(QMainWindow):
	"""Manages the main Delphos window interface (Ui_MainWindow)
	"""
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)	#Initialize myself as a widget
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)			#Create the components of the window
		self.dock_full_screen = False
		self.min_doc_dock_width = 200
		
		#Maximize the display to full size
		self.showMaximized()

		self.base_fishery_url = 'qrc:/documentation/fisheries_documentation.html#'
		self.base_mpa_url = 'qrc:/documentation/mpa_documentation.html#'
		
		#TODO: make this work
		QObject.connect(self.ui.prev_button, SIGNAL("backwardAvailable(bool)"), self.toggle_prev_button)
		QObject.connect(self.ui.next_button, SIGNAL("forwardAvailable(bool)"), self.toggle_next_button)

		#self.ui.dock_doc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.load_toc()

	def toggle_prev_button(self, available):
		#TODO: make this work
		print "toggle prev!"
		if available:
			self.prev_button.isEnabled = available

	def toggle_next_button(self, available):
		#TODO: make this work
		print "toggle next!"
		if available:
			self.next_button.isEnabled = available
		
	def load_toc(self):
		"""Loads the table of contents within the dock widget
		"""
		fisheries_toc = [
			"Introduction",
			"Background", 
			{"Multicriteria Analysis/Evamix": [
				"References", 
				"Algorithm"
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
					"Define Alternatives",
					"Define Criteria"
				]},
				{"8. Run Analysis":[
					"Select Alternatives",
					"Select Criteria",
					"Input Data",
					"Weight Criteria",
					"Run the Program"
				]}
			]},
			"Evaluating Your Results",
			"Next Steps",
			{"Conclusion": [
				"Contact Information"
			]}
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
		url = self.base_fishery_url+label
		#Reload doc editor with new url
		self.ui.doc_browser.setSource(QUrl(url))

	def dock_full_screen(self):
		return self.dock_full_screen
 
 	def toggle_dock(self):
 		if self.dock_full_screen:
 			
  			self.ui.dock_doc.setMinimumSize(self.min_doc_dock_width, 0)
  			self.ui.dock_doc.resize(self.min_doc_dock_width, self.ui.dock_doc.height())

 			doc_dock_size = self.ui.dock_doc.sizeHint()
			print doc_dock_size.width()
			print doc_dock_size.height()

  			self.ui.toc_box.resize(100, self.ui.toc_box.height())
  			self.ui.toc_tree.resize(100, self.ui.toc_box.height())
   			self.ui.doc_box.resize(100, self.ui.doc_box.height())
  			self.ui.doc_browser.resize(100, self.ui.toc_box.height())
 			self.dock_full_screen = False
 		else:
	 		self.ui.dock_doc.setMinimumSize(self.width(), 0)
 			self.dock_full_screen = True