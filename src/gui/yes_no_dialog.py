from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from yes_no_ui import Ui_YesNoDialog

class YesNoDialog(QDialog, Ui_YesNoDialog):
	"""Manages the add alternative dialog
	"""
	def __init__(self, parent, message):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.parent = parent
		self.errorMsg = ""
		
		#Connect slots to signals
		QObject.connect(self.confirm_box,QtCore.SIGNAL("accepted()"), self.process_accept)
		QObject.connect(self.confirm_box,QtCore.SIGNAL("rejected()"), self.process_reject)

		self.message_label.setText(message)

	def process_accept(self):
		"""Processes clicking of Yes button in dialog
		"""
		self.emit(SIGNAL("delete_confirm"), True)
			
	def process_reject(self):
		"""Processes clicking of No button in dialog
		"""
		self.emit(SIGNAL("delete_confirm"), False)