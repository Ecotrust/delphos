import os
import sys
import urllib

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_exceptions import *
from delphos_window import DelphosWindow
from select_type_dialog import SelectTypeDialog
from create_project_dialog import CreateProjectDialog
from open_project_dialog import OpenProjectDialog
from project_view_dialog import ProjectViewDialog

class GuiManager(QObject):
	"""Provides access to, handles and maintins the Delphos GUI interface
	"""
	def __init__(self, project_manager):
		QObject.__init__(self)
		
		#Store reference to proj manager for use by GUI
		self.project_manager = project_manager
		#Create new QT application object
		self.qapp = QApplication(sys.argv)

		qss = QFile(":/qss/main_style.css")
		qss.open(QIODevice.ReadOnly)
		stylesheet = str(qss.readAll())
		qss.close()
		
		#print "stylesheet: "
		#print stylesheet
		
		self.qapp.setStyleSheet(stylesheet)

		#Create DesktopService for accessing services provided by desktop (eg. web browser) 
		self.desktop_services = QDesktopServices()

		#Assign URL handler for help: links which can be placed in widgets and load appropriate help documentation
		#self.desktop_services.setUrlHandler("help", self, SLOT("showHelp(QUrl)"))
		#Assign URL handler for app: links, which can be placed in documentation and load appropriate widgets
		#self.desktop_services.setUrlHandler("help", self, SLOT("showApp(QUrl)"))
		#Test URL handler
		#self.desktop_services.openUrl(QUrl('help:/me/now'))
			
		#Create main delphos window
		self.win = DelphosWindow()
		#Hide the docked widget initially
		self.win.ui.dock_doc.hide()
		#Resize to full screen
		self.win.resize(self.get_screen_width(), self.get_screen_height())

		#Load doc browser with correct documentation
		self.win.ui.doc_browser.setSource(QUrl('qrc:/documentation/fisheries_documentation.html'))
		print self.win.ui.doc_browser.fontInfo()
		#Signal to capture qrc link clicks in text browsers or labels
		QObject.connect(self.win.ui.doc_browser, SIGNAL("anchorClicked(QUrl)"), self.anchor_click_handler)
		QObject.connect(self.win.ui.toc_tree, SIGNAL("anchorClicked(QUrl)"), self.anchor_click_handler)
		QObject.connect(self.win.ui.toc_tree, SIGNAL("itemClicked(QTreeWidgetItem*,int)"), self.win.process_toc_click)
		
		#Top menu slots
		QObject.connect(self.win.ui.menu_exit_delphos, SIGNAL("triggered()"), self.stop_gui)
		QObject.connect(self.win.ui.menu_open_project, SIGNAL("triggered()"), self.handle_open_existing_selection)
		QObject.connect(self.win.ui.menu_create_project, SIGNAL("triggered()"), self.handle_design_new_selection)

		#Flag indicating whether dock_doc widget is currently full screen
		self.dock_doc_is_full_screen = False
        
	def start_gui(self):
		"""Displays the main window and additional startup dialog
		"""
		#Show main window
		self.win.show()		
		#Display dialog for user to select project type
		self.start_type_selection()
		#Start main loop
		sys.exit(self.qapp.exec_())

	def stop_gui(self):
		self.qapp.closeAllWindows()

	def start_type_selection(self):
		"""Loads dialog allowing user to select overall project type (eg. Fisheries, MPAs)
		"""
		#Create startup dialog
		self.select_type_dialog = SelectTypeDialog(self, self.win)
		#Connect handler for type selection
		self.connect(self.select_type_dialog, SIGNAL("type_selected"), self.handle_type_selection)
		#Show startup dialog
		self.select_type_dialog.show()

	def handle_type_selection(self, type):
		"""Stores the analaysis type selected and loads the documentation window
		"""
		self.project_manager.set_current_project_type(type)
		self.select_type_dialog.hide()
		self.select_type_dialog.deleteLater()
		self.win.ui.dock_doc.show()
	
	def handle_intro_selection(self):
		"""Loads up the documentation in the dock window, displays the intro page
		"""
		self.show_documentation_window()		

	def handle_design_new_selection(self):
		"""Start the process of designing a new project
		"""
		self.start_project_creation()
	
	def handle_open_existing_selection(self):
		"""Start the process of opening an existing project
		"""
		self.start_project_opening()
	
	def handle_full_doc_selection(self):
		doc_path = os.getcwd()+os.sep+"documentation"+os.sep+"delphos_full_text_06_07.doc"
		#print doc_path
		doc_url = "file:"+urllib.pathname2url(doc_path)
		#print doc_url
		self.desktop_services.openUrl(QUrl(doc_url))
	
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
		try:
			self.project_manager.create_project(project_filename, project_path, load_default_altern, load_default_crit)
		except DelphosError, e:
			QMessageBox.critical(self.create_proj_dialog, "Project Creation Error", str(e))
		else:
			self.create_proj_dialog.close()
			self.create_proj_dialog.deleteLater()
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
		self.project_view = ProjectViewDialog(self, self.project_manager.get_current_project())
		self.win.setCentralWidget(self.project_view)
		self.project_view.show()

	def get_screen_dimensions(self):
		"""Return (width, height) tuple in pixels of the screen containing the delphos window
		"""
		desktop = self.qapp.desktop()
		desktop_size = desktop.screenGeometry(self.win)
		return (desktop_size.width(), desktop_size.height())
	
	def get_screen_height(self):
		"""Return height in pixels of the screen containing the delphos window
		"""
		desktop = self.qapp.desktop()
		desktop_size = desktop.screenGeometry(self.win)
		return desktop_size.height()

	def get_screen_width(self):
		"""Return width in pixels of the screen containing the delphos window
		"""
		desktop = self.qapp.desktop()
		desktop_size = desktop.screenGeometry(self.win)
		return desktop_size.width()
	
	def get_window_height(self):
		"""Returns the height in pixels of the main window
		"""
		return self.win.height()

	def get_window_width(self):
		"""Returns the width in pixels of the main window
		"""
		return self.win.width()
	
	def anchor_click_handler(self, url):
		"""Called when any anchor link is clicked.  This method used to process special application
		requests
		
		Special application requests are simply link URL's in the form qrc:/app/action.  An example 
		is a link that when clicked should load the 'new project' dialog.  This link
		might look like 'qrc:/app/create_new_project'
		"""
		
		list = url.path().split('/')
		
		#If less than 3 elements it's not a URL we care about
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
			print doc_url
			self.desktop_services.openUrl(QUrl(doc_url))
	
#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory