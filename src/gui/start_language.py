from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from start_language_ui import Ui_StartLanguage

class StartLanguageGui(QDialog, Ui_StartLanguage):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent