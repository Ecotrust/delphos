import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DelphosCheckBox(QCheckBox):
    """A checkbox that holds an additional value.
     
    Value might be used later in processing, for example a unique database table id.
    """
    def __init__(self, parent):
        QCheckBox.__init__(self, parent)
        self.value = None
        
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value
        