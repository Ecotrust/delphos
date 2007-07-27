import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlternativeTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)
        QObject.connect(self,QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.__item_click_handler)
        self.selected_item = None     #The currently selected item in the table
        self.num_columns = 1                #total number of columns in table
        self.altern_name_column = 1;        #Columns containing alternative names
        
    def load(self, alternative_recs):
        """Loads the table with alternatives, given an array of records
        """
        self.clear()
        self.setColumnCount(self.num_columns)
        self.setRowCount(len(alternative_recs))
        
        for i in range(len(alternative_recs)):
            item = QTableWidgetItem()
            item.setText(str(alternative_recs[i][self.altern_name_column]))
            self.setItem(i, 0, item)
        self.resizeColumnsToContents()
    
    def __item_click_handler(self, cur_item):
        self.selected_item = cur_item
    
    def get_current_item(self):
        return self.selected_item
        