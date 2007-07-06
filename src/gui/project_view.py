import os
import re
from os import path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from project_view_ui import Ui_ProjectView

class ProjectView(QDialog, Ui_ProjectView):
	"""Manages interaction with the project interface and the underlying DB
	
	Includes adding, removing, editing and displaying of project data and the sub interfaces needed
	to do that (eg. add new criteria subwindow).
	"""
	def __init__(self, gui_manager, project):
		QDialog.__init__(self, None)
		self.setupUi(self)
		self.gui_manager = gui_manager
		self.project = project