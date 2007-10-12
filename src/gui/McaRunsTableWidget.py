#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
# @license		GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id$
#
# @summary - 
#===============================================================================

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from delphos_exceptions import *

class McaRunsTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.id_column = 0
        self.name_column = 1
        self.description_column = 2
        self.date_column = 3
        
        self.name_display_column = 0
        self.description_display_column = 1
        self.date_display_column = 2

    def load(self, mca_recs):
        """Loads the table with info on past analysis runs
        """
        if mca_recs is not None:
            self.mca_recs = mca_recs
            self.clearContents()
            self.num_rows = len(mca_recs)
            self.setRowCount(self.num_rows)
        
            for i in range(self.num_rows):
                name_item = QTableWidgetItem()
                name_item.setText(mca_recs[i][self.name_column])
                self.setItem(i, self.name_display_column, name_item)
                desc_item = QTableWidgetItem()
                desc_item.setText(mca_recs[i][self.description_column])
                self.setItem(i, self.description_display_column, desc_item)
                date_item = QTableWidgetItem()
                date_item.setText(unicode(mca_recs[i][self.date_column]))
                self.setItem(i, self.date_display_column, date_item)
            self.resizeColumnsToContents()

    def get_selected_id(self):
        index = self.get_current_index()
        if index is not None:
            return self.mca_recs[index][self.id_column]
        else:
            return None

    def get_current_index(self):
        cur_row_item = self.get_current_row_items()
        if cur_row_item is not None:
            return cur_row_item.row()
        else:
            return None

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            #Return the unique criteria description
            return selected_row[0]
        else:
            return None
        