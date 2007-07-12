import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from main_menu_ui import Ui_MainMenuDialog

class MainMenuDialog(QDialog, Ui_MainMenuDialog):
	"""Dialog providing main menu of options
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		
		#Connect slots to signals
		QObject.connect(self.but_introduction, QtCore.SIGNAL("clicked()"), self.intro_selection)
		QObject.connect(self.but_design_project, QtCore.SIGNAL("clicked()"), self.design_new_selection)
		QObject.connect(self.but_open_project, QtCore.SIGNAL("clicked()"), self.open_existing_selection)
		QObject.connect(self.but_full_doc, QtCore.SIGNAL("clicked()"), self.full_doc_selection)
		
	def intro_selection(self):
		self.emit(SIGNAL("intro_selected"))
		
	def design_new_selection(self):
		self.emit(SIGNAL("design_new_selected"))
	
	def open_existing_selection(self):
		self.emit(SIGNAL("open_existing_selected"))
		
	def full_doc_selection(self):
		self.emit(SIGNAL("full_doc_selected"))