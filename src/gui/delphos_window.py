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
		pass
		introduction = 'qrc:/documentation/fisheries_documentation.html#fisheries_introduction'
		background = 'qrc:/documentation/fisheries_documentation.html#fisheries_background'
		
		references = {'References':'qrc:/documentation/fisheries_documentation.html#fisheries_references'}
		algorithm = {'Algorithm':'qrc:/documentation/fisheries_background.html#fisheries_algorithm'}
		evamix = [references, algorithm]
		toc = {'Introduction':introduction, 'Background':background,  'Evamix':evamix}
		
	def dock_full_screen(self):
		return self.dock_full_screen
 
 	def toggle_dock(self):
 		print "toggleing"
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
 
 	def startup(self):
	 	"""Loads the initial start dialog window
 		"""