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
                
                if i == 0:
                    hi = self.horizontalHeaderItem(0)
                    hi.setToolTip("Explicit description of the criterion")
                    hi = self.horizontalHeaderItem(1)
                    hi.setToolTip("General criteria type: Binary, Ordinal, Ratio\nClick help icon for more information")
                    hi = self.horizontalHeaderItem(2)
                    hi.setToolTip("Options are the possible choices for a Binary or Ordinal criterion.\nUnits refers to the unit of measure for a Ratio criterion eg. tons per year")
                    hi = self.horizontalHeaderItem(3)
                    hi.setToolTip("Each criterion can be a Benefit or a Cost.  Click the help icon for more information")
                                        
                name_val = unicode(criteria_recs[i][1])
                type_val = unicode(criteria_recs[i][2])
                type_opt_val = u""
                if type_val == 'Ordinal' or type_val == 'Binary':
                    for opt in criteria_recs[i][3]:
                        type_opt_val += u"("+opt[0]+u": "+unicode(opt[1])+u")"
                cb_val = unicode(criteria_recs[i][4])
                
                #print name_val
                #print type_val
                #print type_opt_val
                #print cb_val
                
                name_item = QTableWidgetItem()
                name_item.setText(name_val)
                self.setItem(i, 0, name_item)
    
                type_item = QTableWidgetItem()
                type_item.setText(type_val)
                self.setItem(i, 1, type_item)
    
                type_opt_item = QTableWidgetItem()
                type_opt_item.setText(type_opt_val)
                self.setItem(i, 2, type_opt_item)
    
                cb_item = QTableWidgetItem()
                cb_item.setText(cb_val)
                self.setItem(i, 3, cb_item)

                self.resizeColumnsToContents()

    def get_selected_row_indexes(self):
        model = self.selectionModel()
        indexes = model.selectedRows(0)
        if indexes:
            #Return the unique criteria description
            return indexes
        else:
            raise DelphosError, "You must first select a criterion"

    def get_first_selected_row_item(self):
        selected_row = self.selectedItems() 
        if selected_row:
            return selected_row[0]  
        else:
            raise DelphosError, "You must first select a criterion"               