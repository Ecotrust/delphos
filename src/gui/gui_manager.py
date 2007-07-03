import os
import sys

#from project import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from delphos_window import DelphosWindow

class GuiManager:
	"""Provides access to, handles and maintins the Delphos GUI interface
	"""
	def __init__(self, project_manager):
		self.project_manager = project_manager
		self.qapp = QApplication(sys.argv)
		self.win = DelphosWindow()

	def start_gui(self):
		self.win.show()
		self.win.startup()
		sys.exit(self.qapp.exec_())
		
#Testing purposes
if __name__ == '__main__':
	os.chdir('..')	#Go to top-level directory