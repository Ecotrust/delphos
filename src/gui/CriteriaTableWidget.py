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

class CriteriaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)

    def load(self, criteria_recs):
        """Loads the table in the criteria tab with the existing project criteria
        """
        if criteria_recs:
            self.clearContents()
            self.setRowCount(len(criteria_recs))
        
            for i in range(len(criteria_recs)):
                name_item = QTableWidgetItem()
                name_item.setText(str(criteria_recs[i][1]))
                self.setItem(i, 0, name_item)
    
                type_item = QTableWidgetItem()
                type_item.setText(str(criteria_recs[i][2]))
                self.setItem(i, 1, type_item)
    
                type_item = QTableWidgetItem()
                type_item.setText(str(criteria_recs[i][3]))
                self.setItem(i, 2, type_item)
    
                cb_item = QTableWidgetItem()
                cb_item.setText(str(criteria_recs[i][4]))
                self.setItem(i, 3, cb_item)

                self.resizeColumnsToContents()

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            #Return the unique criteria description
            return selected_row[0]
        else:
            raise DelphosError, "You must first select a criterion"
        