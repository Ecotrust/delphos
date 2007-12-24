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

class AlternativeTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTextBrowser.__init__(self, parent)
        self.altern_name_column = 1;        #Column containing alternative names
        self.altern_color_column = 2;        #Color to visually associate with altern
        
    def load(self, alternative_recs):
        """Loads the table with alternatives, given an array of records
        """
        self.clearContents()
        self.setRowCount(len(alternative_recs))
        
        for i in range(len(alternative_recs)):
            item = QTableWidgetItem()
            item.setText(unicode(alternative_recs[i][self.altern_name_column]))
            self.setItem(i, 0, item)
            
            altern_color = alternative_recs[i][self.altern_color_column]
            color_item = QTableWidgetItem()
            color_item.setBackgroundColor(QColor(altern_color))
            self.setItem(i, 1, color_item)
                                    
        self.resizeColumnsToContents()

    def get_selected_ids(self):
        return []

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            return selected_row[0]
        else:
            raise DelphosError, "You must first select an alternative"
        