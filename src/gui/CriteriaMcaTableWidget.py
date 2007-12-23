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

class CriteriaMcaTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.id_column = 0
        self.check_column = 0
        self.crit_name_column = 1
        self.crit_type_column = 2
        self.crit_options_column = 3
        self.cost_benefit_column = 4

    def load(self, criteria_recs):
        """Loads the table in the criteria tab with the existing project criteria
        """
        if criteria_recs:
            self.clearContents()

            self.num_rows = len(criteria_recs)
            if not self.num_rows:
                self.num_rows = 0
            self.setRowCount(self.num_rows)
        
            for i in range(self.num_rows):
                name_val = unicode(criteria_recs[i][self.crit_name_column])
                type_val = unicode(criteria_recs[i][self.crit_type_column])
                
                type_opt_val = u""
                if type_val == 'Ordinal' or type_val == 'Binary':
                    for opt in criteria_recs[i][self.crit_options_column]:
                        type_opt_val += u"("+opt[0]+u": "+unicode(opt[1])+u")"
                
                cb_val = unicode(criteria_recs[i][self.cost_benefit_column])
                
                #Add checkbox widget to first column
                check_box = QCheckBox(self)
                self.setCellWidget(i, self.check_column, check_box) 
                #Add criteria description to 2nd column
                name_item = QTableWidgetItem()
                name_item.setText(name_val)
                self.setItem(i, self.crit_name_column, name_item)
                #Add criteria type to 3rd column
                type_item = QTableWidgetItem()
                type_item.setText(type_val)
                self.setItem(i, self.crit_type_column, type_item)
                #Add type options/units to 4th column
                option_item = QTableWidgetItem()
                option_item.setText(type_opt_val)
                self.setItem(i, self.crit_options_column, option_item)
                #Add cost/benefit to 5th column
                cb_item = QTableWidgetItem()
                cb_item.setText(cb_val)
                self.setItem(i, self.cost_benefit_column, cb_item)

                #self.resizeColumnsToContents()

    def check_all(self):
        for i in range(self.num_rows):
            check_box = self.cellWidget(i, self.check_column)
            check_box.setCheckState(Qt.Checked)
            
    def check_one(self, index):
        check_box = self.cellWidget(index, self.check_column)
        check_box.setCheckState(Qt.Checked)
            
    def uncheck_all(self):
        for i in range(self.num_rows):
            check_box = self.cellWidget(i, self.check_column)
            check_box.setCheckState(Qt.Unchecked)

    def get_selected_indexes(self):
        if self.num_rows > 0:
            selected_indexes = []
            for row in range(self.num_rows):
                check_widget = self.cellWidget(row, 0)
                check_state = check_widget.checkState()
                if check_state == Qt.Checked:
                    selected_indexes.append(row)
            return selected_indexes

    def get_current_row_items(self):
        selected_row = self.selectedItems()
        if selected_row:
            #Return the unique criteria description
            return selected_row[0]
        else:
            raise DelphosError, "You must first select a criterion"
        