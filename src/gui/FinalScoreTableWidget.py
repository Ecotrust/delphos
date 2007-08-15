import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *

class FinalScoreTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.weight_column = 0
        #self.vertical_header_width = 300 #criteria descriptions are so freaking long!
        
    def load(self, altern_recs, results):
        """Loads the table with scores, given a list of records
        """
        self.clearContents()
        self.num_rows = len(altern_recs)    
        self.setRowCount(self.num_rows)
        
        for i in range(self.num_rows):
            header_item = QTableWidgetItem()
            #header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
            header_item.setText(altern_recs[i][1])
            header_item.setToolTip(altern_recs[i][1])
            self.setVerticalHeaderItem(i, header_item)
            
            score_item = QTableWidgetItem()
            score_item.setText(unicode(results[i]))
            self.setItem(i, 0, score_item)
            
        self.resizeColumnsToContents()