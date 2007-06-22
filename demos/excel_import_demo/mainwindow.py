from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_ui import Ui_MainWindow
#efrom projectwindow_ui import Ui_ProjectWindow
#from one_button_ui import Ui_One_Button_Form

import sys

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow
		self.setupUi(self)

		#self.workspace=QWorkspace()
		#proj_win = ProjectWindow(self.workspace)  #parent should be workspace I think
		#self.workspace.addWindow(proj_win)
		#self.setCentralWidget(self.workspace)

#class ProjectWindow(QMainWindow) :
#	def __init__(self, parent=None) :
#		QWidget.__init__(self, parent)
#		self.ui = Ui_ProjectWindow
#		self.ui.setupUi(self)

def main(argv):
	# create Qt application
	app = QApplication(argv)

	# create main window
	wnd = MainWindow()
	wnd.show()

	# run!
	retval = app.exec_()
  
	# exit
	sys.exit(retval)

if __name__ == "__main__":
	main(sys.argv)

