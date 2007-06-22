import sys

import pyExcelerator
from pyExcelerator import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_ui import Ui_MainWindow
import sip

class StartApp(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)	#required
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)			#required
		QObject.connect(self.ui.buttonOpen,QtCore.SIGNAL("clicked()"), self.file_dialog)

	def file_dialog(self):
		fd = QFileDialog(self)
		self.filename = fd.getOpenFileName()
		from os.path import isfile
		if isfile(self.filename):
			self.loadTableFromExcel(self.filename)
			#text = open(self.filename).read()
			#self.ui.textWindow.setText(text)

	def loadTableFromExcel(self, filename):
		for sheet_name, values in parse_xls(filename, 'cp1251'):
			print 'Sheet = "%s"' % sheet_name.encode('cp866', 'backslashreplace')
			for row_idx, col_idx in sorted(values.keys()):
				v = values[(row_idx, col_idx)]
				#item = QTableWidgetItem(v)
				item = QTableWidgetItem()
				
				#if type(v) == type(1)
				#	item.setData(Qt.DisplayRole, v)
				if isinstance(v, unicode):
					v = v.encode('cp866', 'backslashreplace')
					
				if type(v)==type('a'):
					item.setText(v)
				else:
					s = QVariant(v)
					print type(Qt.DisplayRole)
					item.setData(Qt.DisplayRole, s)
					
				self.ui.FisheryDataTable.setItem(row_idx, col_idx, item)
				print '(%d, %d) =' % (row_idx, col_idx), v

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = StartApp()
    myapp.show()
    sys.exit(app.exec_())

