import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mpa_main_menu_ui import Ui_MpaMainMenuDialog

class MpaMainMenuDialog(QDialog, Ui_MpaMainMenuDialog):
	"""Dialog providing main menu of options
	"""
	def __init__(self, gui_manager, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.gui_manager = gui_manager
		
		#Connect slots to signals
		QObject.connect(self.mpa_intro_button, QtCore.SIGNAL("clicked()"), self.intro_selection)
		QObject.connect(self.mpa_new_project_button, QtCore.SIGNAL("clicked()"), self.design_new_selection)
		QObject.connect(self.mpa_open_project_button, QtCore.SIGNAL("clicked()"), self.open_existing_selection)
		QObject.connect(self.mpa_full_doc_button, QtCore.SIGNAL("clicked()"), self.full_doc_selection)
		
	def intro_selection(self):
		self.emit(SIGNAL("mpa_intro_selected"))
		
	def design_new_selection(self):
		self.emit(SIGNAL("mpa_design_new_selected"))
	
	def open_existing_selection(self):
		self.emit(SIGNAL("mpa_open_existing_selected"))
		
	def full_doc_selection(self):
		self.emit(SIGNAL("mpa_full_doc_selected"))