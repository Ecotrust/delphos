import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlternativeTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)
        
    def load(self, alternative_recs):
        """Loads the table with alternatives, given an array of records
        """
        self.clear()
        self.setColumnCount(1)
        self.setRowCount(len(alternative_recs))
        
        for i in range(len(alternative_recs)):
            item = QTableWidgetItem()
            item.setText(str(alternative_recs[i][1]))
            self.setItem(i, 0, item)
        self.resizeColumnsToContents()