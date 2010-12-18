#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright    2007 Ecotrust
# @author        Tim Welch
# @contact        twelch at ecotrust dot org
# @license        GNU GPL 2 
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

import os
import sys
import urllib

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from sqlalchemy import *

from delphos_exceptions import *
from delphos_window import DelphosWindow
from select_type_dialog import SelectTypeDialog
from select_mpa_type_dialog import SelectMpaTypeDialog
from create_project_dialog import CreateProjectDialog
from open_project_dialog import OpenProjectDialog
from project_view_dialog import ProjectViewDialog
from language_dialog import LanguageDialog
from credits_dialog import CreditsDialog
from about_dialog import AboutDialog
from progress_dialog2 import ProgressDialog2

#PyQt modules
from PyQt4.QtCore import *

class GuiManager(QObject):
    """Provides access to, handles and maintins the Delphos GUI interface
    """
    def __init__(self, project_manager, config_manager):
        QObject.__init__(self)
        
        #Store reference to proj manager for use by GUI
        self.project_manager = project_manager
        self.config_manager = config_manager
        #Create new QT application object
        self.qapp = QApplication(sys.argv)
        
        #Setup translation
        self.appTranslator = QTranslator()        
        #locale_name = QLocale.system().name()  #Get system locale
        locale_name = 'es_MX'  #Start with spanish, this is hackish
        if self.appTranslator.load("i18n/"+locale_name+".qm"):
            self.qapp.installTranslator(self.appTranslator)
            print 'translator installed'        
        else:
            print 'translator not found'
                
        QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))

        #Create DesktopService for accessing services provided by desktop (eg. web browser) 
        self.desktop_services = QDesktopServices()
            
        #Create main delphos window
        self.win = DelphosWindow(self)
        
        qss = QFile(":/qss/main_style.css")
        qss.open(QIODevice.ReadOnly)
        stylesheet = str(qss.readAll())
        qss.close()
            
        #print "stylesheet"+str(self.qapp.styleSheet())
        #self.win.setStyleSheet(stylesheet)        
        
        #Hide the docked widget initially
        self.win.ui.dock_doc.hide()
        
        self.save_dialog = ProgressDialog2("Saving...")
        self.load_dialog = ProgressDialog2("Loading...")
        self.create_dialog = ProgressDialog2("Creating...")
        self.process_dialog = ProgressDialog2("Processing...")
        
        #Signal to capture qrc link clicks in text browsers or labels
        QObject.connect(self.win.ui.doc_browser, SIGNAL("anchorClicked(QUrl)"), self.anchor_click_handler)
        QObject.connect(self.win.ui.toc_tree, SIGNAL("anchorClicked(QUrl)"), self.anchor_click_handler)
        QObject.connect(self.win.ui.toc_tree, SIGNAL("itemClicked(QTreeWidgetItem*,int)"), self.win.process_toc_click)
        
        #Top menu slots
        QObject.connect(self.win.ui.menu_main_menu, SIGNAL("triggered()"), self.get_started)
        QObject.connect(self.win.ui.menu_exit_delphos, SIGNAL("triggered()"), self.stop_gui)
        QObject.connect(self.win.ui.menu_open_project, SIGNAL("triggered()"), self.handle_open_existing_selection)
        QObject.connect(self.win.ui.menu_create_project, SIGNAL("triggered()"), self.handle_design_new_selection)
        QObject.connect(self.win.ui.menu_credits, SIGNAL("triggered()"), self.show_credits)
        QObject.connect(self.win.ui.menu_about, SIGNAL("triggered()"), self.show_about)
        
        QObject.connect(self.project_manager, SIGNAL("project_changed"), self.reload_doc)
        
        #Flag indicating whether dock_doc widget is currently full screen
        self.dock_doc_is_full_screen = False

    def start_gui(self):
        """Displays the main window and additional startup dialog
        """
        #Show main window
        self.win.show()        
        #Display dialog for user to select project type
        self.start_language_selection()
        #Start main loop
        sys.exit(self.qapp.exec_())

    def stop_gui(self):
        self.qapp.closeAllWindows()

    def get_started(self):
        """Loads dialog allowing user to select overall project type (eg. Fisheries, MPAs)
        """
        #Create startup dialog
        self.select_type_dialog = SelectTypeDialog(self, self.win)
        #Connect handler for type selection
        self.connect(self.select_type_dialog, SIGNAL("get_started"), self.handle_get_started)
        #Show startup dialog
        self.select_type_dialog.show()

    def handle_get_started(self, action):
        """Save analysis type or continue type selection
        """              
        self.select_type_dialog.hide()
        self.select_type_dialog.deleteLater()

        if action == 'open_project':
            self.handle_open_existing_selection()
        elif action == 'create_project':
            self.handle_design_new_selection()
        elif action == 'fisheries_doc':
            self.project_manager.set_current_project_type("fisheries")
            self.get_started()
            self.win.load_full_doc()
        elif action == 'mpa_doc':
            self.start_mpa_type_selection()       

    def start_mpa_type_selection(self):
        """Loads dialog allowing user to select mpa project type (eg. Community, site)
        """
        #Create startup dialog
        self.select_mpa_type_dialog = SelectMpaTypeDialog(self, self.win)
        #Connect handler for type selection
        self.connect(self.select_mpa_type_dialog, SIGNAL("mpa_type_selected"), self.handle_mpa_type_selection)
        #Show startup dialog
        self.select_mpa_type_dialog.show()

    def handle_mpa_type_selection(self, mpa_type):
        """Stores the analaysis type selected and loads the documentation window
        """
        self.project_manager.set_current_project_type(mpa_type)          
        self.select_mpa_type_dialog.hide()
        self.select_mpa_type_dialog.deleteLater()
        self.get_started()
        self.win.load_full_doc()

    def start_language_selection(self):
        """Used for selecting language to load for documentation"""
        self.language_dialog = LanguageDialog(self, self.win)
        self.connect(self.language_dialog, SIGNAL("language_selected"), self.finish_language_selection)
        self.language_dialog.show()
    
    def finish_language_selection(self, language):
        self.config_manager.set_language(language)
        cur_proj_type = self.project_manager.get_current_project_type()
        
        self.language_dialog.hide()
        self.language_dialog.deleteLater()
        #Load doc browser
        #self.win.ui.doc_browser.load_doc(cur_proj_type, language)
        self.get_started()

    def reload_doc(self):
        language = self.config_manager.get_language()
        cur_proj_type = self.project_manager.get_current_project_type()
        #Load doc browser
        self.win.ui.doc_browser.load_doc(cur_proj_type, language)
        #Load the table of contents
        self.win.load_toc(cur_proj_type, language)
    
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
            self.create_dialog.show()
            self.project_manager.create_project(project_filename, project_path, project_type, load_default_altern, load_default_crit, self.config_manager.get_language())
        except (DelphosError, exceptions.DBAPIError), e:
            self.create_dialog.hide()
            QMessageBox.critical(self.create_proj_dialog, "Project Creation Error", "Error creating/opening project file. Try again.  Do you have the correct permissions to create a project in that location?\n\n"+str(e))
        else:
            self.create_proj_dialog.close()
            self.create_proj_dialog.deleteLater()
            self.start_project_display()
            self.create_dialog.hide()
            
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
            self.load_dialog.show()
            self.project_manager.open_project(project_filename, project_path)
        except DelphosError, e:
            self.load_dialog.hide()
            QMessageBox.critical(self.open_proj_dialog,"Project Open Error", "Project opening failed: "+str(e))
        else:
            self.open_proj_dialog.close()
            self.start_project_display()
            self.load_dialog.hide()    
    
    def start_project_display(self):
        """Create widget displaying project
        """
        self.project_view = ProjectViewDialog(self, self.project_manager.get_current_project())
        self.win.setCentralWidget(self.project_view)
        self.project_view.show()
        #Load the table of contents
        self.win.load_toc()
        self.win.ui.dock_doc.show()
    
    def show_credits(self):
        """Show credits dialog
        """
        credits_dialog = CreditsDialog(self, self.win)
        credits_dialog.show()

    def show_about(self):
        """Show about dialog
        """
        about_dialog = AboutDialog(self.win)
        about_dialog.show()

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
        
        #print url.path()
        list = url.path().split('/')
        
        #If less than 3 elements it's not a URL we care about
        #for item in list:
        #    print item
        #print len(list)
        if len(list) < 3:
            return
        #Extract 'keywords' from path
        type = list[1]
        action = list[2]

        if type == 'app':
            if action == 'create_project':
                self.start_project_creation()
        
        elif type == 'doc':
            #Find which documentation subdir to look in
            project_type = self.project_manager.get_current_project_type()
            language = self.config_manager.get_language()
            doc_subdir = ""
            #print "my language"
            #print language
            if project_type == 'fisheries':
                if language == 'english':
                    doc_subdir = 'fisheries'+os.sep+'english'+os.sep
                else:
                    doc_subdir = 'fisheries'+os.sep+'spanish'+os.sep
            elif project_type == "communities":
                if language == 'english':
                    doc_subdir = 'mpa'+os.sep+'communities'+os.sep+'english'+os.sep
                else:
                    doc_subdir = 'mpa'+os.sep+'communities'+os.sep+'spanish'+os.sep
            elif project_type == "sites":
                if language == 'english':
                    doc_subdir = 'mpa'+os.sep+'sites'+os.sep+'english'+os.sep
                else:
                    doc_subdir = 'mpa'+os.sep+'sites'+os.sep+'spanish'+os.sep                                            
            
            doc_path = os.getcwd()+os.sep+"documentation"+os.sep+doc_subdir+os.sep+action
            doc_url = "file:"+urllib.pathname2url(unicode(doc_path))
            #print "doc url"
            print doc_url
            self.desktop_services.openUrl(QUrl(doc_url))
    
#Testing purposes
if __name__ == '__main__':
    os.chdir('..')    #Go to top-level directory