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
from gui.start_language_ui import Ui_StartLanguage

class DelphosWindow(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)	#required
		self.ui = Ui_StartLanguage()
		self.ui.setupUi(self)			#required

if __name__ == "__main__":
	app = QApplication(sys.argv)
	delphos = DelphosWindow()
	delphos.show()
	sys.exit(app.exec_())