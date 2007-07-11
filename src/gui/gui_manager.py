import os
import sys
import webbrowser

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from delphos_window import DelphosWindow
from select_type_dialog import SelectTypeDialog
from main_menu_dialog import MainMenuDialog
from create_project_dialog import CreateProjectDialog
from open_project_dialog import OpenProjectDialog
from project_view import ProjectView

class GuiManager(QObject):
	"""Provides access to, handles and maintins the Delphos GUI interface
	"""
	def __init__(self, project_manager):
		QObject.__init__(self)
		#Store reference to proj manager for use by GUI
		self.project_manager = project_manager
		#Create new QT application object
		self.qapp = QApplication(sys.argv)
		#Create main delphos window
		self.win = DelphosWindow()
		#Hide the docked widget initially
		self.win.ui.dock_doc.hide()

	def start_gui(self):
		"""Displays the main window and additional startup dialog
		"""
		#Show main window
		self.win.show()
		#Create startup dialog
		self.select_type_dialog = SelectTypeDialog(self, self.win)
		#Connect handler for type selection
		self.connect(self.select_type_dialog, SIGNAL("type_selected"), self.handle_type_selection)
		#Show startup dialog
		self.select_type_dialog.show()
		#Start main loop
		sys.exit(self.qapp.exec_())

	def handle_type_selection(self, type):
		self.project_manager.set_analysis_type(type)
		self.select_type_dialog.hide()
		del self.select_type_dialog
		
		self.main_menu_dialog = MainMenuDialog(self, self.win)
		#Connect handlers to process main menu selections
		self.connect(self.main_menu_dialog, SIGNAL("intro_selected"), self.handle_intro_selection)
		self.connect(self.main_menu_dialog, SIGNAL("design_new_selected"), self.handle_design_new_selection)
		self.connect(self.main_menu_dialog, SIGNAL("open_existing_selected"), self.handle_open_existing_selection)
		self.connect(self.main_menu_dialog, SIGNAL("full_doc_selected"), self.handle_full_doc_selection)		
		self.main_menu_dialog.show()
	
	def handle_intro_selection(self):
		self.win.ui.dock_doc.show()
		self.main_menu_dialog.hide()

	def handle_design_new_selection(self):
		self.main_menu_dialog.hide()
		del self.main_menu_dialog
		self.start_project_creation()
	
	def handle_open_existing_selection(self):
		self.main_menu_dialog.hide()
		del self.main_menu_dialog
		self.start_project_opening()
	
	def handle_full_doc_selection(self):
		os.chdir('..'+os.sep+'docs')
		file_path = "file://"+os.getcwd()+os.sep+"delphos_full_text_06_07.doc"
		print file_path
		webbrowser.open(file_path)
		os.chdir('..'+os.sep+'src')
	
	def start_project_creation(self):
		"""Create widget for new project creation, gets the process started
		"""
		#TODO: handle removal of startup dialog, at least simply dropping reference to it
		self.create_proj_dialog = CreateProjectDialog(self, self.win)
		self.connect(self.create_proj_dialog, SIGNAL("create_project_info_collected"), self.finish_project_creation)
		self.create_proj_dialog.show()

	def finish_project_creation(self, *args):
		"""Calls for project creation after info has been gathered from user

		project_type (string)
		project_path (string)
		project_filename (string)
		load_default_altern (boolean) - whether to load default alternatives into new project DB
		load_default_crit (boolean) whether to load default criteries into new project DB
		"""
		project_filename, project_path, project_type, load_default_altern, load_default_crit = args
		self.create_proj_dialog.close()
		try:
			self.project_manager.create_project(project_filename, project_path, project_type, load_default_altern, load_default_crit)
		except DelphosError, e:
			QMessageBox.critical(self,"Project Creation Error", e)
		self.start_project_display()
			
	def start_project_opening(self):
		"""Create dialog for opening an existing project
		"""
		self.open_proj_dialog = OpenProjectDialog(self, self.win)
		self.connect(self.open_proj_dialog, SIGNAL("open_project_info_collected"), self.finish_project_opening)
		self.open_proj_dialog.show()
	
	def finish_project_opening(self, *args):
		"""Calls for opening of project given the necessary project information
		"""
		project_filename, project_path = args
		try:
			self.project_manager.open_project(project_filename, project_path)
		except DelphosError, e:
			QMessageBox.critical(self.open_proj_dialog,"Project Open Error", "Project opening failed: "+str(e))
		else:
			self.open_proj_dialog.close()
			self.start_project_display()		
	
	def start_project_display(self):
		"""Create widget displaying project
		"""
		self.project_view = ProjectView(self, self.project_manager.get_current_project())
		self.win.setCentralWidget(self.project_view)
		self.project_view.show()
		
#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory