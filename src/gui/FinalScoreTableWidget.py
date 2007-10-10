import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from util.common_functions import *

class FinalScoreTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.weight_column = 0
        self.altern_color_display_column = 2
        #self.vertical_header_width = 300 #criteria descriptions are so freaking long!
        
    def load(self, final_results):
        """Loads the table with scores, given a list of altern records and a list of sorted results mapped to altern ids
        """
        self.clearContents()
        self.num_rows = len(final_results)    
        self.setRowCount(self.num_rows)
        
        for i in range(len(final_results)):
            header_item = QTableWidgetItem()
            #header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
            header_item.setText(final_results[i][1])
            header_item.setToolTip(final_results[i][1])
            self.setVerticalHeaderItem(i, header_item)
            
            score_item = QTableWidgetItem()
            score_item.setText(unicode(final_results[i][3]))
            self.setItem(i, 0, score_item)
            
            rank_item = QTableWidgetItem()
            rank_item.setText(unicode(final_results[i][2]))
            self.setItem(i, 1, rank_item)
            
            #Add alternative color to third column
            color_item = QTableWidgetItem()
            color_item.setBackgroundColor(QColor(final_results[i][4]))
            self.setItem(i, self.altern_color_display_column, color_item)            
            
        self.resizeColumnsToContents()