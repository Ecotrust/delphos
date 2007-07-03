import os
import sys

#from project import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_window import DelphosWindow
from start_dialog import StartDialog
from create_project_dialog import CreateProjectDialog

class GuiManager:
	"""Provides access to, handles and maintins the Delphos GUI interface
	"""
	def __init__(self, project_manager):
		#Store reference to proj manager for use by GUI
		self.project_manager = project_manager
		#Create new QT application object
		self.qapp = QApplication(sys.argv)
		#Create main delphos window
		self.win = DelphosWindow()

	def start_gui(self):
		"""Displays the main window and additional startup dialog
		"""
		#Show main window
		self.win.show()
		#Create startup dialog
		self.start_dialog = StartDialog(self, self.win)
		#Show startup dialog
		self.start_dialog.show()
		#Start main loop
		sys.exit(self.qapp.exec_())

	def create_new_project(self):
		#TODO: handle removal of startup dialog, at least simply dropping reference to it
		self.create_proj_dialog = CreateProjectDialog(self, self.win)
		self.create_proj_dialog.show()

	def open_existing_project(self):
		print "got here"
		
#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory