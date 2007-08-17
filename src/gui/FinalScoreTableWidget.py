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
        
    def load(self, altern_recs, sorted_results):
        """Loads the table with scores, given a list of altern records and a list of sorted results mapped to altern ids
        """
        self.clearContents()
        self.num_rows = len(altern_recs)    
        self.setRowCount(self.num_rows)
        
        print altern_recs
        print sorted_results
        
        #Make altern recs a dict using altern_id as key
        altern_recs = dict(altern_recs)
        
        for i in range(len(sorted_results)):
            (altern_id, score) = sorted_results[i]
            score = round(score, 4)
            altern_name = altern_recs[altern_id]
            
            header_item = QTableWidgetItem()
            #header_item.setSizeHint(QSize(self.vertical_header_width, header_item.sizeHint().height()))
            header_item.setText(altern_name)
            header_item.setToolTip(altern_name)
            self.setVerticalHeaderItem(i, header_item)
            
            score_item = QTableWidgetItem()
            score_item.setText(unicode(score))
            self.setItem(i, 0, score_item)
            
            rank_item = QTableWidgetItem()
            rank_item.setText(unicode(i+1))
            self.setItem(i, 1, rank_item)
            
        self.resizeColumnsToContents()