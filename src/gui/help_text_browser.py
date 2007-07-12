import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HelpTextBrowser(QTextBrowser):
	def __init__(self, parent=None):
		QTextBrowser.__init__(self, parent)
	
	def setSource(self, url):
		list = url.path().split('/')
		
		#If less than 3 elements it's not a URL we care about
		if len(list) < 3:
			return
		
		type = list[1]
		
		#Don't change the browsers source if its an 'app' link.
		if type == 'app':
			return
		else:
			#change the browser source as normal
			QTextBrowser.setSource(self, url)
        
if __name__ == "__main__":
	class HelpLoader(QMainWindow):
		def __init__(self, parent=None):
			QWidget.__init__(self, parent)
			self.help_browser = HelpTextBrowser(self)
			self.help_browser.setSource(QUrl('qrc:/blort/foo'))
			
	a = QApplication(sys.argv)
	app = HelpLoader()
	app.show()
	a.exec_()