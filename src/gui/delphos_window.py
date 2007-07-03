from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from main_window_ui import Ui_MainWindow

class DelphosWindow(QMainWindow):
	"""Manages the main Delphos window interface (Ui_MainWindow)
	"""
	
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)	#Initialize myself as a widget
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)			#Create the components of the window
 
 	def startup(self):
	 	"""Loads the initial start dialog window
 		"""
