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

class AlternativeMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        #Index into alternative DB table
        self.altern_id_column = 0
        self.altern_name_column = 1
        self.altern_color_column = 2
        
        #Index into alternative table widget
        self.altern_check_display_column = 0
        self.altern_name_display_column = 1
        self.altern_color_display_column = 2

    def load(self, alternative_recs):
        """Loads the table with alternatives, given a list of records
        """
        self.clearContents()
        self.num_rows = len(alternative_recs)
        self.setRowCount(self.num_rows)
        
        for i in range(self.num_rows):
            #Add checkbox widget to first column
            check_box = QCheckBox(self)
            self.setCellWidget(i, self.altern_check_display_column, check_box)      
            
            #Add alternative name to second column
            item = QTableWidgetItem()
            item.setText(unicode(alternative_recs[i][self.altern_name_column]))
            self.setItem(i, self.altern_name_display_column, item)
            
            #Add alternative color to third column
            altern_color = alternative_recs[i][self.altern_color_column]
            color_item = QTableWidgetItem()
            color_item.setBackgroundColor(QColor(altern_color))
            self.setItem(i, self.altern_color_display_column, color_item)
            
        self.resizeColumnsToContents()
    
    def check_all(self):
        for i in range(self.num_rows):
            check_box = self.cellWidget(i, self.altern_check_display_column)
            check_box.setCheckState(Qt.Checked)
        
    def uncheck_all(self):
        for i in range(self.num_rows):
            check_box = self.cellWidget(i, self.altern_check_display_column)
            check_box.setCheckState(Qt.Unchecked)
        
    def get_selected_indexes(self):
        """Returns list of indexes of alternatives selected in table
        
        Can be used for lookup in list structure containing alternatives data
        """
        selected_indexes = []
        for row in range(self.num_rows):
            check_widget = self.cellWidget(row, self.altern_check_display_column)
            check_state = check_widget.checkState()
            if check_state == Qt.Checked:
                selected_indexes.append(row)
        return selected_indexes
    
    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            return selected_row[0]
        else:
            raise DelphosError, "You must first select an alternative"
        