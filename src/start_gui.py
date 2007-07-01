#Built-in modules
import sys

#Third-party modules
import sip
import pyExcelerator
import sqlalchemy
from pyExcelerator import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Delphos modules
from gui import *
#from start_wizard_ui import Ui_StartWizard
from gui.main_window_ui import Ui_MainWindow
from gui.start_language import StartLanguageGui

class Delphos(QMainWindow):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)	#Initialize as a widget
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)			#Create the components of the window
 
 	def startup(self):
 		lang_dialog = StartLanguageGui(self)
		lang_dialog.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	delphos = Delphos()
	delphos.show()
	delphos.startup()
	sys.exit(app.exec_())